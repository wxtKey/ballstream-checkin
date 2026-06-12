import os
import requests

EMAIL = os.environ["BALL_EMAIL"]
PASSWORD = os.environ["BALL_PASSWORD"]

s = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0"
}

# 登录
login = s.post(
    "https://bbs.ball.stream/api/auth/login",
    json={
        "login": EMAIL,
        "password": PASSWORD
    },
    headers=headers
)

print("=== LOGIN ===")
print(login.text)

print("=== COOKIES ===")
print(s.cookies.get_dict())

# 签到
checkin = s.post(
    "https://bbs.ball.stream/api/checkin",
    headers={
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://bbs.ball.stream/?v=checkin",
        "Origin": "https://bbs.ball.stream"
    }
)

print("=== CHECKIN ===")
print("Status:", checkin.status_code)
print(checkin.text[:1000])
