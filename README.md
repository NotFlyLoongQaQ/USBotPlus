# USBot++ You SB(Bitch) Bot

[![](https://img.shields.io/badge/Python-3.4.4+-red.svg)]() [![](https://img.shields.io/badge/Python-Flask-blue.svg)]() [![](https://img.shields.io/badge/Bomb-USBot-blue.svg)]()
该Readme将会最详细的讲解该项目的安装方法.

## 服务端

Dark-Forest 支持服务器集群，但是这可能需要您修改init.py。

我们将会先讲述单服务器的安装方法。

### 单服务器安装Dark-Forest

如果您是Linux服务器，请连接ssh，如果您使用Windows服务器，请使用rdp连接到服务器。

进入终端，对该仓库进行克隆。

```bash
git clone https://github.com/NotFlyLoongQaQ/Dark-Forest-AtHackchat
```

然后切换到serve目录并启动服务：

```bash
cd serve
python3 httpserve.py
```

完成!

### 多服务器安装Dark-Forest

首先，您需要在您要部署DarkForest的服务器上运行单服务器安装的方法，随后您需要修改init.py。

请将目光落在init.py的第十一行：

```python
labby1 = 'http://您的usbot节点/api/auth/labby1/'
```

在后面添加代码：

```python
labby2 = 'http://您的usbot节点/api/auth/labby1/'
```

然后，在main模块中，请找到exec，并将那段代码修改成类似这样：

```python
if __name__ == '__main__':
    for i in len(knowRooms):
	a    = random.randint(1,您的服务器数)
	name = 'labby' + str(a)
        exec('FOREST' + str(i) + ' = Gun(' + knowRooms[i] + ', ' + name + ')')
  
```

为此您可能需要导入random模块。

## 客户端

首先，您需要在服务器的serve目录中创建token.txt，这是您与服务端的通讯密钥，请务必妥善保存。

将密钥复制到本地并另存为key.cofing，然后运行init.py，感谢您为构建黑暗森林做出的努力！



# USBot++ You SB(Bitch) Bot

[![](https://img.shields.io/badge/Python-3.4.4+-red.svg)]()[![](https://img.shields.io/badge/Python-Flask-blue.svg)]()[![](https://img.shields.io/badge/Bomb-USBot-blue.svg)]()
This Readme will explain how to install the project in the most detail.

## Server

Dark-Forest supports server clustering, but this may require you to modify init.py.

We'll start with a single server installation.

### Single server install Dark-Forest

If you are a Linux server, connect to ssh, if you are using a Windows server, connect to the server using rdp.

Enter the terminal and clone the warehouse.

```bash
git clone https://github.com/NotFlyLoongQaQ/Dark-Forest-AtHackchat
```

Then switch to the serve directory and start the service:

```bash
cd serve
python3 httpserve.py
```

Finished!

### Multi-server install Dark-Forest

First, you need to run the single-server installation method on the server where you want to deploy DarkForest, and then you need to modify init.py.

Focus on line 11 of init.py:

```python
labby1 = 'http://your usbot node /api/auth/labby1/'
```

Add the code after:

```python
labby2 = 'http://your usbot node /api/auth/labby1/'
```

Then, in the main module, find exec and change that code to something like this:

```python
if __name__ == '__main__':
for i in len(knowRooms):
a = random.randint(1, the number of your servers)
name = 'labby' + str(a)
exec('FOREST' + str(i) + ' = Gun(' + knowRooms[i] + ', ' + name + ')')

```

You may need to import the random module for this purpose.

## Client

First, you need to create token.txt in the serve directory of the server, which is the key for communication between you and the server. Keep it properly.

Copy the key locally and save it as key.cofing, then run init.py and thank you for your efforts in building the Dark Forest!

Youdao Neural Network Translation (YNMT)
