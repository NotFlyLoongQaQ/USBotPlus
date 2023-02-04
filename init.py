"""
        BlocksTeam 2022-2023        
        By: NotFlyLoong
"""

import json
import random
import requests
import websocket

labby1 = 'http://您的usbot节点/api/auth/labby1/'

class Gun():
    def __init__(self, name , labbys, rooms):
        self.name = name
        self.labbys = labbys
    
    def checkRoom(self, room):
        check_ws = websocket.create_connection('wss://hack.chat/chat-ws',sslopt={"cert_reqs":ssl.CERT_NONE})  # 加上这个参数就可以了
        a = json.dumps({"cmd":"join","channel":str(room),"nick":str('checker'),"password":str(random.randint(10000,99999))})
        check_ws.send(a)
        msg = check_ws.recv()
        print('[Log] Return:',msg)
        return msg
    def shoot(self, room):
        with open('key.cofing', 'r') as f:
            t = f.read()
        requests.get(labby1 + t + '/' + self.name)
    
knowRooms = ['programming','banana','chemistry','meta','lounge','math','physics','technology','games','game','23','sb23','you-channell']

if __name__ == '__main__':
    for i in len(knowRooms):
        exec('FOREST' + str(i) + ' = Gun(' + knowRooms[i] + ', ' + labby1 + ')')
        