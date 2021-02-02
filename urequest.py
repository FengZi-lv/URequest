# URequest v1.0
# 网络请求工具
# 一些功能还没有完全实现
# bug也可能很多
# 代码也非常乱
# 没有实现的函数会使用pass,以及v2.0实现
# 不喜自喷

# 使用本工具时不要使用类型fiddler的抓包工具,会导致本工具卡死,原因可能是https的事

# 最后,如果各位大佬有什么意见,email fengzi.lv@outlook.com

import requests
import os
import re
import ssl
from prettytable import PrettyTable


def Help(cmd):
    os.system("cls")
    h = PrettyTable()
    h.field_names = ["Code", "Usage"]
    h.add_row(["help", "获取关于URequest的信息帮助"])
    h.add_row([": [name] [content]", "在Header中添加参数, 其中[name]为参数名字, [content]为参数内容\n例如: 想要设置'User-Agent': 'Mozilla/5.0'\n使用$ 'User-Agent' 'Mozilla/5.0'即可"])
    h.add_row(["$ [name] [content]", "添加参数, 其中[name]为参数名字 , { way:设置GET/POST , cookies:设置Cookies , url:设置请求地址 , data:设置发送的数据 格式[name] [content] } , [content]为参数内容\n"])
    h.add_row(["send", "发送请求"])
    h.add_row(["clear", "重置所有参数"])
    h.add_row(["rq", "获取Request返回"])
    h.add_row(["rs", "获取Response返回"])
    h.add_row(["save [path]", "保存请求参数和响应结果, [path]为路径(包含文件名)"])
    h.add_row(["exit", "退出URequest"])
    h.add_row(["use [name]", "使用扩展, 其中[name]为扩展名, 查看扩展名请使用pluginhelp命令查看"])
    h.add_row(["get [name]", "安装扩展, 其中[name]为扩展名, 查看扩展名请使用pluginlist命令查看 (需要连接网络)"])
    print(h)
    print("\033[1;31m[注意] 所有参数均要使用['], 不可使用[\"]或没有使用引号\033[0m")


def Change(cmd):
    global request_header
    request_header[cmd[0].lower()] = cmd[1]
    pass

def Set(cmd):
    global request_cookie,request_data,request_way,Url
    if cmd[0]=="way":
        request_way=cmd[1]
    elif cmd[0]=="cookies":
        for line in cmd[1].split(';'):
            name, value = line.strip().split('=', 1)
            request_cookie[name] = value
    elif cmd[0]=="url":
        Url=cmd[1]
    elif cmd[0]=="data":
        request_data[cmd[1]]=cmd[2]



def Send(cmd):
    os.system("cls")
    print("In the processing . . .")
    ssl._create_default_https_context = ssl._create_unverified_context
    global request_header,request_way,request_cookie,Url,request_data,response_header,response_status,response_text,response_time
    print("In sending a request . . .")
    if request_way=="GET":
        try:
            r = requests.get(Url,headers=request_header,cookies=request_cookie,params=request_data,verify=True)
            r.encoding = 'utf-8'
            request_header=r.request.headers
            response_header=r.headers
            response_text=r.text
            response_status=r.status_code
            response_time=r.elapsed.total_seconds()
        except:
            print("ERROR: Fatal error!")
            return

    elif request_way=="POST":
        try:
            r = requests.post(Url,headers=request_header,cookies=request_cookie,data=request_data,verify=True)
            r.encoding = 'utf-8'
            response_header=r.headers
            response_status=r.status_code
            response_text=r.text
            response_time=r.elapsed.total_seconds()
        except:
            print("ERROR: Fatal error!")
            return
    print("Request successful, use [rs] to view the response")
    


def Clear(cmd):
    global Url,request_cookie,request_way,request_data,request_header,response_header,response_text,response_status,response_time,response_cookie
    Url = ""
    request_cookie = ""
    request_way = "GET"
    request_data={}
    request_header = {
        'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
    }
    response_header = {}
    response_text = ""
    response_status=000
    response_time=0
    response_cookie={}


def Save(cmd):
    pass

def Exit(cmd):
    if input("Are you sure you want to quit? [Y]")=="Y" :
        exit()


def USE(cmd):
    pass


def GET(cmd):
    pass


def PRINTLIST(p):  # 打印参数 help pluginhelp pluginlist
    return
    for r, d, files in os.walk('./list/'):
        for f in files:
            name = os.path.basename(os.path.join(r, f))
            if name == p:
                try:
                    f = open('D:\\readfiledemo.txt', 'r')
                    txt = f.read()

                except:
                    print("ERROR: Fatal error! It could be because of permissions")
                finally:
                    if f:
                        f.close()
                break



def Welcome():
    print("\033[1;31m[\t          \t ]\033[0m")
    print("\033[1;31m[\t[ URequest ]\t ]\033[0m")
    print("\033[1;31m[\t   v1.0   \t ]\033[0m")
    print("\033[1;33m[  Network Request Tools ]\033[0m")
    print("\033[1;34m[     [2021 BY FengZi]   ]\033[0m")
    print("\nSend [help] to get help")


def InfoRequest(c):
    os.system("cls")
    global request_header,Url,request_cookie,request_data
    b = PrettyTable()
    b.field_names = ["Name", "Content"]
    b.add_row(["URL", Url])
    b.add_row(["Request Way", request_way])
    b.add_row(["Cookie",request_cookie])
    b.add_row(["Data",request_data])
    h = PrettyTable()
    h.field_names = ["Name", "Content"]
    for key in request_header:
        h.add_row([key, request_header[key]])
    print("---------------Basic Information---------------")
    print(b)
    print("---------------Request Header---------------")
    print(h)


def InfoResponse(cmd):
    os.system("cls")
    global response_status,response_cookie,request_data,response_header,response_text
    b = PrettyTable()
    b.field_names = ["Name", "Content"]
    b.add_row(["StatusCode", response_status])
    b.add_row(["Cookie",response_cookie])
    b.add_row(["Time",request_data])
    r = PrettyTable()
    r.field_names = ["Name", "Content"]
    for key in response_header:
        r.add_row([key, response_header[key]])
    print("\033[1;31m\t\t[ URequest ]\t\t\033[0m")
    print("---------------Basic Information---------------")
    print(b)
    print("---------------Response Header---------------")
    print(r)
    print("---------------Response Text---------------")
    if(cmd!=["all"]):
        if len(response_text)>300:
            print("[*]The response is over 300 bytes, please use [rs 'all'] if you want to view them all\n")
            print(response_text[0:300])
            return
    print(response_text)

def ParseCMD(cmd):
    re_return = re.search(
        r"(?P<cmd_name>[^ |\t|\r]*)(?P<cmd_parm>((( |\t|\r)*)(([^ |\t|\r])*))*)", cmd, re.I)
    try:
        _parm = re_return.group("cmd_parm").split("'")
        parm = []
        for key in range(len(_parm)):
            if(key % 2 != 0):
                parm.append(_parm[key])
        return re_return.group("cmd_name"), parm
    except:
        return re_return.group("cmd_name"), False


Url = ""  # url
request_cookie = {}  # cookie
request_way = "GET"  # GET or POST
request_data={}
request_header = {
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
}  # header
cmd_list = {
    "help": Help,
    ":": Change,
    "$":Set,
    "rq":InfoRequest,
    "rs":InfoResponse,
    "send": Send,
    "clear": Clear,
    "save":Save,
    "exit":Exit
}
response_header = {}
response_text = ""
response_status=000
response_time=0
response_cookie={}
Welcome()
while True:
    cmd, parm = ParseCMD(input('Urequest>'))
    func = cmd_list.get(cmd, 0)
    if func == 0:
        print("\033[1;31m[Error]\033[0m The command could not be found")
    else:
        func(parm)
