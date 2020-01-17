## HttpLimitRequest模块

此模块允许您限制给定会话的请求数量，或者在特殊情况下使用一个地址。

```nginx
http {
    limit_req_zone  $binary_remote_addr  zone=one:10m   rate=1r/s;

    ...
 
    server {
 
        ...
 
        location /search/ {

            limit_req   zone=one  burst=5;
        }
```

指令:

```nginx
Syntax: limit_req_zone $session_variable zone=name_of_zone:size rate=rate

Default: none

Context: http

指令描述了存储会话状态的区域。会话的值由给定的变量决定。使用的例子:
limit_req_zone  $binary_remote_addr  zone=one:10m   rate=1r/s;
在这种情况下，会话状态被分配为一个名为“one”的区域，该区域的查询平均速度限制为每秒1个请求。
在本例中，会话是按每个用户跟踪的，但是请注意，我们使用了变量$binary_remote_addr，而不是变量$remote_addr，从而将状态大小减少到64字节。一个1mb的区域可以容纳大约16000个这种大小的州。
速度的单位是请求/秒或请求/分钟。速率必须是整数，所以如果需要指定每秒少于一个请求，例如每两秒一个请求，那么可以将其指定为“30r/m”。
```

```nginx
Syntax: limit_req zone=zone burst=burst [nodelay]

Default: none

Context: http, server, location

指令指定区域(区域)和请求的最大可能爆发(爆发).如果超过了区域内的要求,请求被延迟,以便以给定的速度处理查询.多余的请求将被延迟，直到它们的数量不超过指定的突发数量.在这种情况下，请求完成代码“服务不可用”(503)。默认情况下，突发事件为零。
例如下面示例:
limit_req_zone  $binary_remote_addr  zone=one:10m   rate=1r/s;
    server {
        location /search/ {
            limit_req   zone=one  burst=5;
        }

允许用户平均每秒不超过1个请求，不超过5个查询。如果在限制突发延迟内的多余请求是不必要的，您应该使用nodelay:
         limit_req   zone=one  burst=5  nodelay;
```

