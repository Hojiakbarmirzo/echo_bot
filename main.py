import requests
import json
from pprint import pprint

def sentMSG(indx,answer):
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    payload={
        'chat_id':indx,
        'text':answer
    }
    r=requests.get(url,params=payload)


token='1696683157:AAH3NeNVQfFeIwBQtBCAokCOb2hp9_773SQ'

def getUpdates():
    url=f'https://api.telegram.org/bot{token}/getUpdates'
    r=requests.get(url)
    data=r.json()
    updates=data['result']
    return updates


temp=len(getUpdates())

while True:
    if temp != len(getUpdates()):
        temp=len(getUpdates())
        update=getUpdates()[temp-1]
        xat=update['message']
        user=xat['from']
        user_id=user['id']
        text=xat['text']
        sentMSG(user_id,text)
        

        
   

    

