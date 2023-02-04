from distutils.command import check
import websocket
import requests
import json
import time
import random
import socks
import ssl
import uuid
from threading import Thread
names = []
threads = []
proxies = []

cname = ''
with open('server.txt','r') as f:
    cname = f.read()


def sendd(text):
    return json.dumps({"cmd":"chat","text":str(text)})

class main:
    def __init__(self,room,name,pas):
        self.room = room
        self.name = name
        self.pas = pas
        
    def on_message(self,ws,message):
        print('收到消息：',message)
        msg = json.loads(message)
        if msg['cmd'] == 'chat' and '~kick' in msg['text']:
            if (self.name in msg['text']):
                while True:
                    try:
                        rand = random.randint(3,20)
                        uid = str(uuid.uuid4()).replace('-', '')[0:rand]
                        check_lock_msg = json.loads(check_lockroom(cname,uid,uid))
                        
                        if (check_lock_msg['cmd'] == 'onlineSet'):
                            break
                        time.sleep(10)
                    except:
                        time.sleep(10)
                ws.send(sendd('不要尝试踢USBot，除非你锁房，否则他们还会回来的。不过需要注意的是，只要你一解锁房间，他们也会第一时间回来的。祝你有个美好的一天！（小提示：快去叫管理来这里开验证码吧，我需要一些验证码来训练模型）'))
                rand = random.randint(3,20)
                uid = str(uuid.uuid4()).replace('-', '')[0:rand]
                new_thread = Thread(target=run,args=(cname,uid,uid,proxies[random.randint(0,len(proxies)-1)]))
                threads.append(new_thread)
                print(threads[-1])
                threads[-1].start()
                proxies.pop(0)
                ws.close()
                return


    def on_error(self,ws,error):
        print('错误',error)
    

    def on_close(self,ws):
        print('断开')
    

    def on_open(self,ws):

        # 连接上服务器了则调用
        a = json.dumps({"cmd":"join","channel":str(self.room),"nick":str(self.name),"password":str(self.pas)})
        hi = random.choice(["hello","hi","hey","hi yo","hey yo"])
        ws.send(a)
        names.append(str(self.name))

def run(room,name,pas,proxy):
    var_main = main(room = room,name = name,pas = pas)
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp('wss://hack.chat/chat-ws',on_message = var_main.on_message,on_error = var_main.on_error,on_close = var_main.on_close)
    ws.on_open = var_main.on_open 
    ws.run_forever(proxy_type='http',http_proxy_host=proxy.split(':')[0], http_proxy_port=int(proxy.split(':')[1]),sslopt={"cert_reqs": ssl.CERT_NONE})

def check_lockroom(room,name,pas):
    check_ws = websocket.create_connection('wss://hack.chat/chat-ws',sslopt={"cert_reqs":ssl.CERT_NONE})  # 加上这个参数就可以了
    a = json.dumps({"cmd":"join","channel":str(room),"nick":str(name),"password":str(pas)})
    check_ws.send(a)
    msg = check_ws.recv()
    print('检查返回值：',msg)
    return msg

if __name__ == "__main__":
    while True:
        try:
            rand = random.randint(3,20)
            uid = str(uuid.uuid4()).replace('-', '')[0:rand]
            check_lock_msg = json.loads(check_lockroom(cname,uid,uid))
            if (check_lock_msg['cmd'] == 'onlineSet'):
                break
        except:
            pass
        time.sleep(10)

    with open("proxies.txt","r") as f:
        proxies=f.read().split("\n")
    print(names,proxies)
    for l in proxies:
        rand = random.randint(3,20)
        uid = str(uuid.uuid4()).replace('-', '')[0:rand]
        threads.append(Thread(target=run,args=(cname,uid,uid,proxies[random.randint(0,len(proxies)-1)])))
    print(threads)
    for l in threads:
        l.start()
        time.sleep(2)
        print(names)
        if len(names) == 2:
            print('breaked')
            break
    print(names)