# Python

Sample Slack gongji service

Environment variables:

- `SLACK_BOT_TOKEN` : Slack OAuth token with `chat:write` permission.

Usage:

`/공지 -채널 내용`

The first word after the command indicates the target channel (optionally prefixed with `-`). The remaining text is posted to that channel.
