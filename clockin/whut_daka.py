#!/usr/bin/python3
from email.message import EmailMessage
import requests, json
from smtplib import SMTP
import smtplib
import time

headers = {
    "Host": "zhxg.whut.edu.cn",
    "Connection": "keep-alive",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 "
        "NetType/WIFI MiniProgramEnv/Windows WindowsWechat"
    ),
    "Cookie": "JSESSIONID=d24b441d-c536-4432-bb91-13d387c2a5c1",
    "X-Tag": "flyio",
    "content-type": "application/json",
    "Referer": "https://servicewechat.com/wxa0738e54aae84423/5/page-frame.html",
    "Accept-Encoding": "gzip, deflate, br",
}

# 系统设置代理后，需要这个才能发出请求。
# 需要pip 安装pysocks socks 包
"""
proxy={
        'http':'socks5://127.0.0.1:7890',
        'https':'socks5://127.0.0.1:7890'
        }
"""
# 原始发包数据
postdata = {
    "diagnosisName": "",
    "relationWithOwn": "",
    "currentAddress": "湖北省武汉市武昌区友谊大道",
    "remark": "",
    "healthInfo": "正常",
    "isDiagnosis": 0,
    "isFever": 0,
    "isInSchool": 1,
    "isLeaveChengdu": 0,
    "isSymptom": "0",
    "temperature": '36"C~36.5°C',
    "province": "湖北省",
    "city": "武汉市",
    "county": "武昌区",
}
url = "https://zhxg.whut.edu.cn/yqtjwx/monitorRegister"
session = requests.Session()

# 吴涛
"""
postdata['currentAddress']="湖北省黄石市黄石港区彩虹路"
postdata['isInSchool']="0"
postdata['province']="湖北省"
postdata['city']="黄石市"
postdata['county']="黄石港区"

def wutao():
    response = session.post(url, data=json.dumps(postdata), headers=headers)#, proxies=proxy)
    print(response.text);
    session.close();
    return response.text


#郭亚文
def guoyawen():
    headers['Cookie']='JSESSIONID=3df7ce21-c1ec-42f8-8e8f-22a19b74dd8c';
    response = session.post(url, data=json.dumps(postdata), headers=headers)# ,proxies=proxy)
    print(response.text)
    session.close();
    return response.text
"""
# 这是 张超杰的 在家的打卡， 返校后将这五个  postdata  注释了就可以了。
postdata["currentAddress"] = "河南省周口市淮阳区009县道"
postdata["isInSchool"] = "0"
postdata["province"] = "河南省"
postdata["city"] = "周口市"
postdata["county"] = "淮阳区"


# 张超杰
def zhang():
    #  这里是 Cookie,  若发包失败，则这里需要重新抓包，获取新的Cookie
    headers["Cookie"] = "JSESSIONID=686c04f5-fe10-47d6-90f3-6705e9879601"
    response = session.post(
        url, data=json.dumps(postdata), headers=headers
    )  # , proxies=proxy)
    print(response.text)
    session.close()
    # 这里调用发送邮件
    res = response.json()
    mail(res)
    return response.text


"""
postdata['currentAddress']="湖北省孝感市云梦县隔蒲镇黄金村一组"
postdata['isInSchool']="0"
postdata['province']="湖北省"
postdata['city']="孝感市"
postdata['county']="云梦县"

#褚志刚
def chu():
    headers['Cookie']='JSESSIONID=17eb562e-f613-4b25-b686-8b9bb9ed4e81';
    response = session.post(url, data=json.dumps(postdata), headers=headers)#, proxies=proxy)
    print(response.text);
    session.close();
    res=response.json()
    mail_response = mail(res)
    return response.text + '\n' + mail_response
"""


# 发送邮件程序。 如果不能运行，就看官方文档的例子重新实现
def mail(res):
    mail_host = "smtp.qq.com"
    mail_user = "1148636359@qq.com"  # 发送邮件的发件人
    mail_pass = "keaaxrutovczhcbf"  # 发送邮件发件人的权限密码

    sender = "1148636359@qq.com"
    receiver = ["1148636359g@gmail.com"]  # 邮件收件人，可改，可加。
    if res["status"] or res["message"] == "今日已填报":
        str = "健康打卡成功！"
    else:
        str = "健康打卡失败！"
    # 设置发送邮件的内容
    message = EmailMessage()
    message.set_content(str)

    message["From"] = sender
    message["To"] = receiver
    subject = "Python SMTP 发送邮件"
    # 设置发送的主题（标题）
    message["Subject"] = subject

    try:
        smtpObj = SMTP(mail_host, 587)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receiver, message.as_string())
        print("Successful")
        out_text = "Successful"
    except smtplib.SMTPException as e:
        print(e)
        print("Error")
        out_text = "Error"
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    out_text = out_text + "\n" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return out_text


# 主函数调用，不需要改。  现在只调用了 张超杰的打卡。
def main():
    # wutao()
    # guoyawen()
    # zhang()
    # chu()
    json_text = {"status": 200, "message": "今日已填报"}
    mail(json_text)


if __name__ == "__main__":
    main()
