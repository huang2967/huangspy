import requests
import re
import os
import urllib3

urllib3.disable_warnings()

def sign(cookie):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36",
        "Cookie": cookie,
    }
    sign_url = "https://www.52pojie.cn/home.php?mod=task&do=apply&id=2"
    try:
        response = requests.get(
            sign_url,"https://www.52pojie.cn/home.php?mod=spacecp&ac=credit&showcredit=1",
            headers=headers,
            verify=False
        )
        coin = re.findall("吾爱币: </em>(.*?)&nbsp;", response.text)[0]
        point = re.findall("<em>积分: </em>(.*?)<span", response.text)[0]
        return f"吾爱币: {coin}\n积分: {point}"
    except Exception as e:
        return f"签到失败: {str(e)}"

if __name__ == "__main__":
    cookie = os.environ.get("wuai_COOKIE", "")
    if not cookie:
        print("❌ 未配置环境变量 wuai_COOKIE")
    else:
        result = sign(cookie)
        print(result)
