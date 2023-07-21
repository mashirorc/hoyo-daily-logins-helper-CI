import os

from onepush import get_notifier

WEBHOOK = os.environ['WEBHOOK']


#if "Message: OK" not in log_content:
n = get_notifier('discord')
print(n.params)  
    
response = n.notify(webhook=WEBHOOK,content=log_content)
print(response.text) 
