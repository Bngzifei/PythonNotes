## HttpProxy模块

此模块专门将请求导向其它服务.

示例:

```nginx
location / {
: proxy_pass        http://localhost:8000;
: proxy_set_header  X-Real-IP  $remote_addr;
}
```

注意一点,当使用HTTP PROXY 模块时(或者甚至是使用FastCGI时),用户的整个请求会在nginx中缓冲直至传送给后端被代理的服务器.因此,上传进度的测算就会运作得不正确,如果它们通过测算后端服务器收到的数据来工作的话。

### proxy_buffer_size

```nginx
语法: proxy_buffer_size the_size

默认值: proxy_buffer_size 4k/8k

上下文: http, server, location

该指令设置缓冲区大小,从被代理的后端服务器取得的响应内容,会先读取放置到这里.

小的响应header通常位于这部分响应内容里边.

默认来说,该缓冲区大小等于指令
proxy_buffers
所设置的;但是,你可以把它设置得更小.
```

### proxy_buffering

```nginx
语法: proxy_buffering on|off

默认值: proxy_buffering on

上下文: http, server, location

该指令开启从后端被代理服务器的响应内容缓冲.

如果缓冲区开启,nginx假定被代理的后端服务器会以最快速度响应,并把内容保存在由指令
proxy_buffer_size
和
proxy_buffers
指定的缓冲区里边.

如果响应内容无法放在内存里边,那么部分内容会被写到磁盘上.

如果缓冲区被关闭了,那么响应内容会按照获取内容的多少立刻同步传送到客户端

nginx不尝试计算被代理服务器整个响应内容的大小,nginx能从服务器接受的最大数据,是由指令
proxy_buffer_size
指定的.
```

### proxy_buffers

```nginx
语法: proxy_buffers the_number is_size;

默认值: proxy_buffers 8 4k/8k;

上下文: http, server, location

该指令设置缓冲区的大小和数量,从被代理的后端服务器取得的响应内容,会放置到这里. 默认情况下,一个缓冲区的大小等于页面大小,可能是4K也可能是8K,这取决于平台
```

### proxy_busy_buffers_size

```nginx
语法: proxy_busy_buffers_size size;

默认值: proxy_busy_buffers_size proxy_buffer_size * 2;

上下文: http, server, location
```

### proxy_connect_timeout

```nginx
语法: proxy_connect_timeout timeout_in_seconds

上下文: http, server, location

此指令为到proxyserver的连接分配超时。这不是服务器返回页面的时间，而是[#proxy_read_timeout proxy_read_timeout]语句。如果您的proxyserver启动了，但是挂起了(例如，它没有足够的线程来处理您的请求，因此它将您放入连接池中，以便稍后处理)，那么此语句将不会有任何帮助，因为已经建立了到服务器的连接。有必要记住，这次暂停不能超过75秒。
```

### proxy_headers_hash_bucket_size

```nginx
语法: proxy_headers_hash_bucket_size size;

默认值: proxy_headers_hash_bucket_size 64;

上下文: http, server, location, if
这个指令设置散列表的桶大小。
```

### proxy_headers_hash_max_size

```nginx
语法: proxy_headers_hash_max_size size;

默认值: proxy_headers_hash_max_size 512;

上下文: http, server, location, if
这个指令设置了hashtable的最大大小。
```

### proxy_ignore_client_abort

```nginx
语法: proxy_ignore_client_abort [ on|off ]

默认值: proxy_ignore_client_abort off

上下文: http, server, location

Available since: 0.3.36
如果客户端断开请求,也保持后端的下载
```

### proxy_intercept_errors

```nginx
语法: proxy_intercept_errors [ on|off ]

默认值: proxy_intercept_errors off

上下文: http, server, location

This directive decides if nginx will intercept responses with HTTP status codes of 400 and higher.

By default all responses will be sent as-is from the proxied server.

If you set this to
on
then nginx will intercept status codes that are explicitly handled by an
error_page
directive. Responses with status codes that do not match an
error_page
directive will be sent as-is from the proxied server.
```

### proxy_max_temp_file_size

```nginx
语法: proxy_max_temp_file_size size;

默认值: proxy_max_temp_file_size 1G;

上下文: http, server, location, if
```

### proxy_method

```nginx
语法: proxy_method [method]

默认值: None

上下文: http, server, location

用于允许代理其他HTTP方法。
目前，Nginx似乎只允许这个指令的一个实例，并且只接受一个参数(方法)，所以还不清楚这对于代理Subversion之类的东西有多大用处。
例如:
: proxy_method PROPFIND;
```

### proxy_next_upstream

```nginx
语法: proxy_next_upstream [error|timeout|invalid_header|http_500|http_503|http_404|off]

默认值: proxy_next_upstream error timeout

上下文: http, server, location
指令决定，在什么情况下请求将被传输到下一个服务器:
error — an error has occurred while connecting to the server, sending a request to it, or reading its response;
timeout — occurred timeout during the connection with the server, transfer the requst or while reading response from the server;
invalid_header — server returned a empty or incorrect answer;
http_500 — server returned answer with code 500
http_503 — server returned answer with code 503
http_404 — server returned answer with code 404
off — it forbids the request transfer to the next server

只有在没有向客户端传输任何内容的情况下，才能将请求传输到下一个服务器——也就是说，如果在传输请求的过程中出现错误或超时，则不可能在另一个服务器上重试当前请求。
```

### proxy_pass

```nginx
语法: proxy_pass URL

默认值: no

上下文: location, if in location
该指令设置监听代理服务器的端口或套接字，以及反映位置的URI。
端口可以用主机名或地址和端口的名称来表示，例如:
proxy_pass http://localhost:8000/uri /;
和socket——unix的socket形式:
proxy_pass http://unix:/tmp/backend.socket:/uri /;
路径在unix后面指示,并在两个冒号之间结束.

随着对服务器的请求的转移，对应于位置的URI被替换为URI，在指令proxy_pass中指出。
但是，当无法确定被替换的位置时，这条规则有两个例外:
1.如果位置是由正则表达式分配的;
2.如果在代理的位置在指令的帮助下重写改变URI和与此配置将精确处理请求(中断):

location  /name/ {
: rewrite      /name/([^/] +)  /users?name=$1  break;
: proxy_pass   http://127.0.0.1;
}

对于这些URI，它是在没有映射的情况下传输的。
此外，还可以指定URI请求将以与发送客户机相同的形式传输，而不是以处理后的形式传输v。

在功能工作过程中:
1.两个或多个斜杠被转换成一个斜杠:“//”——“/”;
2.对当前目录的引用被删除:"/。”——“/”;
3.对以前目录的引用被删除:“/dir /..””——“/”。

如果在服务器上需要以未处理的形式传输URI，那么在指令proxy_pass中需要指出没有URI的URL服务器:

location  /some/path/ {
: proxy_pass   http://127.0.0.1;
}



```

### proxy_pass_header

```nginx
语法: proxy_pass_header the_name

上下文: http, server, location

这个指令允许传输禁止响应的标题行.

示例:
location / {
: proxy_pass_header Server;
: proxy_pass_header X-MyHeader;
}
```

### proxy_pass_request_body

```nginx
语法: proxy_pass_request_body [ on | off ] ;

默认值: proxy_pass_request_body on;

上下文: http, server, location

```

### proxy_pass_request_headers

```nginx
语法: proxy_pass_request_headers [ on | off ] ;

默认值: proxy_pass_request_headers on;

上下文: http, server, location
```

### proxy_redirect

```nginx
语法: proxy_redirect [ default|off|redirect replacement ]

默认值: proxy_redirect default

上下文: http, server, location
这个指令设置文本，必须在响应头“位置”和“刷新”中更改。
让我们假设代理服务器返回了一行:
Location: http://localhost:8000/two/some/uri/
那么,命令 
proxy_redirect   http://localhost:8000/two/   http://frontend/one/;
将会把这一行重写为表单.
Location: http://frontend/one/some/uri/
在可替换行中，可以不指明服务器的名称:
proxy_redirect http://localhost:8000/two/ /;
如果与80不同，则设置服务器和端口的基本名称。
默认情况下，由参数“default”给出的更改使用了指令位置和proxy_pass的参数。
因此，以下两种配置是等价的:
location /one/ {
: proxy_pass       http://upstream:port/two/;
: proxy_redirect   default;
}

location /one/ {
: proxy_pass       http://upstream:port/two/;
: proxy_redirect   http://upstream:port/two/   /one/;
}

在替换行，可以使用一些变量:
proxy_redirect   http://localhost:8000/    http://$host:$server_port/;
这个指令重复了几次:
: proxy_redirect   default;
: proxy_redirect   http://localhost:8000/    /;
: proxy_redirect   http://www.example.com/   /;
参数off禁止所有proxy_redirect.
这一级的指令:
: proxy_redirect   off;
: proxy_redirect   default;
: proxy_redirect   http://localhost:8000/    /;
: proxy_redirect   http://www.example.com/   /;
在这个指令的帮助下，可以添加主机名相对重定向，由代理服务器发出:
proxy_redirect   /   /;

```

### proxy_read_timeout

```nginx
语法: proxy_read_timeout the_time

默认值: proxy_read_timeout 60

上下文: http, server, location

这个指令为代理服务器的响应设置读超时。它决定NGINX将等待多长时间来获得请求的响应。超时不是为整个响应建立的，而是仅在两个读取操作之间建立的。
```

### proxy_send_lowat

```nginx
语法: proxy_send_lowat [ on | off ]

默认值: proxy_send_lowat off;

上下文: http, server, location, if

这个指令设置为SNDLOWAT。
```

### proxy_send_timeout

```nginx
语法: proxy_send_timeout time_in_seconds

默认值: proxy_send_timeout 60

上下文: http, server, location

该指令通过向代理服务器传输请求来分配超时。超时不是建立在请求的整个传输上，而是建立在记录的两次操作之间。如果在此之后代理服务器不再接收新数据，则nginx将关闭连接
```

### proxy_set_header

```nginx
语法: proxy_set_header header value

默认值: Host and Connection

上下文: http, server, location

这个指令允许重新定义和添加一些将被传输到代理服务器的请求头行。
作为值，可以使用文本、变量及其组合。
这个指令继承自上一层，当在这一层没有描述他们的指令
proxy_set_header
默认情况下，只有两行会被重新定义:
proxy_set_header Host $proxy_host;
proxy_set_header Connection Close;
不变的请求头“Host”可以这样发送:
proxy_set_header Host $http_host;
但是，如果客户端请求中没有这一行，则不会传输任何内容。
在这种情况下，最好使用变量$host，它的值等于请求头“host”中的服务器名，或者是服务器的基本名，如果没有行:
proxy_set_header Host $host;
此外，可以将服务器的名称与代理服务器的端口一起传输:
proxy_set_header Host $host:$proxy_port;
```

### proxy_store

```nginx
语法: proxy_store [on | off | path]

默认值: proxy_store off

上下文: http, server, location

这个指令设置上游文件存储的路径。参数“on”按照指令别名或根中指定的路径保存文件。参数“off”禁止存储。此外，路径名可以通过带有变量的行来明确赋值:
proxy_store   /data/www$original_uri;
文件的修改时间将设置为响应中“Last-Modified”标头的日期。为了能够安全的文件在这个目录下是必须的路径下的临时文件目录，由指令proxy_temp_path为数据位置。
该指令可用于创建后端动态输出的本地副本，例如，这些副本不经常更改:

location /images/ {
: root                 /data/www;
: error_page           404 = /fetch$uri;
}

location /fetch {
: internal;

: proxy_pass           http://backend;
: proxy_store          on;
: proxy_store_access   user:rw  group:rw  all:r;
: proxy_temp_path      /data/temp;

: alias                /data/www;
}

需要说明的是，proxy_store不是缓存，而是随需应变的镜像。
```

### proxy_store_access

```nginx
语法: proxy_store_access users:permissions [users:permission ...]

默认值: proxy_store_access user:rw

上下文: http, server, location
该指令为创建的文件和目录分配权限，例如:
proxy_store_access  user:rw  group:rw  all:r;
如果为组或所有分配了任何权限，则不需要为用户分配权限:
proxy_store_access  group:rw  all:r;
```

### proxy_temp_file_write_size

```nginx
语法: proxy_temp_file_write_size size;

默认值: proxy_temp_file_write_size proxy_buffer_size * 2;

上下文: http, server, location, if
```

### proxy_temp_path

```nginx
语法: proxy_temp_path dir-path [ level1 [ level2 [ level3 ]  ;

默认值: $NGX_PREFIX/proxy_temp controlled by --http-proxy-temp-path at ./configure stage

上下文: http, server, location

这个指令的工作原理类似于client_body_temp_path，它指定一个位置来缓冲文件系统中代理的大型请求。
```

### 官方链接:http://nginx.org/ru/docs/http/ngx_http_proxy_module.html