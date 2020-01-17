## HttpHeaders模块

本模板可以设置HTTP报文的头标。

示例:

```nginx
: expires     24h;
: expires     0;
: expires     -1;
: expires     epoch;
: add_header  Cache-Control  private;
```

### 增加头标

```nginx
语法： add_header name value

默认值： none

作用域： http, server, location

当HTTP应答状态码为 200、204、301、302 或 304 的时候，增加指定的HTTP头标。

其中头标的值可以使用变量。
```

### 设置过期时间

```nginx
语法： expires [time|epoch|max|off]

默认值： expires off

作用域： http, server, location

使用本指令可以控制HTTP应答中的“Expires”和“Cache-Control”的头标，（起到控制页面缓存的作用）。

可以在time值中使用正数或负数。“Expires”头标的值将通过当前系统时间加上您设定的 time 值来获得。

epoch 指定“Expires”的值为 1 January, 1970, 00:00:01 GMT。
max 指定“Expires”的值为 31 December 2037 23:59:59 GMT，“Cache-Control”的值为10年。
-1 指定“Expires”的值为 服务器当前时间 -1s,即永远过期

“Cache-Control”头标的值由您指定的时间来决定：
负数：
Cache-Control: no-cache
正数或零：
Cache-Control: max-age = #
, # 为您指定时间的秒数。
"off" 表示不修改“Expires”和“Cache-Control”的值
```

