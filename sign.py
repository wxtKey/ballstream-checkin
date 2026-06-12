import os
import requests

EMAIL = os.environ["BALL_EMAIL"]
PASSWORD = os.environ["BALL_PASSWORD"]

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0"
}

# 登录
login = session.post(
    "https://bbs.ball.stream/api/auth/login",
    json={
        "login": EMAIL,
        "password": PASSWORD
    },
    headers=headers,
    timeout=30
)

print("登录结果：")
print(login.text)

# 签到
checkin = session.post(
    "https://bbs.ball.stream/api/checkin",
    headers=headers,
    timeout=30
)

print("签到结果：")
print(checkin.text)
