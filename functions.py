# -*- coding: UTF-8 -*-  

import os
import time

from master import main as restart
from termcolor import *

def install():
    print (colored('输入help以查询支持安装的软件',"yellow"))
    AZXX = input(colored('请写出您要安装的程序：',"yellow"))
    if AZXX == "help":
        print (colored('可安装的软件列表:',"blue"))
        print (colored('          名称          支持状态',"blue"))
        print (colored('          网易云音乐          未知',"blue"))
        print (colored('          PINYIN          OK',"blue"))
        print (colored('          补全系统          ok',"blue"))
        print (colored('          vm-tools          ok',"blue"))
        print (colored('          QQirc          ok',"blue"))
        print (colored('          mdk4          ok',"blue"))
        print (colored('          bettercap(v1.6)          ok',"blue"))
        print (colored('          powershell          (Only in Kali-linux)',"blue"))
        AZXX = input(colored('请写出您要安装的程序：',"yellow"))
    if AZXX ==  "网易云音乐":
        os.system('apt-get -y install gdebi')
        os.system('wget -P /tmp  http://d1.music.126.net/dmusic/netease-cloud-music_1.1.0_amd64_ubuntu.deb')
        os.system('gdebi /tmp/netease-cloud-music_1.1.0_amd64_ubuntu.deb')
        os.system('reset')
        print (colored("操作完成，3秒后重启脚本","blue"))
        time.sleep(3)
        restart()
    if AZXX == "输入法":
        os.system('apt-get -y install fcitx-googlepinyin')
        os.system('reset')
        print (colored("操作完成，3秒后重启脚本","blue"))
        time.sleep(3)
        restart()
    if AZXX == "PINYIN":
        os.system('apt-get -y install fcitx-googlepinyin')
        os.system('reset')
        print (colored("操作完成，3秒后重启脚本","blue"))
        time.sleep(3)
        restart()
    if AZXX == "补全系统":
        os.system('apt-get -y install kali-linux-all')
        print (colored("操作完成，3秒后重启脚本","blue"))
        os.system('reset')
        time.sleep(3)
        restart()
    if AZXX == "vm-tools":
        os.system('apt-get update')
        os.system('apt-get -y install open-vm-tools-desktop fuse')
        os.system('reset')
        print (colored("操作完成，3秒后重启脚本","blue"))
        time.sleep(3)
        restart()
    if AZXX == "QQirc":
        os.system("reset")
        print (colored("第一阶段:安装依赖!","red"))
        os.system("apt-get install perl  -y")
        os.system("apt-get install libssl-dev -y")
        os.system("apt-get install cpanminus -y")
        os.system("reset")
        print (colored("第二阶段:安装ircQQ","red"))
        os.system("cpanm Mojo::Webqq")
        os.system("cpanm -v Mojo::IRC::Server::Chinese")
        os.system("reset")
        print (colored("第三阶段:配置并运行!","red"))
        os.system("touch /home/qq.pl")
        irc = open("/home/qq.pl","a")
        irc.write("""#!/usr/bin/env perl
use Mojo::Webqq;
my ($host,$port,$post_api);
$host = "0.0.0.0"; #发送消息接口监听地址，没有特殊需要请不要修改
$port = 5000;      #发送消息接口监听端口，修改为自己希望监听的端口
my $client = Mojo::Webqq->new();
$client->load("ShowMsg");
$client->load("Openqq",data=>{listen=>[{host=>$host,port=>$port}], post_api=>$post_api});
$client->run();""")
        irc.close()
        print (colored("配置完成!","red"))
        os.system("echo 'perl /home/qq.pl' > ~/QQirc.sh")
        os.system("perl /home/qq.pl")
    if  AZXX == "mdk4":
        os.system("reset")
        print (colored("第一阶段:安装依赖!","red"))
        os.system("apt-get -y install g++ git  libnl-3-dev libnl-genl-3-dev pkg-config libpcap-dev build-essential")
        print (colored("第二阶段:CLONE项目","red"))
        os.system('git clone https://github.com/aircrack-ng/mdk4.git "/home/mdk4"')
        print (colored("第二阶段:编译","red"))
        os.system('echo "cd /home/mdk4\nmake\nmake install" > /tmp/LS.sh')
        os.system("sh /tmp/LS.sh")
        os.system("rm /tmp/LS.sh")
        print (colored("操作完成，3秒后重启脚本","blue"))
        time.sleep(3)
        restart()
    if AZXX == "bettercap":
        os.system("bash ./scrips/install_old_bettercap.sh")
        print (colored("操作完成，3秒后重启脚本 开启命令:bettercapj","blue"))
        time.sleep(3)
        restart()
    if AZXX == "powershell":
        DXCXX = input(colored("多线程下载(Y,N):"))
        if DXCXX == "Y":
            os.system('axel -o /tmp -n 25 "https://github.com/PowerShell/PowerShell/releases/download/v6.0.2/powershell_6.0.2-1.debian.9_amd64.deb"')
            os.system("dpkg -i /tmp/powershell_6.0.2-1.debian.9_amd64.deb")
            os.system("apt-get install -f -y")
            inst = open("/bin/powershell","w")
            inst.write("""#!/usr/bin/env bash
exec xterm -e pwsh &""")
            inst.close()
            print (colored("操作完成，3秒后重启脚本 开启命令:powershell","blue"))
            time.sleep(3)
            restart()
        if DXCXX == "N":
            os.system('wget -P /tmp "https://github.com/PowerShell/PowerShell/releases/download/v6.0.2/powershell_6.0.2-1.debian.9_amd64.deb"')
            os.system("dpkg -i /tmp/powershell_6.0.2-1.debian.9_amd64.deb")
            os.system("apt-get install -f -y")
            os.system("touch /bin/powershell")
            os.system("chmod 777 /bin/powershell")
            inst = open("/bin/powershell","w")
            inst.write("""#!/usr/bin/env bash
exec xterm -e pwsh &""")
            inst.close()
            print (colored("操作完成，3秒后重启脚本 开启命令:powershell","blue"))
            time.sleep(3)
            restart()
def deb():
    print (colored('输入help以查询支持的软件源',"yellow"))
    debX = input(colored('请写出您要变为的软件源：',"yellow"))
    if debX == "help":
        print (colored('可使用的软件列表:',"blue"))
        print (colored('          名称          支持状态',"blue"))
        print (colored('          中科大          ok',"blue"))
        print (colored('          官方源          OK',"blue"))
        print (colored('          手动(高级)          OK',"blue"))
        debX = input(colored('请写出您要变为的软件源：',"yellow"))
    if debX == "中科大":
        os.system('rm -rf /etc/apt/sources.list')
        os.system('echo "deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib\ndeb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib" >/etc/apt/sources.list')
        os.system('apt-get update --fix-missing')
        os.system('reset')
        print (colored("操作完成，3秒后重启脚本","blue"))
        time.sleep(3)
        restart()
    if debX == "官方源":
        os.system('rm -rf /etc/apt/sources.list')
        os.system('echo "deb http://http.kali.org/kali kali-rolling main non-free contrib\ndeb-src http://http.kali.org/kali kali-rolling main non-free contrib" >/etc/apt/sources.list')
        os.system('apt-get update --fix-missing')
        os.system('reset')
        print (colored("操作完成，3秒后重启脚本","blue"))
        time.sleep(3)
        restart()
    if debX == "手动":
        os.system("reset")
        print (colored(r'本模块作者:{"text":"josn"}',"red"))
        DAA = input(colored("help查看帮助,请选择模式:","yellow"))
        if DAA == "help":
            print (colored('                模式名称     介绍',"red"))
            print (colored('                w     覆盖之前的数据(危险)',"red"))
            print (colored('                a     追加写入(推荐)',"red"))
            DAA = input(colored("请选择模式:","yellow"))
        if DAA == "w":
            DA = open("/etc/apt/sources.list","w") 
            XR = input(colored(r"写入\n即可换行,写入源地址:","yellow"))
            DA.write(XR)
            DA.close
            print (colored("操作完成，3秒后重启脚本","blue"))
            time.sleep(3)
            restart()
        if DAA == "a":
            DA = open("/etc/apt/sources.list","a")
            XR = input(colored(r"写入\n即可换行,写入源地址:","yellow"))
            DA.write(XR)
            DA.close()
            print (colored("操作完成，3秒后重启脚本","blue"))
            time.sleep(3)
            restart()
def gpg():
    os.system('wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add')
    os.system('apt-get update')
    os.system('reset')
    print (colored("操作完成，3秒后重启脚本","blue"))
    time.sleep(3)
    restart()
def  download():
    XC = input(colored("输入要使用的线程数:","yellow"))
    LJ = input(colored("输入要下载的文件链接:","yellow"))
    print (colored("初始化中Loding...","blue"))
    os.system("apt-get -y install axel")
    print (colored("初始化完成","blue"))
    os.system("axel -o /root/ -n"+ XC +' '+'\"'+LJ+'\"')
    os.system('reset')
    print (colored("文件存放路径：/root/","blue"))
    print (colored("操作完成，3秒后重启脚本","blue"))
    time.sleep(3)
    restart()
def PATH():
    print (colored('输入help以查询支持的一键配置环境的语言',"yellow"))
    YY = input(colored("输入要安装的语言环境:","yellow"))
    if YY == "help":
        print (colored('可使用的语言列表:',"blue"))
        print (colored('          名称          支持状态',"blue"))
        print (colored('          GO          ok',"blue"))
        YY = input(colored("输入要安装的语言环境:","yellow"))
    if YY == "GO":
        os.system("wget -P /root https://studygolang.com/dl/golang/go1.10.linux-amd64.tar.gz")
        os.system("tar -xf /root/go1.10.linux-amd64.tar.gz -C /root/")
        os.system('echo "export PATH=$PATH:/root/go/bin" >> /root/.bashrc')
        print (colored("操作完成，3秒后重启脚本","blue"))
        print (colored("用户root的GO语言环境部署完成","blue"))
        time.sleep(3)
        restart()
