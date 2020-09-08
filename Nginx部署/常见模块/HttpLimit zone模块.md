## HttpLimit zone模块

本模块可以针对条件，进行会话的并发连接数控制。（例如：限制每个IP的并发连接数。）

配置示例:

```nginx
http {
: limit_zone   one  $binary_remote_addr  10m;

: ...

: server {

: ...

: location /download/ {
: limit_conn   one  1;
: }
```

### limit_zone

```nginx
语法： limit_zone zone_name $variable the_size

默认值： no

作用域： http

本指令定义了一个数据区，里面记录会话状态信息。
$variable 定义判断会话的变量；the_size 定义记录区的总容量。

例子：

limit_zone   one  $binary_remote_addr  10m;
定义一个叫“one”的记录区，总容量为 10M，以变量 $binary_remote_addr 作为会话的判断基准（即一个地址一个会话）。


您可以注意到了，在这里使用的是 $binary_remote_addr 而不是 $remote_addr。

$remote_addr 的长度为 7 至 15 bytes，会话信息的长度为 32 或 64 bytes。 而 $binary_remote_addr 的长度为 4 bytes，会话信息的长度为 32 bytes。

当区的大小为 1M 的时候，大约可以记录 32000 个会话信息（一个会话占用 32 bytes）。
```

### limit_conn

```nginx
语法： limit_conn zone_name the_size

默认值： no

作用域： http, server, location

指定一个会话最大的并发连接数。 当超过指定的最发并发连接数时，服务器将返回 "Service unavailable" (503)。

例子：

limit_zone   one  $binary_remote_addr  10m;

: server {
: location /download/ {
: limit_conn   one  1;
: }
定义一个叫“one”的记录区，总容量为 10M，以变量 $binary_remote_addr 作为会话的判断基准（即一个地址一个会话）。 限制 /download/ 目录下，一个会话只能进行一个连接。 简单点，就是限制 /download/ 目录下，一个IP只能发起一个连接，多过一个，一律503。
```

