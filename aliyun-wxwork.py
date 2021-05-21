#!/usr/bin/env python
# coding=utf-8
from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify
from urlparse import urlparse, parse_qs
import time
import sys
import requests
import json


app = Flask(__name__)

base_path = ''
dedata = {'ret': 0, 'msg': "success"}

# 企业微信群机器人

def send_wechat(md):
    wechat_bot_url = "群机器人webhook地址"
    headers = {'Content-Type': 'application/json'}
    request_data = {"msgtype": "markdown", "markdown": {"content": md}}

    r = requests.post(wechat_bot_url, data=json.dumps(request_data))

@app.route('/', methods=['POST'])
def home():
    # 接收阿里推过来的信息
    a = request.get_data(as_text=True)
    url1 = str(a) #转换成str格式，不然中文规则名会乱码
    url2 = '?&' #加个url截取标志，方便下面提取
    url = url2 + url1
    # 提取url参数
    query = urlparse(url).query
    # 将字符串转换为字典
    params = parse_qs(query)
    result = {key: params[key][0] for key in params}

    timestamp = result['timestamp']  #阿里推过来的时间戳
    alterTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(timestamp[:-3])))   #将时间戳转换成正常时间
    alertState = result['alertState'] #告警状态
    alertName = result['alertName'] #告警规则名
    instanceName = result['instanceName'] #服务器名/ip
    curValue = result['curValue'] #当前值
    expression = (result['expression'])[8:] #规则设置的触发值
    preTriggerLevel = result['preTriggerLevel'] #告警级别

    if alertState == "ALERT":
        md = ("**阿里云监控预警**" + "\n" + "监控项：" + alertName + "\n" + "服务器：" + instanceName + "\n" + "当前值：<font color=\"warning\">" + curValue + "</font>\n" + "触发值：" + expression + "\n" +"告警时间：" + alterTime)
    elif alertState == "OK":
        md = ("**阿里云预警恢复**" + "\n" + "监控项：" + alertName + "\n" + "服务器：" + instanceName + "\n" + "当前值：<font color=\"info\">" + curValue + "</font>\n" + "恢复时间：" + alterTime)
    elif alertState == "INSUFFICIENT_DATA":
        md = "监控数据不足，请登录阿里云检查预警配置！"
    else:
        md = ("接收到未知预警消息，请及时处理!" + url1)

    send_wechat(md)
    return (jsonify(dedata))


def handler(environ, start_response):
    parsed_tuple = urlparse(environ['fc.request_uri'])
    li = parsed_tuple.path.split('/')
    global base_path
    if not base_path:
        base_path = "/".join(li[0:5])
    return app(environ, start_response)