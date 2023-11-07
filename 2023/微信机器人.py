import pymysql
from flask import Flask, request, jsonify
import json
import requests
from wx_api import send_message, query_info_by_wxid, query_group_list, query_group_members, confirm_payment, agree
from find_info import get_wx_info
from datetime import datetime

app = Flask(__name__)
# 连接到本地 MySQL 数据库
connection = pymysql.connect(host='localhost', user='root', password='123456', database='KGGOGO', charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def process_event_10009(message_dict):
    rootID = "wxid_0q2jr040l8hf22"
    rootID1 = "1"
    # 群ID
    fromWxid = message_dict['data']['data'].get('fromWxid')
    msg = message_dict['data']['data'].get('msg')
    timeStamp = message_dict['data']['data'].get('timeStamp')

    # 管理员功能
    if fromWxid == rootID or fromWxid == rootID1:
        # 上传商品命令 XX团购XX元
        if '功能' in msg:
            send_message(fromWxid,
                         "命令包含:\n 功能:查询功能和其命令 \n XX团购XX元:上传XX商品 团购一份价格为XX\n修改XX为XX元:修改XX商品，价格一份变为XX元）\n 开始接龙XX:开始接龙XX商品，")
        if '团购' in msg and '元' in msg:
            # 获取商品名称和价格
            start_idx = msg.index('团购')
            start_idx1 = msg.index('团购') + 2
            end_idx = msg.index('元')
            name = msg[0:start_idx]
            price = msg[start_idx1:end_idx]
            # 添加到数据库
            try:
                with connection.cursor() as cursor:
                    # 插入数据到商品列表表中
                    sql1 = "select `商品名称` from `商品列表` where `商品名称` = %s "
                    cursor.execute(sql1, (name,))
                    result = cursor.fetchall()
                    if result:
                        send_message(fromWxid, f" {name} 商品已经有了，可以更改其价格或上传其他商品 ")
                    else:
                        sql2 = "INSERT INTO `商品列表` (`商品名称`, `团购价格`) VALUES (%s, %s)"
                        cursor.execute(sql2, (name, price))
                        # 提交更改
                        connection.commit()
                        send_message(fromWxid, f"上传商品成功\n上传 {name} 商品 一份{price}元")
            except Exception as e:
                send_message(fromWxid, f"错误{e}，请联系管理员")

        if '删除' in msg:
            try:
                start_idx = msg.index('删除') + 2
                end_idx = msg.index('商')
                name = msg[start_idx:end_idx]
                # 删除某商品
                with connection.cursor() as cursor:
                    sql = "DELETE FROM `商品列表` WHERE `商品名称` = %s "
                    cursor.execute(sql, (name,))

                # 提交更改
                connection.commit()
                send_message(fromWxid, f"商品 {name} 已删除。")

            except Exception as e:
                send_message(fromWxid, f"错误{e}，请联系管理员")

        if '修改' in msg and '为' in msg and '元' in msg:
            try:
                # 获取商品名称和价格
                start_idx = msg.index('修改') + 2
                end_idx = msg.index('为')
                name = msg[start_idx:end_idx]

                start_idx = msg.index('为') + 1
                end_idx = msg.index('元')
                price = msg[start_idx:end_idx]

                # 更新商品价格到数据库
                with connection.cursor() as cursor:
                    sql = "UPDATE `商品列表` SET `团购价格` = %s WHERE `商品名称` = %s"
                    cursor.execute(sql, (price, name))

                # 提交更改
                connection.commit()
                send_message(fromWxid, f"商品'{name}'的价格已更新为'{price}'元。")

            except Exception as e:
                send_message(fromWxid, f"错误{e}，请联系管理员")
        # 商品 或 团品 查询 已经有的商品和价格列表
        if '商品' in msg or '团品' in msg:
            try:
                # 查询商品列表和价格
                with connection.cursor() as cursor:
                    sql = "SELECT `商品名称`, `团购价格` FROM `商品列表`"
                    cursor.execute(sql)
                    result = cursor.fetchall()

                # 输出查询结果
                if result:
                    for row in result:
                        send_message(fromWxid, f"商品名称：{row['商品名称']}，团购价格：{row['团购价格']}元")
                else:
                    send_message(fromWxid, "暂无商品信息。")

            except Exception as e:
                send_message(fromWxid, f"错误{e}，请联系管理员")


        # 停止接龙命令 ，让数据库 拼单状态为1的=0
        elif '截单' in msg:
            try:
                # 获取数据库游标
                with connection.cursor() as cursor:
                    # 将拼单状态为1的记录更新为0
                    sql_update = "UPDATE 团购单号信息表 SET 是否在接龙 = 0 "
                    sql_update1 = "UPDATE 商品列表 SET 是否正在接龙 = 0 "
                    sql_update2 = "UPDATE 接龙 SET 是否接龙 = 0 "
                    sql_update3 = "UPDATE 接龙 SET 接龙msg = '' "
                    cursor.execute(sql_update)
                    cursor.execute(sql_update1)
                    cursor.execute(sql_update2)
                    cursor.execute(sql_update3)
                    # 提交更改
                connection.commit()
                send_message(fromWxid, "已截单")
            except Exception as e:
                # 处理可能的异常
                send_message(fromWxid, f"错误{e}，截单失败，请联系管理员")
        # 开始接龙命令 开始接龙XX ，查找该商品，并且使其是否正在接龙=1，并在团购订单信息中添加信息

        elif '开始接龙' in msg:
            # 将时间戳转换为 datetime 对象
            timeStamp = float(timeStamp)
            dt_object = datetime.fromtimestamp(timeStamp / 1000.0)  # 需要除以1000转换为秒
            # 将 datetime 对象格式化为字符串
            formatted_time = dt_object.strftime('%Y%m%d')
            # 格式化后的时间字符串，例如：20230807
            try:
                # 获取数据库游标
                with connection.cursor() as cursor:
                    # 获取商品名称
                    start_idx = msg.index('开始接龙') + 4
                    name = msg[start_idx:]

                    # 在"商品列表"表中查找商品
                    sql_select = "SELECT * FROM 商品列表 WHERE 商品名称 = %s"
                    cursor.execute(sql_select, (name,))
                    result = cursor.fetchone()

                    if result:
                        dingdanhao = formatted_time + name
                        sql1 = "SELECT `团购价格` FROM `商品列表` WHERE 商品名称 = %s"
                        cursor.execute(sql1, (name,))
                        result = cursor.fetchone()
                        price = result['团购价格']
                        # 如果商品存在，插入新的团购信息到团购单号信息表中
                        sql_insert = "INSERT INTO `团购单号信息表` (`团购单号`, `商品`, `商品价格`, `是否在接龙`) VALUES (%s, %s, %s,%s)"
                        cursor.execute(sql_insert, (dingdanhao, name, price, 1))

                        # 更新商品列表中的是否正在接龙状态为1
                        sql_update2 = "UPDATE 商品列表 SET 是否正在接龙 = 1 WHERE 商品名称 = %s"
                        cursor.execute(sql_update2, (name,))

                        connection.commit()

                        send_message(fromWxid, "开始成功，机器人开始工作啦")
                    else:
                        # 如果商品不存在，返回提示信息
                        send_message(fromWxid, f"商品列表没有{name}商品，请上传后再接龙。")
            except Exception as e:
                # 处理可能的异常
                send_message(fromWxid, f"错误{e}，开始接龙失败，请联系管理员")
        # 没付款查询
        elif '没付款' in msg:
            try:
                # 获取数据库游标
                with connection.cursor() as cursor:
                    sql = "SELECT 微信名称 FROM 团购信息 WHERE 是否付款 = 0"
                    cursor.execute(sql)
                    result = cursor.fetchone()
                    send_message(fromWxid, result)
                connection.commit()
            except Exception as e:
                # 处理可能的异常
                send_message(fromWxid, f"错误{e}，查询失败，请联系管理员")

        # 查询团购谁没拿的命令
        elif '没拿' in msg:
            try:
                # 获取数据库游标
                with connection.cursor() as cursor:
                    # 查询拼单状态为0的微信名称
                    sql = "SELECT 微信名称,团购商品 FROM 团购信息 WHERE 是否已领 = 0"
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    wx_and_goods = [(row['微信名称'], row['团购商品']) for row in result]
                    send_message(fromWxid, wx_and_goods)
                connection.commit()
            except Exception as e:
                # 处理可能的异常
                send_message(fromWxid, f"错误{e}，查询失败，请联系管理员")
    else:
        # 会员，付款和完成订单，积分以及积分 查询兑换
        # 首先如果没在数据库，进入数据库
        if '积分' in msg:
            try:
                # 获取数据库游标
                with connection.cursor() as cursor:
                    # 查询wxid所在行的剩余积分
                    sql = "SELECT 剩余积分 FROM wx会员 WHERE 微信ID = %s"
                    cursor.execute(sql, (fromWxid,))
                    result = cursor.fetchone()

                    if result:
                        remaining_points = result['剩余积分']
                        send_message(fromWxid, f"你的积分为{remaining_points}。")
                        send_message(fromWxid, "输入'兑换'可以积分兑换鸡蛋，100积分获得五个鸡蛋。鸡蛋需要当天领取")
            except Exception as e:
                # 处理可能的异常
                send_message(fromWxid, "异常错误，请联系管理员")
        elif '兑换' in msg:
            try:
                # 获取数据库游标
                with connection.cursor() as cursor:
                    # 查询wxid所在行的剩余积分
                    sql = "SELECT 剩余积分 FROM wx会员 WHERE 微信ID = %s"
                    cursor.execute(sql, (fromWxid,))
                    result = cursor.fetchone()

                    if result:
                        remaining_points = result['剩余积分']

                        if remaining_points >= 100:
                            # 更新剩余积分和已兑换积分并输出兑换成功信息
                            new_remaining_points = remaining_points - 100
                            sql_update = "UPDATE wx会员 SET 剩余积分 = %s, 已兑换积分 = 已兑换积分 + 100 WHERE 微信ID = %s"
                            cursor.execute(sql_update, (new_remaining_points, fromWxid))
                            connection.commit()
                            send_message(fromWxid, "兑换成功，请当天领取鸡蛋。")
                        else:
                            send_message(fromWxid, "剩余积分不足100。")
            except Exception as e:
                # 处理可能的异常
                send_message(fromWxid, "异常错误，请联系管理员")

        elif '完成' in msg:
            try:
                # 获取数据库游标
                with connection.cursor() as cursor:
                    # 更新团购信息表中对应wxid的行，将完成状态设置为1
                    sql_update = "UPDATE 团购信息 SET 是否完成 = 1,是否领取 =1 WHERE 微信ID = %s"
                    cursor.execute(sql_update, (fromWxid,))
                    # 查询团购信息，用wx查询订单，是否付款，如果付款=1，增加 商品价格*份数   ，else print（“机器人没收到付款，统计功能失败，可以联系管理员”）
                    # 缺少订单唯一标识
                    sql_update1 = "UPDATE vx会员 SET 历史获得积分 = 1,已兑换积分 =1 WHERE 剩余积分 = %s"
                    connection.commit()
                    print("团购信息已更新，已完成团购。")
            except Exception as e:
                # 处理可能的异常
                print("更新团购信息失败:", e)
        elif '成为会员' in msg:
            # 如果 wxid 不在本地表中
            if not is_wxid_in_local_table(fromWxid):
                # 查询用户信息并添加到本地 MySQL 数据库的 wx会员 表和团购信息表
                user_info = query_user_info(fromWxid)
                if user_info:
                    add_user_to_local_table(user_info)
                    send_message(fromWxid, "恭喜成为会员，团购积累积分可兑换鸡蛋，100积分兑换5个鸡蛋")


def process_event_10003(message_dict):
    # 确认收款，看收款的金额是否正确，正确接受，并查询数据，上传确认付款
    money = user_dict['data']['data'].get('money')
    fromWxid = user_dict['data']['data'].get('fromWxid')
    transferid = user_dict['data']['data'].get('transferid')
    nick = get_wx_info(fromWxid).get('nick')
    # 从数据库团购单号信息找到正在团购的商品单号，

    dingdanhao = dingdanhao + '-' + wx_info['nick']
    sql_query = "SELECT 份数, 团品价格 FROM 团购信息 WHERE wxid = %s and 是否付款 = 0 and 订单号 = %s"
    cursor.execute(sql_query, (fromWxid, dingdanhao))

    result = cursor.fetchone()

    if result:
        groupbuy_count = result['份数']
        groupbuy_price = result['团品价格']

        # 计算期望收款金额
        expected_money = groupbuy_count * groupbuy_price

        if money == expected_money:
            confirm_payment(fromWxid, transferid)
            a = f"您已经付款成功，一共收到{money}元。/n拿到团品后输入完成可获得积分哦，积分可以兑换鸡蛋，但是请不要提前输入完成)"
            send_message(fromWxid, a)
        else:
            # 输出金额不正确的提示信息
            error_msg = f"您定了{groupbuy_count}份，一份{groupbuy_price}元，需要转账{expected_money}元，数额不对无法收款，请转账准确金额，多余金额24小时后自动退款"
            send_message(fromWxid, error_msg)
    else:
        # 输出找不到团购信息的提示信息
        print("找不到对应的团购信息，无法确认收款。")


def process_event_10008(message_dict):
    wxid = message_dict.get('wxid')
    des = message_dict['data'].get('des')
    timeStamp = message_dict['data']['data'].get('timeStamp')
    fromWxid = message_dict['data']['data'].get('fromWxid')
    finalFromWxid = message_dict['data']['data'].get('finalFromWxid')
    msg = message_dict['data']['data'].get('msg')

    # 在这里进行 event 为 10008 的逻辑处理
    # 如果 msg 中包含 "#接龙" 字样，执行接龙功能
    if "接龙" in msg:
        result = do_jielong(fromWxid, finalFromWxid, msg, timeStamp)
        return result


def process_event_10011(message_dict):
    v3 = message_dict['data']['data']['v3']
    v4 = message_dict['data']['data']['v4']
    wxid = message_dict['data']['data']['wxid']
    response_data = agree(v3, v4)
    if response_data["msg"] == "操作成功":
        send_message(wxid, "向我发送 '成为会员',成功团购就可获得积分，积分可兑换鸡蛋哦 ")


def do_jielong(fromWxid, finalFromWxid, msg, timeStamp):
    info = get_wx_info(finalFromWxid)
    # 如果是新的接龙信息，储存该信息
    # 这里查询数据库 接龙 开始接龙为1的
    try:
        with connection.cursor() as cursor:
            # 查询接龙msg，where 所在群 = ‘’
            sql = "SELECT `接龙msg` FROM `接龙` WHERE `所在群` = %s"
            cursor.execute(sql, (fromWxid,))
            result = cursor.fetchone()
            jielong_info = result.get('接龙msg', '')
    except Exception as e:
        send_message(fromWxid, f"错误{e}，请联系管理员")
    # 管理员在群里发送#接龙 让大家接龙
    if "#接龙" in msg and not jielong_info:

        # 上传数据库 ’接龙msg‘表  ， 表里有     团购单号       接龙  是否接龙  是否截单  ，接龙是否为空
        jielong_info = msg
        # 更新数据库 接龙 信息
        reply = "大家好，接龙开始了！\n加我好友，群里直接回复’接龙+份数‘就可以参与接龙了。\n接龙更方便"
        # 更新 '接龙msg' 字段
        try:
            with connection.cursor() as cursor:
                # 更新接龙msg字段
                sql = "UPDATE `接龙` SET `接龙msg` = %s WHERE `所在群` = %s"
                cursor.execute(sql, (jielong_info, fromWxid))
                connection.commit()
                send_message(fromWxid, reply)
        except Exception as e:
            send_message(fromWxid, "失败,可以联系管理员")

    # 如果接龙信息已储存，且有人回复“我要接龙”，无论会员不会员,更新接龙信息,
    # 查询数据库  接龙为1 的行里 接龙是否不空
    elif "#接龙" in msg and jielong_info and len(msg) > 20:
        try:
            with connection.cursor() as cursor:
                # 更新接龙msg字段
                sql = "UPDATE `接龙` SET `接龙msg` = %s WHERE `所在群` = %s"
                cursor.execute(sql, (msg, fromWxid))
                connection.commit()
                return True  # 更新成功返回True

        except Exception as e:
            print("数据库更新出错:", str(e))
            return False  # 更新失败返回False
    # 判断是否为会员
    elif "接龙" in msg and "#接龙" not in msg and jielong_info:
        try:
            with connection.cursor() as cursor:
                # 查询wxid所在行的信息
                sql = "SELECT * FROM wx会员 WHERE 微信ID = %s"
                cursor.execute(sql, (wxid,))
                result = cursor.fetchone()

                if result:
                    nick = info.get('nick')
                    msg1 = chinese_number_to_integer(msg)
                    if jielong_number_match:
                        jielong_number = re.search(r'\d+', msg1)
                    else:
                        # 如果没有找到接龙份数，则默认为一份
                        jielong_number = 1

                    if nick:
                        jielong_info += f"\n{len(jielong_info.splitlines())}. {nick.strip()} {jielong_number}份"
                        # 发送接龙信息到群里
                        send_message(wxid, jielong_info)
                        try:
                            with connection.cursor() as cursor:
                                # 更新接龙msg字段
                                sql = "UPDATE `接龙` SET `接龙msg` = %s  WHERE `所在群` = %s"
                                cursor.execute(sql, (msg, fromWxid))
                                connection.commit()
                                return True  # 更新成功返回True

                        except Exception as e:
                            print("数据库更新出错:", str(e))
                            return False  # 更新失败返回False
                        # 从团购单号信息表找取 是否在接龙 = 1 的 名称 价格 单号
                        groupbuy_info = query_groupbuy_info()
                        if groupbuy_info:
                            # 将会员参与团购信息添加到本地 MySQL 数据库的 #添加到团购信息里
                            add_groupbuy_to_local_table(groupbuy_info, finalFromWxid, fromWxid, jielong_number)

                        # 向用户发送一串信息
                        send_auto_reply(FromWxid, "您已成功参与接龙，谢谢！")
                        send_auto_reply(FromWxid, "金额可直接转我，订单完成后积分")


                else:
                    content = "你好我是接龙小机器人，添加我好友后，向我发送'成为会员'在群里发送'接龙'可以直接参与接龙哦"
                    send_message(fromWxid, content)
                    return

        except Exception as e:
            print("数据库查询出错:", str(e))
            return None


def is_wxid_in_local_table(wxid):
    with connection.cursor() as cursor:
        sql = "SELECT COUNT(*) AS count FROM `wx会员` WHERE `微信ID`=%s"
        cursor.execute(sql, (wxid,))
        result = cursor.fetchone()
        return result['count'] > 0


def query_user_info(wxid):
    user_info = []
    info = get_wx_info(wxid)
    nick = info.get('nick')
    vxid = info.get('wxid')
    wxNum = info.get('wxNum')
    user_info.append((nick, vxid, wxNum))
    return user_info


def add_user_to_local_table(user_info):
    # 在这里实现将用户信息添加到本地 MySQL 数据库的数据表
    with connection.cursor() as cursor:
        sql = "INSERT INTO `wx会员` (`微信名称`, `微信ID`, `微信号`) VALUES (%s, %s, %s)"
        cursor.executemany(sql, user_info)

        sql1 = "INSERT INTO `会员团购表` (`微信名称`, `微信ID`, `微信号`) VALUES (%s, %s, %s)"
        cursor.executemany(sql1, user_info)

        connection.commit()


def query_groupbuy_info():
    groupbuy_info = []
    with connection.cursor() as cursor:
        sql = "SELECT 商品, 商品价格, 团购单号 FROM 团购单号信息表 WHERE 是否在接龙 = 1"
        cursor.execute(sql)
        result = cursor.fetchone()

        if result:
            商品名称 = result["商品"]
            商品价格 = result["商品价格"]
            团购单号 = result["团购单号"]
            groupbuy_info.append((商品名称, 价格, 团购单号))

    return groupbuy_info


def add_groupbuy_to_local_table(info, wxid, a, jielong_number):
    wx_info = get_wx_info(wxid)
    dingdanhao = info[0][2] + '-' + wx_info['nick']
    with connection.cursor() as cursor:
        sql = "INSERT INTO `团购信息` (`微信名称`, `微信ID`, `微信号`, `所在群`, `团购单号`, `团购商品`, `商品价格`, `份数`, `订单号`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (
        wx_info['nick'], wx_info['wxid'], a, wx_info['wxNum'], info[0][2], info[0][0], info[0][1], jielong_number,
        dingdanhao), )


def chinese_number_to_integer(chinese_number):
    chinese_numbers = {
        "一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
        "六": 6, "七": 7, "八": 8, "九": 9, "十": 10,
        "十一": 11, "十二": 12, "十三": 13, "十四": 14, "十五": 15,
        "十六": 16, "十七": 17, "十八": 18, "十九": 19, "二十": 20,
        "二十一": 21, "二十二": 22, "二十三": 23, "二十四": 24, "二十五": 25,
        "二十六": 26, "二十七": 27, "二十八": 28, "二十九": 29, "三十": 30,
        "三十一": 31, "三十二": 32, "三十三": 33, "三十四": 34, "三十五": 35,
        "三十六": 36, "三十七": 37, "三十八": 38, "三十九": 39, "四十": 40,
        "四十一": 41, "四十二": 42, "四十三": 43, "四十四": 44, "四十五": 45,
        "四十六": 46, "四十七": 47, "四十八": 48, "四十九": 49, "五十": 50
    }

    number = ""
    result = 0
    for char in chinese_number:
        if char in chinese_numbers:
            number += str(chinese_numbers[char])
        else:
            number += char

    try:
        result = int(number)
    except ValueError:
        print("Invalid input")

    return result


@app.route('/callback', methods=['POST'])
def receive_message():
    message = request.get_data()
    message_dict = json.loads(message.decode('utf-8'))

    event = message_dict.get('event')

    if event == 10008:
        result = process_event_10008(message_dict)
        return jsonify({"status": "success", "result": result})

    elif event == 10009:
        result = process_event_10009(message_dict)
        return jsonify({"status": "success", "result": result})

    elif event == 10003:
        result = process_event_10003(message_dict)
        return jsonify({"status": "success"})

    elif event == 10011:
        result = process_event_10011(message_dict)
        return jsonify({"status": "success"})

    return jsonify({"status": "success"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)