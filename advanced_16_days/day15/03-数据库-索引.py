print('------')
"""
索引:计算机中非常著名的概念,都是为了提高查找的效率
  
列表:顺序查找,一个一个找,很慢.  <下标-索引>
字典:通过key查找值value    <key其实可以称之为索引>

计算机中的二八原则:       8:2 百分之八十是读操作,百分之二十是写操作.

表索引也是数据库中的一项单独的文件:.idx   index索引数据 存的是表数据位置信息

表数据的位置信息  扇区号

索引也是需要排序的

意义:快速的定位到表数据所在位置 --提高数据的查找速率.<因为是在有序的索引中快速定位到具体位置>

索引无法提高数据的插入,更新,删除效率,因为会导致索引的重新排序<这样的资源开销也很大>

让数据变得有序---索引. 

"""
# --------------------------------------查看索引--------------------------------------->
"""查看表中已有的索引:
show index from 表;

mysql> show index from goods;
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| goods |          0 | PRIMARY  |            1 | id          | A         |          19 | NULL     | NULL   |      | BTREE      |         |               |
| goods |          1 | brand_id |            1 | brand_id    | A         |           8 | NULL     | NULL   |      | BTREE      |         |               |
| goods |          1 | cate_id  |            1 | cate_id     | A         |           6 | NULL     | NULL   |      | BTREE      |         |               |
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
3 rows in set

注意:主键默认会有一个索引
"""
# -----------------------------------创建索引------------------------------------------->
"""
创建索引:
# create index 索引字段 on 表名(字段名称(字段类型是字符串(长度)))
# create index i_t on test_index(title(10));
注意:如果字段是字符串类型的数据就加长度,如果是其他类型不用写长度.

由于索引本身也是数据文件,所以索引不要太多

查看:
show index from 表名;
--------------------------删除索引---------------------------------->
删除索引:
drop index 索引名称 on 表名;

set profiling=1;  设置配置文件的模式为打开
show profiles;查看配置文件

示例:验证索引的查询速度是否更快
mysql> show index from test_index;
Empty set

mysql> set profiling=1;
Query OK, 0 rows affected

mysql> select * from test_index where title='ha-99999';   --> 花费时间 0.047921
+----------+
| title    |
+----------+
| ha-99999 |
+----------+
1 row in set

mysql> show  profiles;  --->查看执行语句持续的时间   Duration:持续.
+----------+----------+-------------------------------------------------+
| Query_ID | Duration | Query                                           |
+----------+----------+-------------------------------------------------+
|        1 | 0.047921 | select * from test_index where title='ha-99999' |
+----------+----------+-------------------------------------------------+
1 row in set

mysql> create index i_title on test_index(title(10));    -->创建索引
Query OK, 0 rows affected
Records: 0  Duplicates: 0  Warnings: 0

mysql> select * from test_index where title='ha-99999';   -->花费时间 0.000448
+----------+
| title    |
+----------+
| ha-99999 |
+----------+
1 row in set

mysql> show profiles;
+----------+------------+-------------------------------------------------+
| Query_ID | Duration   | Query                                           |
+----------+------------+-------------------------------------------------+
|        1 |   0.047921 | select * from test_index where title='ha-99999' |
|        2 | 0.24268925 | create index i_title on test_index(title(10))   |
|        3 |   0.000448 | select * from test_index where title='ha-99999' |
+----------+------------+-------------------------------------------------+
3 rows in set

-----------------------------分割线:授权---------------------------------------
\G:将sql语句中的结果   每一条记录<即一行>的所有字段信息用一块<也可以当做一行>显示,形如下面这种:

mysql> select * from jd.goods\G;
*************************** 1. row ***************************
        id: 1
      name: LV包治百病
   cate_id: 5
  brand_id: 2
     price: 3399.000
   is_show: 
is_saleoff:
*************************** 2. row ***************************
        id: 2
      name: 古奇
   cate_id: 5
  brand_id: 7
     price: 4999.000
   is_show: 
is_saleoff:

----------------------------查看:---------------------------------->
show slave status\G;
查看用户信息:
select host,user,authentication_string from user;
说明:
1.>host:表示允许访问的主机
2.>user:用户名
3.>authentication_string:密码,是加密后的值
+-----------+------------------+-------------------------------------------+
| host      | user             | authentication_string                     |
+-----------+------------------+-------------------------------------------+
| localhost | root             | *E74858DB86EBA20BC33D0AECAE8A8108C56B17FA |
| localhost | mysql.sys        | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
| localhost | debian-sys-maint | *EFED9C764966EDB33BB7318E1CBD122C0DFE4827 |
| %         | laoli            | *84AAC12F54AB666ECFC2A83C676908C8BBC381B1 |
+-----------+------------------+-------------------------------------------+
%  --> 表示在任意主机都可以使用
修改密码:
update user set authentication_string=password('新密码') where user='root';


-----------------------查看授权------------------------------------->
查看用户权限:
show grants for '用户名'@'主机名';
主机名:%代表任意主机 代表用户只能在哪里使用
show grants for 'root'@'localhost';
+---------------------------------------------------------------------+
| Grants for root@localhost                                           |
+---------------------------------------------------------------------+
| GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION |
| GRANT PROXY ON ''@'' TO 'root'@'localhost' WITH GRANT OPTION        |
+---------------------------------------------------------------------+
2 rows in set (0.00 sec)
----------------------------示例------------------------------->
show grants for 'laoli'@'%';
+------------------------------------------------------+
| Grants for laoli@%                                   |
+------------------------------------------------------+
| GRANT USAGE ON *.* TO 'laoli'@'%'                    |
| GRANT ALL PRIVILEGES ON `jing_dong`.* TO 'laoli'@'%' |
+------------------------------------------------------+

-----------------------创建用户并授权------------------------->
创建用户并授权
grant 权限列表 on 数据库.表名 to '用户名'@'访问的主机名' identified by '密码' with option

示例:创建一个laoli的账号,密码为12345678,可以任意电脑进行连接访问,并且对jing_dong数据库中的所有表拥有所有权限.

grant all privileges on jing_dong.* to 'laoli'@'%' identified by '12345678';

with option表示用户可以将自己拥有的权限授权给其他用户

示例: 更改所有权限
grant all privileges on *.* to 'root'@'%' identified by 'password' with grant option;
 
示例:grant select on jing_dong.* to 'laowang'@'localhost' identified by '123456';
说明:jing_dong.*表示可以操作数据库jing_dong的所有表,*表示所有表.权限是查询权限select

访问主机通常使用%号,表示此账户可以使用任何ip的主机登录访问此数据库.
访问主机可以设置成localhost或者具体的ip,表示只允许本机或者特定主机访问.

权限有:create、alter、drop、insert、update、delete、select 增删改查四种

------------------------移除权限-------------------------------->
移除权限:
revoke 权限 on 数据库.表 from '用户名'@'主机名';

一般不会涉及到这些.这是运维的事情.但是我们要脑子里面有印象


-------------------------修改权限------------------------------>

1.>grant 权限名称 on 数据库.表名 to 账户@主机 with grant option;
注意:记得修改完权限之后进行flush操作
2.>flush privileges;  刷新权限列表


-------------------------修改密码-------------------------------->
1.>使用root登录,修改mysql的user表

方式:update user set authentication_string=password('新密码') where user='用户名';
示例:update user set authentication_string=password('123) where user='laowang';

2.>刷新权限:flush privileges;

-------------------------删除账户-------------------------------->
方式一:
1.>使用root登录:use mysql;
drop user '用户名'@'主机';
示例:drop user 'laowang'@'%';
方式二:
2.>delete from user where user='用户名';
示例:delete from user where user='laowang';
建议使用方式2.


--操作结束之后记得刷新权限
flush privileges;

ubuntu下面重启mysql服务:
sudo service mysql restart


"""
# ---------------------------------主从配置:--------------------------->
"""
主从配置:  多台机子服务 
主-->接收用户的更新,通过二进制日志发给从服务器,这样来保持主从同步.
因为从 可以看到 主 的日志,你做一步我就做一步.
主 必须打开二进制文件,这样才能让 从 看到.

基于二进制日志 文件

主从之间要有一个唯一的ID号


--------------------------数据库文件备份/恢复------------------------>

备份: mysqldump -uroot -p jing_dong > python.sql;

恢复: mysql -uroot -p 新创建的数据库名 > python.sql;

# 注意:恢复的时候先要创建一个新的数据库



--all-databases --lock-all-tables > ~

目的:解决服务不可用的问题<就是在特殊情况下,服务器挂了,准备多台服务器就可以把这种情况发生的概率降低


show slave status \G;  <PS:status 和 \G之间有没有空格都可以,mysql都会自动识别出来>

如果失败了 reset slave; 重新设置     set是设置的意思,加了re前缀就是重新设置的意思.
如果还不行,使用reset slave all;  全部重新设置

----------------------------------启动slave,查看状态----------------------->
mysql> start slave;
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> show slave status \G;
*************************** 1. row ***************************
               Slave_IO_State: Connecting to master
                  Master_Host: 192.168.17.128
                  Master_User: slave
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000001
          Read_Master_Log_Pos: 746
               Relay_Log_File: DESKTOP-DM93Q7A-relay-bin.000012
                Relay_Log_Pos: 4
        Relay_Master_Log_File: mysql-bin.000001
             Slave_IO_Running: Connecting
            Slave_SQL_Running: Yes
              Replicate_Do_DB:
          Replicate_Ignore_DB:
           Replicate_Do_Table:
       Replicate_Ignore_Table:
      Replicate_Wild_Do_Table:
  Replicate_Wild_Ignore_Table:
                   Last_Errno: 0
                   Last_Error:
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 123
              Relay_Log_Space: 154
              Until_Condition: None
               Until_Log_File:
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File:
           Master_SSL_CA_Path:
              Master_SSL_Cert:
            Master_SSL_Cipher:
               Master_SSL_Key:
        Seconds_Behind_Master: 0
Master_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 2003
                Last_IO_Error: error connecting to master 'slave@192.168.17.128:3306' - retry-time: 60  retries: 2
               Last_SQL_Errno: 0
               Last_SQL_Error:
  Replicate_Ignore_Server_Ids:
             Master_Server_Id: 0
                  Master_UUID:
             Master_Info_File: C:\ProgramData\MySQL\MySQL Server 5.7\Data\master.info
                    SQL_Delay: 0
          SQL_Remaining_Delay: NULL
      Slave_SQL_Running_State: Slave has read all relay log; waiting for more updates
           Master_Retry_Count: 86400
                  Master_Bind:
      Last_IO_Error_Timestamp: 180923 16:01:50
     Last_SQL_Error_Timestamp:
               Master_SSL_Crl:
           Master_SSL_Crlpath:
           Retrieved_Gtid_Set:
            Executed_Gtid_Set:
                Auto_Position: 0
         Replicate_Rewrite_DB:
                 Channel_Name:
           Master_TLS_Version:
1 row in set (0.00 sec)



注意:Slave_IO_Running: Connecting
     Slave_SQL_Running: Yes
     
只有这两项都是Yes的状态下,才说明主从同步设置成功.如上显示Connecting一般都是主从之间通信有问题,务必要注意检查.
"""