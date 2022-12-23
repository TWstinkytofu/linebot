import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()

machine = TocMachine(
    states=["user","menu", "Create_things","Delete","Update","list","Update_choose","Read","Create","things","name"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "menu",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "name",
            "conditions": "is_going_to_name",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "things",
            "conditions": "is_going_to_things",
        },
        {
            "trigger": "advance",
            "source": "name",
            "dest": "list",
            "conditions": "is_going_to_list",
        },
        {
            "trigger": "advance",
            "source": "list",
            "dest": "Delete",
            "conditions": "is_going_to_Delete",
        },
        {
            "trigger": "advance",
            "source": "list",
            "dest": "Update_choose",
            "conditions": "is_going_to_Update_choose",
        },
        {
            "trigger": "advance",
            "source": "name",
            "dest": "Create_things",
            "conditions": "is_going_to_Create_things",
        },
        {
            "trigger": "advance",
            "source": "name",
            "dest": "Read",
            "conditions": "is_going_to_Read",
        },
        {
            "trigger": "advance",
            "source": "Create_things",
            "dest": "Create",
        },
        {
            "trigger": "advance",
            "source": "Update_choose",
            "dest": "Update",
        },
        {   "trigger": "error", 
            "source": ["menu","list","name","Update_choose"],
            "dest": "menu"
        },
        {   "trigger": "show_menu", 
            "source": ["things","Delete","Update","Read","Create"],
            "dest": "menu"
        },
        {   "trigger": "advance", 
            "source": "menu",
            "dest": "list",
            "conditions": "go_back_list"
        },
        {   "trigger": "advance", 
            "source": "menu",
            "dest": "Update_choose",
            "conditions": "go_back_Update_choose"
        },
        {   "trigger": "advance", 
            "source": "menu",
            "dest": "Delete",
            "conditions": "go_back_Delete"
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = "your channel_secret"
channel_access_token = "your channel_access_token"
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        response = machine.advance(event)
        print(f"\nFSM STATE: {machine.state}")
        if response == False:
            machine.error(event)
            machine.set_error()
            send_text_message(event.reply_token, "Back to menu")
        machine.show_menu(event)

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
