# idena-ubuntu-tool
This is a tool for help people use ubuntu to do more thing in idena.
Main use tengxunyun API and idena API
# The goal to write it is just use ubuntu to achieve:
* build win vps to do idena test
* state idena account balance and state just like you are human or not
* exchange nodekey on win vps
you just state you address and nodekey in xlxs , all thing will do auto
# 技术支持
shell、cmd、python
# 文件目录
![image](https://github.com/weiliali/idena-ubuntu-tool/assets/46802173/c2670f43-e59e-49e4-b8a3-0405b21f3f8d)
## win端准备
### idena-start.bat
快捷命令：
按下【win+R】打开运行输入：【shell:Common Startup】
然后将想要开机启动的应用放置进去就好了。
### [安装openssh](https://urabas.com/2022/05/05/zai-windows-server-2012-r2-pei-zhi-openssh/)
安装 Chocolatey
Chocolatey 是 windows 下一款命令行包管理软件。
请先以管理员身份运行 PowerShell。 请运行以下命令安装 Chocolatey：
```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

使用 Chocolatey 安装 OpenSSH
OpenSSH 是一款用于远程登录的连接工具，它使用 SSH 协议。 它会加密客户端与服务器之间的所有流量，从而遏止窃听、连接劫持和其他攻击。 OpenSSH 在 2018 年秋季已添加至 Windows，并包含在 Windows 10 和 Windows Server 2019 中。

但是 Windows Server 2012 R2 并未包含 OpenSSH。请先以管理员身份运行 PowerShell，运行以下安装 OpenSSH 命令：

```
choco install openssh -y
```
启动并配置 OpenSSH 服务器

安装完成以后，打开C:\Program Files\OpenSSH-Win64目录运行install-sshd.ps1脚本安装 sshd 服务：


启动sshd服务
```
Start-Service sshd
Start-Service ssh-agent
```
开启开机自启
```
Set-Service -Name sshd -StartupType 'Automatic'
Set-Service -Name ssh-agent -StartupType 'Automatic'					
```

## linux端准备
1. 下载所有并解压缩到ubuntu中
2. 安装依赖源
```
apt-get update
apt install python3-pip -y
pip install --upgrade tencentcloud-sdk-python
pip install openpyxl
pip install paramiko
pip install time
```
## 文档格式
### idena-all.xlsx
address	nodekey	ip	state	balance	stake
![image](https://github.com/weiliali/idena-ubuntu-tool/assets/46802173/f9a60abc-8263-4515-9876-1975d1be1e19)


