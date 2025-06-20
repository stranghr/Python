from flask import Flask, request
import requests
import os

app = Flask(__name__)

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")        # 환경변수에서 불러옴
NOTICE_CHANNEL = os.environ.get("NOTICE_CHANNEL")          # 예: C01ABCDE1

@app.route("/gongji", methods=["POST"])
def gongji():
    text = request.form.get("text")                        # 사용자가 입력한 내용
    user_name = request.form.get("user_name")              # 누가 보냈는지

    if not text:
        return "공지 내용이 비어있습니다.", 200

    message = f":loudspeaker: *{user_name}의 공지:* {text}"

    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "channel": NOTICE_CHANNEL,
        "text": message
    }

    # Slack으로 메시지 전송
    requests.post("https://slack.com/api/chat.postMessage", headers=headers, json=payload)

    return "공지 전송 완료", 200
