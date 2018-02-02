# sms-forwarder

### Getting started
* Create a [Slack App](https://api.slack.com/slack-apps) and install it on your Slack
* Create an phone number on [Twilio](https://www.twilio.com/) (or other)
* Set your Slack App ApiKey in the slack.py file
* Start the forwarder by running `python app.py`
* In Twilio, create a webhook for incoming message. Forward the payload to POST {{your domain / IP}}:8080

### Options
You can change the target channel in the slack.py file
