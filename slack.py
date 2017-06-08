from slacker import Slacker

slack = Slacker('API KEY HERE')

def post(message):
    slack.chat.post_message('#general', message)
