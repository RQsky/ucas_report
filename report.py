import time
import requests

url = "https://app.ucas.ac.cn/ncov/api/default/save"        # 学院填报接口
mes_url = ""                                                # server酱的接口

cookies = {
    "eai-sess": "",
    "UUkey": ""
}

data = {
    "realname": "",  # 姓名
    "number": "",  # 学号

    "szgj_api_info": "{\"area\":{\"label\":\"\",\"value\":\"\"},\"city\":{\"label\":\"\",\"value\":\"\"},\"address\":\"\",\"country\":{\"label\":\"\",\"value\":\"\"},\"details\":\"\",\"province\":{\"label\":\"\",\"value\":\"\"}}",
    "sfzx": "0",    # 是否在校
    "szdd": "国内",  # 所在地点
    "ismoved": "1",
    "tw": "3",       # 体温选项序号
    "sfcxtz": "0",
    "sfjcbh": "0",   # 是否接触病患
    "sfcyglq": "0",  # 是否处于隔离期
    "sfcxzysx": "0",
    "old_szdd": "国内",
    "geo_api_info": "{\"address\":\"北京市海淀区\",\"details\":\"中关村街道智能化大厦自动化大厦(中关村东路)\",\"province\":{\"label\":\"北京市\",\"value\":\"\"},\"city\":{\"label\":\"\",\"value\":\"\"},\"area\":{\"label\":\"海淀区\",\"value\":\"\"}}",
    "old_city": "{\"address\":\"北京市海淀区\",\"details\":\"中关村街道智能化大厦自动化大厦(中关村东路)\",\"province\":{\"label\":\"北京市\",\"value\":\"\"},\"city\":{\"label\":\"\",\"value\":\"\"},\"area\":{\"label\":\"海淀区\",\"value\":\"\"}}",
    "geo_api_infot": "{\"address\":\"\",\"details\":\"\",\"country\":{\"label\":\"\",\"value\":\"\"},\"province\":{\"label\":\"\",\"value\":\"\"},\"city\":{\"label\":\"\",\"value\":\"\"},\"area\":{\"label\":\"\",\"value\":\"\"}}",
    "date": time.strftime("%Y-%m-%d", time.localtime()),
    "jcjgqk": "1",
    "jrsflj": "否",      # 今日是否离京
    "jrsfdgzgfxdq": "否",  # 今日是否到过中高风险地区
    "gtshcyjkzt": "正常",  # 共同生活成员健康状态
    "app_id": "ucas",

    # "szgj": "",
    # "old_sfzx": "",
    # "bztcyy": "",
    # "sfyyjc": "",
    # "jcjgqr": "",
    # "jcbhlx": "",
    # "gllx": "",
    # "fjsj": "",
    # "jcbhrq": "",
    # "glksrq": "",
    # "fxyy": "",
    # "jcjg": "",
    # "jcjgt": "",
    # "qksm": "",
    # "remark": "",
    # "ljrq": "",
    # "qwhd": "",
    # "chdfj": "",
    # "ddd": ""
}

result = requests.post(url=url, data=data,cookies=cookies)

if mes_url:
    if result.text[5] == "0":
        payload = {'text': '填报成功'}
    elif result.text[5] == "1":
        payload = {'text': '请勿重复填报'}
    else:
        payload = {'text': '未知错误'}
    requests.get(url=mes_url, params=payload)
# print(result.text)

