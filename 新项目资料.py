https://github.com/MPOS/php-mpos

https://rahulmanuwas.gitbooks.io/mpos-nomp/content/

开源项目上线后地址:
https://beam.suprnova.cc/

体验地址:
https://www.bfcpool.com/account/profit.html
账户: 54303771@qq.com
密码: w123456
抹茶交易所:
https://www.mxc.co/trade/easy#MX_USDT

项目正式上线地址:
https://www.bfcpool.com/

数据库没有密码:
登录账号是mysql
直接mysql -umysql就可以进去.

ubuntu18.04卸载mysql:
https://blog.csdn.net/iehadoop/article/details/82961264

ubuntu18安装mysql教程:
https://blog.csdn.net/dmedaa/article/details/89965556

您新购买云服务器:
154.221.25.18
账号：root
密码：3vyQ725M

ubuntu18源码安装mysql5.6:
https://blog.csdn.net/kevinhades/article/details/88692551


https://blog.csdn.net/kevinhades/article/details/88692551

/usr/local/mysql/scripts/mysql_install_db --user=mysql --basedir=/usr/local/mysql --datadir=/data/mysqldata


python2.7问题记录:
https://blog.csdn.net/wangjiegege/article/details/77478870

navicat导入sql文件:
https://www.cnblogs.com/chenlimei/p/10375676.html

比特币抵押质押解释:
https://zhuanlan.zhihu.com/p/52392921

python实现的区块链:
https://github.com/Carlos-Zen/blockchain-python/blob/master/README_zh.md

申请了新的云主机之后,通常会遇到下面的问题:
ubuntu新项目:
问题:MySQL只有information_schema,test两个数据库
https://www.cnblogs.com/xbq8080/p/6654672.html

http://154.221.25.18:8000/pledge

后面安装mysql就用这个版本:
Server version: 5.7.25 MySQL Community Server

CV:就是简历的意思

Python3 sqlacodegen 根据已有数据库生成 ORM 使用的 model.py
https://www.cnblogs.com/yuqilin/p/10743386.html

自定义设计orm:
https://blog.csdn.net/u013181595/article/details/77036446?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~first_rank_v2~rank_v25-3-77036446.nonecase

https://beam.suprnova.cc/index.php

获取算力:
https://www.bfcpool.cn/pool/api/getHashrate.html?puid=2483
https://www.bfcpool.cn/pool/api/getHashrate.html?puid=1452

返回值:
{
  "code": 1,
  "msg": "ok",
  "data": {
    "now_hashrate": "0.000 H/s",   1小时实时算力
    "hashrate24": "0.000 KH/s"     24小时平均算力
  }
}

获取worker个数:
https://www.bfcpool.cn/pool/api/getWorkerNum.html?puid=2483
https://www.bfcpool.cn/pool/api/getWorkerNum.html?puid=1452   总共的
单页的:
https://www.bfcpool.cn/pool/api/getworker.html?type=0&page=1&puid=1452
返回值:
{
  "code": 1,
  "msg": "ok",
  "data": {
    "total": 0,         所有
    "active": 0,        活跃
    "offline": 0        不活跃
  }
}

获取收益:
https://www.bfcpool.cn/pool/api/getEarning.html?puid=2483
https://www.bfcpool.cn/pool/api/getEarning.html?puid=1452
返回值:
{
  "code": 1,
  "msg": "ok",
  "data": {
    "now": "0.00000000",
    "yesterday": "0.00000000",
    "blance": "0.00000000"
  }
}

矿机管理:
https://www.bfcpool.cn/pool/api/getworker.html?type=0&page=1&puid=2483
返回值:
{
  "code": 1,
  "msg": "ok",
  "data": {
    "total": 0,
    "active": 0,
    "offline": 0,
    "data": []
  }
}

收益记录:
https://www.bfcpool.cn/pool/api2/profit_day.html?token=qNTPy9Byw5eampyaZ5qRmmSbZ5GbmpRoZJzHY51dbGllmZiWxWyZa8mbXNKpoMifYmxtl4vVmaCcdZdocmZmZ2eXmZo%3D&page=1
返回值:
{
  "code": 1,
  "msg": "ok",
  "data": {
    "data": [
      {
        "time": "2020-04-23",
        "profit": "1.77457761",      满抵押收益
        "suanli": "622.222 H/s",     算力
        "pay_status": 1,			 结算状态
        "pay_time": "2020-04-24 09:59:38",  结算时间
        "pay_token": "3dd349d30abc317226d00d02c26f5c5bc255a7742e4954f500194899835b2219",
        "reality_coin": "1.77457761",  实际收益
        "pay_token2": "3dd3...2219"
      },
      {
        "time": "2020-04-22",
        "profit": "57.16023536",
        "suanli": "16.238 KH/s",
        "pay_status": 1,
        "pay_time": "2020-04-23 10:24:53",
        "pay_token": "768c0de1d92ccee14f8e4189c13d33d63a022eb5f24473ea3f11d98333d3c537",
        "reality_coin": "57.16023536",
        "pay_token2": "768c...c537"
      },
      {
        "time": "2020-04-21",
        "profit": "43.15288686",
        "suanli": "8.969 KH/s",
        "pay_status": 1,
        "pay_time": "2020-04-22 10:10:13",
        "pay_token": "9072882766970176ed9eb901ba8fa8af38ccd79d7e97ea213823772a441ccbe0",
        "reality_coin": "43.15288686",
        "pay_token2": "9072...cbe0"
      },
      {
        "time": "2020-04-16",
        "profit": "22.10141332",
        "suanli": "4.814 KH/s",
        "pay_status": 1,
        "pay_time": "2020-04-17 09:42:50",
        "pay_token": "6431903bd0da42120ca8bbc1024b2a099fa51fa8d109f571f3c3e4354ac80c2e",
        "reality_coin": "22.10141332",
        "pay_token2": "6431...0c2e"
      },
      {
        "time": "2020-04-14",
        "profit": "3.30303107",
        "suanli": "2.274 KH/s",
        "pay_status": 1,
        "pay_time": "2020-04-15 09:41:50",
        "pay_token": "eecd96aec61d8a1ebf6cc12c3148ad4431409c6f8d3f4397df3b713d1e4c2fb7",
        "reality_coin": "3.30303107",
        "pay_token2": "eecd...2fb7"
      },
      {
        "time": "2020-04-13",
        "profit": "22.81949697",
        "suanli": "15.491 KH/s",
        "pay_status": 1,
        "pay_time": "2020-04-14 09:38:04",
        "pay_token": "a03c6cf24b8361cc2c552adadff4122e58dee19a47c0496748db229f9e4bb570",
        "reality_coin": "22.81949697",
        "pay_token2": "a03c...b570"
      },
      {
        "time": "2020-04-12",
        "profit": "20.39941481",
        "suanli": "14.498 KH/s",
        "pay_status": 1,
        "pay_time": "2020-04-13 09:36:59",
        "pay_token": "0bac18b2bfdb18271ff85649aff8fdfbd0d81484bfc6c58d35a9d0347d452612",
        "reality_coin": "20.39941481",
        "pay_token2": "0bac...2612"
      },
      {
        "time": "2020-04-11",
        "profit": "20.19307182",
        "suanli": "14.590 KH/s",
        "pay_status": 1,
        "pay_time": "2020-04-12 09:39:13",
        "pay_token": "bdb5afb57a8610f6679ae439becd160d9567897da9ba61c59cc9ab8110933f35",
        "reality_coin": "20.19307182",
        "pay_token2": "bdb5...3f35"
      },
      {
        "time": "2020-04-10",
        "profit": "22.00904374",
        "suanli": "14.585 KH/s",
        "pay_status": 1,
        "pay_time": "2020-04-11 10:47:10",
        "pay_token": "b4fd37c7b8821e4cb6cc9b8b8240f11664836c0280be1a67ffeef5b499f05853",
        "reality_coin": "22.00904374",
        "pay_token2": "b4fd...5853"
      },
      {
        "time": "2020-04-09",
        "profit": "22.26744836",
        "suanli": "14.506 KH/s",
        "pay_status": 1,
        "pay_time": "2020-04-10 09:44:39",
        "pay_token": "085f5a600fd6d3759e5fac2ef23dff0aafb8126e9922306f56957f0612f5267d",
        "reality_coin": "22.26744836",
        "pay_token2": "085f...267d"
      }
    ],
    "total": 28
  }
}

https://beam.suprnova.cc/index.php?page=statistics&action=pool

交易地址:
http://167.172.144.49/


API Calls
Return data from coind

getdifficulty
Returns the current difficulty.
167.172,144,49/api/getdifficulty

getconnectioncount
Returns the number of connections the block explorer has to other nodes.
167.172,144,49/api/getconnectioncount

getblockcount
Returns the current block index.
167.172,144,49/api/getblockcount

getblockhash [index]
Returns the hash of the block at ; index 0 is the genesis block.
167.172,144,49/api/getblockhash?index=1337

getblock [hash]
Returns information about the block with the given hash.
167.172,144,49/api/getblock?hash=1733320247b15ca2262be646397d1ffd6be953fa638ebb8f5dcbb4c2b91b34f1

getrawtransaction [txid] [decrypt]
Returns raw transaction representation for given transaction id. decrypt can be set to 0(false) or 1(true).
167.172,144,49/api/getrawtransaction?txid=f270cd3813254c9922a2e222a56ba745842d9112223a1394062e460b33d27b7e&decrypt=0
167.172,144,49/api/getrawtransaction?txid=f270cd3813254c9922a2e222a56ba745842d9112223a1394062e460b33d27b7e&decrypt=1

getnetworkhashps
Returns the current network hashrate. (hash/s)
167.172,144,49/api/getnetworkhashps

Extended API
Return data from local indexes

getmoneysupply
Returns current money supply
167.172,144,49/ext/getmoneysupply

getdistribution
Returns wealth distribution stats
167.172,144,49/ext/getdistribution

getaddress (/ext/getaddress/hash)
Returns information for given address
167.172,144,49/ext/getaddress/RBiXWscC63Jdn1GfDtRj8hgv4Q6Zppvpwb

gettx (/ext/gettx/hash)
Returns information for given tx hash
167.172,144,49/ext/gettx/f270cd3813254c9922a2e222a56ba745842d9112223a1394062e460b33d27b7e

getbalance (/ext/getbalance/hash)
Returns current balance of given address
167.172,144,49/ext/getbalance/RBiXWscC63Jdn1GfDtRj8hgv4Q6Zppvpwb

getlasttxsajax (/ext/getlasttxsajax/min)
Returns last transactions greater than [min]
Note: returned values are in satoshis
167.172,144,49/ext/getlasttxsajax/100

Linking (GET)
Linking to the block explorer

transaction (/tx/txid)
167.172,144,49/tx/f270cd3813254c9922a2e222a56ba745842d9112223a1394062e460b33d27b7e

block (/block/hash)
167.172,144,49/block/1733320247b15ca2262be646397d1ffd6be953fa638ebb8f5dcbb4c2b91b34f1

address (/address/hash)
167.172,144,49/address/RBiXWscC63Jdn1GfDtRj8hgv4Q6Zppvpwb

qrcode (/qr/hash)
167.172,144,49/qr/RBiXWscC63Jdn1GfDtRj8hgv4Q6Zppvpwb

https://github.com/topics/mpos-api