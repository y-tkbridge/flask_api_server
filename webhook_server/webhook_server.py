#coding: utf-8

from flask import Flask, request, jsonify, make_response
from slackclient import SlackClient
import requests, os, json

slack_token = os.getenv("SLACK_API_TOKEN")
print(slack_token)
client = SlackClient(slack_token)

app = Flask(__name__)
message_body = None

@app.route("/ytakahashi-profile", methods=['GET'])
def get():
    result = {"y-takahashi-jsonprofile": {
        "name":"Yuta Takahashi",
        "job":"web engineer",
        "portfolio":"https://y-tkbridge.github.io/Portfolio/index.html",
        "skills":[
            {
            "ruby":"made chatbot",
            "ruby on rails":"made web app and rails tutorial ",
            "python":"virus hash automation Evaluation　and Raspberrypi3 iot unit",
            "javascript":"made spa todo app question app",
            "html":"spa todo and portfolio",
            "css":"spa todo and portfolio",
            },
            {
            "aws":"ec2,elb,autoscaling,ecs,codebuild,rds,r53,s3,iam",
            "gcp":"firebase,hosting app",
            "linux":"ubunt7 debian ubuntu  shell is fish bash "
            }
            ]
        }
    }

    return make_response(jsonify(result))

@app.route("/test-takahashi-api", methods=["POST"])
def post():
    print request.headers
    print "body: %s" % request.data
    create_backlog_message(request.data)
    return request.data

def create_backlog_message(messages):
    backlog_json_load_dic = json.loads(messages)

def post_slack(text):
    print("post")
    requests.post(
        post_url,
        data=json.dumps(
            {"text": text}))

def channel_list(client):
    channels = client.api_call("channels.list")
    if channels['ok']:
        return channels['channels']
    else:
        return None

app.run(host="127.0.0.1", port=8000)
