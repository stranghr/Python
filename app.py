from flask import Flask, request
import requests
import os

app = Flask(__name__)

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")        # 슬랙 봇 토큰

@app.route("/gongji", methods=["POST"])
def gongji():
    text = request.form.get("text", "").strip()            # 명령 뒤의 전체 입력
    user_name = request.form.get("user_name")              # 누가 보냈는지

    if not text:
        return "사용법: /공지 -채널 내용", 200

    # 첫 단어는 대상 채널, 나머지는 공지 내용
    parts = text.split(None, 1)
    if len(parts) < 2:
        return "사용법: /공지 -채널 내용", 200

    channel_token, message = parts
    if channel_token.startswith("-"):
        target_channel = channel_token[1:]
    else:
        target_channel = channel_token

    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "channel": target_channel,
        "text": message
    }

    # Slack으로 메시지 전송
    requests.post("https://slack.com/api/chat.postMessage", headers=headers, json=payload)

    return "공지 전송 완료", 200
