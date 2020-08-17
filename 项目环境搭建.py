# 项目环境搭建:
# 注意:不能偷懒啊,手贱使用了 git push origin xxx -f 
# 应该合理使用 git commit --amend 不应该每次都这么使用


步骤:

1、先更新apt源:
sudo apt-get update
sudo apt-get upgrade

2、安装依赖包：
sudo apt-get install sendmail libqtgui4 qt4-qmake libqt4-dev build-essential libboost-dev libboost-system-dev libboost-filesystem-dev libssl-dev libdb++-dev git libboost-all-dev libcurl4-openssl-dev libdb5.1-dev libdb5.1++-dev mysql-server python-twisted python-mysqldb python-dev python-setuptools python-memcache python-simplejson memcached php5-memcached php5-mysqlnd php5-curl php5-json libapache2-mod-php5


可能遇到的问题:
依赖包无法找到或者无法安装:
E: Unable to locate package liqtgui4  注意包的名字是否拼写错误
解决办法:
执行 vim /etc/apt/sources.list 文件,在最后一行将下面的地址复制进去:

deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse


# 彻底解决的办法:
https://blog.csdn.net/MENGHUANBEIKE/article/details/78052317?locationNum=8&fps=1

linux的版本依赖问题很令人纠结，不过我们可以通过使用aptitude软件包管理器来解决这个依赖问题，aptitude是可以选择合适的版本与匹配软件安装。

首先安装aptitude工具:
sudo apt-get install aptitude

再利用aptitude来安装libssl-dev:
sudo aptitude install libssl-dev

apt-get 误删之后重现安装:
https://jingyan.baidu.com/article/5225f26bbab600e6fa0908bb.html



1.指定端口

ssh -p 端口 用户@ip地址

例子
ssh -p 29565 root@182.168.1.58

pkill -kill -t pts/0

遇到的钱包数据库初始化失败的问题:
https://www.itdaan.com/tw/608b50c1a172