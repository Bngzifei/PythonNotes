## HttpGzip模块

这个模块支持在线实时压缩输出数据流

使用范例:

```nginx
: gzip             on;
: gzip_min_length  1000;
: gzip_proxied     expired no-cache no-store private auth;
: gzip_types       text/plain application/xml;
```

内置变量 $gzip_ratio 可以获取到gzip的压缩比率。

### gzip

```nginx
语法: gzip on|off

默认值: gzip off

作用域: http, server, location, if (x) location

开启或者关闭gzip模块
```

### gzip_buffers

```nginx
语法: gzip_buffers number size

默认值: gzip_buffers 4 4k/8k

作用域: http, server, location


设置系统获取几个单位的缓存用于存储gzip的压缩结果数据流。 例如 4 4k 代表以4k为单位，按照原始数据大小以4k为单位的4倍申请内存。 4 8k 代表以8k为单位，按照原始数据大小以8k为单位的4倍申请内存。

如果没有设置，默认值是申请跟原始数据相同大小的内存空间去存储gzip压缩结果。
```

### gzip_comp_level

```nginx
语法: gzip_comp_level 1..9

默认值: gzip_comp_level 1

作用域: http, server, location

gzip压缩比，1 压缩比最小处理速度最快，9 压缩比最大但处理最慢（传输快但比较消耗cpu）。
```

### gzip_min_length

```nginx
语法: gzip_min_length length

默认值: gzip_min_length 0

作用域: http, server, location


设置允许压缩的页面最小字节数，页面字节数从header头中的Content-Length中进行获取。

默认值是0，不管页面多大都压缩。

建议设置成大于1k的字节数，小于1k可能会越压越大。 即: gzip_min_length 1024
```

### gzip_http_version

```nginx
语法: gzip_http_version 1.0|1.1

默认值: gzip_http_version 1.1

作用域: http, server, location

识别http的协议版本。由于早期的一些浏览器或者http客户端，可能不支持gzip自解压，用户就会看到乱码，所以做一些判断还是有必要的。 注：21世纪都来了，现在除了类似于百度的蜘蛛之类的东西不支持自解压，99.99%的浏览器基本上都支持gzip解压了，所以可以不用设这个值,保持系统默认即可。
```

### gzip_proxied

```nginx
语法: gzip_proxied [off|expired|no-cache|no-store|private|no_last_modified|no_etag|auth|any] ...

默认值: gzip_proxied off

作用域: http, server, location

Nginx作为反向代理的时候启用，开启或者关闭后端服务器返回的结果，匹配的前提是后端服务器必须要返回包含"Via"的 header头。

off - 关闭所有的代理结果数据的压缩
expired - 启用压缩，如果header头中包含 "Expires" 头信息
no-cache - 启用压缩，如果header头中包含 "Cache-Control:no-cache" 头信息
no-store - 启用压缩，如果header头中包含 "Cache-Control:no-store" 头信息
private - 启用压缩，如果header头中包含 "Cache-Control:private" 头信息
no_last_modified - 启用压缩,如果header头中不包含 "Last-Modified" 头信息
no_etag - 启用压缩 ,如果header头中不包含 "ETag" 头信息
auth - 启用压缩 , 如果header头中包含 "Authorization" 头信息
any - 无条件启用压缩
```

### gzip_types

```nginx
语法: gzip_types mime-type [mime-type ...]

默认值: gzip_types text/html

作用域: http, server, location

匹配MIME类型进行压缩，（无论是否指定）"text/html"类型总是会被压缩的。


注意：如果作为http server来使用，主配置文件中要包含文件类型配置文件

http
{
	include       conf/mime.types;
	......
}

如果你希望压缩常规的文件类型，可以写成这个样子:

http 
{
: include       conf/mime.types;

: gzip on;
: gzip_min_length  1000;
: gzip_buffers     4 8k;   
: gzip_http_version 1.1; 
: gzip_types       text/plain application/x-javascript text/css text/html application/xml;

: ......	
}
```

