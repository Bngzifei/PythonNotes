## HttpFcgi模块

这个模块允许Nginx 与FastCGI 进程交互，并通过传递参数来控制FastCGI 进程工作。

配置实例:

```nginx
location / {
  fastcgi_pass   localhost:9000;
  fastcgi_index  index.php;

  fastcgi_param  SCRIPT_FILENAME  /home/www/scripts/php$fastcgi_script_name;
  fastcgi_param  QUERY_STRING     $query_string;
  fastcgi_param  REQUEST_METHOD   $request_method;
  fastcgi_param  CONTENT_TYPE     $content_type;
  fastcgi_param  CONTENT_LENGTH   $content_length;
}
```

语法:

### fastcgi_buffers

```nginx
syntax: fastcgi_buffers the_number is_size;

default: fastcgi_buffers 8 4k/8k;

context: http, server, location

该指令集设置缓冲区的数量和大小，用于缓存从 FastCGI Server 接收到的数据。默认情况下，一个缓冲区的大小相当于一个页面的大小。根据平台的不同设置为4K/8K
```

### fastcgi_buffer_size

```nginx
syntax: fastcgi_buffer_size the_size

default: fastcgi_buffer_size 4k/8k

context: http, server, location

该指令设置从fastcgi服务器获得的缓冲大小，将读取响应的第一部分。
在响应的这一部分中，小的response-header通常位于其中。
默认情况下，buffersize等于指令fastcgi_buffers中的一个缓冲区的大小;但是，可以将其设置为less。
```

### fastcgi_cache

```nginx
syntax: fastcgi_cache zone;

default: none

context: http, server, location

设置缓存在共享内存中的名称. 一块区域可以被用于不用的地方。
```

### fastcgi_cache_key

```nginx
syntax: fastcgi_cache_key line ;

default: none

context: http, server, location

设置缓存的key, 例:
fastcgi_cache_key localhost: 9000 $ request_uri;
```

### fastcgi_cache_methods

```nginx
syntax: fastcgi_cache_methods [GET HEAD POST];

default: fastcgi_cache_methods GET HEAD;

context: main,http,location

GET/HEAD是语法糖，即你不能禁用GET/HEAD，即使你只是设置.
例子:
fastcgi_cache_methods  POST;

```

### fastcgi_cache_min_uses

```nginx
syntax: fastcgi_cache_min_uses n

default: fastcgi_cache_min_uses 1

context: http, server, location
```

### fastcgi_cache_path

```nginx
syntax: fastcgi_cache_path /path/to/cache [levels=m:n keys_zone=name:time inactive=time clean_time=time]

default: none

context: http, server, location
```

### fastcgi_cache_use_stale

```nginx
syntax: fastcgi_cache_use_stale [updating|error|timeout|invalid_header|http_500]

default: fastcgi_cache_use_stale off;

context: http, server, location
```

### fastcgi_cache_valid

```nginx
syntax: fastcgi_cache_valid [http_error_code|time]

default: none

context: http, server, location
```

### fastcgi_index

```nginx
syntax: fastcgi_index file

default: none

context: http, server, location

将被附加到URI并存储在变量$fastcgi_script_name中的文件的名称(如果URI以斜杠结尾)。
```

### fastcgi_hide_header

```nginx
syntax: fastcgi_hide_header name

context: http, server, location

默认情况下Nginx 不会从FastCGI 进程里给客户端发送"Status" 和"X-Accel-..." 消息头。这个指令可以用来掩饰别的headers 。

如果需要"Status" 和"X-Accel-..." 消息头，那就需要使用这个指令让FastCGI 强制发送消息头给客户端。
```

### fastcgi_ignore_client_abort

```nginx
syntax: fastcgi_ignore_client_abort on|off

default: fastcgi_ignore_client_abort off

context: http, server, location

这个指令用来决定忽略用户取消的请求。
```

### fastcgi_intercept_errors

```nginx
syntax: fastcgi_intercept_errors on|off

default: fastcgi_intercept_errors off

context: http, server, location

这个指令用来决定是否要把客户端转向4xx和5xx错误页，或允许Nginx自动指定错误页页。

注意：你需要在此明确错误页,它才是有用的。Igor 曾说：“如果没有定制的处理机制，Nginx不会拦截一个没有缺省页的错误。Nginx 只会拦截一些小的错误，放过其他一些。
```

### fastcgi_param

```nginx
syntax: fastcgi_param parameter value

default: none

context: http, server, location

该指令指定的参数,将被传递给FastCGI-server。

它可能使用字符串、变量及其它们的组合来作为参数值。如果不在此制定参数，它就会继承外层设置；如果在此设置了参数，将清除外层相关设置，仅启用本层设置。

下面是一个例子,对于PHP来说的最精简的必要参数：

  fastcgi_param  SCRIPT_FILENAME  /home/www/scripts/php$fastcgi_script_name;
  fastcgi_param  QUERY_STRING     $query_string;

参数SCRIPT_FILENAME 是PHP 用来确定执行脚本的名字，而参数QUERY_STRING 是它的一个子参数。

如果要处理POST,那么这三个附加参数是必要的：

  fastcgi_param  REQUEST_METHOD   $request_method;
  fastcgi_param  CONTENT_TYPE     $content_type;
  fastcgi_param  CONTENT_LENGTH   $content_length;

如果PHP 在编译时使用了--enable-force-cgi-redirect选项，设置参数REDIRECT_STATUS 的值为200就是必须的了。

  fastcgi_param  REDIRECT_STATUS  200;
```

