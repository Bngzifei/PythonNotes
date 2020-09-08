## HttpSSL

此模块启用HTTPS支持

它支持检查客户端证书，但有两个限制:

- 无法指定已废除证书的清单(撤销清单)
- 如果您有一个链证书文件(有时称为中间证书)，您不需要像在Apache中那样单独指定它。相反，您需要将chain cert中的信息添加到主证书文件的末尾。这可以通过键入“cat chain”来实现。"在命令行上。一旦完成，你就不会使用链式证书文件做任何其他事情，你只需要把Nginx指向主证书文件。

默认情况下，模块没有被构建，需要指定——with- with-http_ssl_module参数to ./configure来构建模块。构建这个模块需要OpenSSL库和包含文件，它们通常是独立包中必需的文件。

下面是一个配置示例，为了减少CPU负载，建议只运行一个工作进程，并启用保持连接:

```nginx
worker_processes 1;
http {

  server {
    listen               443;
    ssl                  on;
    ssl_certificate      /usr/local/nginx/conf/cert.pem;
    ssl_certificate_key  /usr/local/nginx/conf/cert.key;
    keepalive_timeout    70;
  }

}
```

使用链证书时，只需将额外的证书附加到.crt文件中(在本例中为cert.pem)。您自己的证书需要放在文件的顶部，否则密钥将与密钥不匹配。

### 生成证书

要生成假证书，您可以执行以下步骤:

```nginx
$ cd /usr/local/nginx/conf
$ openssl genrsa -des3 -out server.key 1024
$ openssl req -new -key server.key -out server.csr
$ cp server.key server.key.org
$ openssl rsa -in server.key.org -out server.key
$ openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
```

将新证书配置为nginx.conf:

```nginx
server {

    server_name YOUR_DOMAINNAME_HERE;
    listen 443;
    ssl on;
    ssl_certificate /usr/local/nginx/conf/server.crt;
    ssl_certificate_key /usr/local/nginx/conf/server.key;

}
```

重启Nginx.

现在准备好访问:

```nginx
https://YOUR_DOMAINNAME_HERE
```

### ssl

```nginx
syntax: ssl [on|off]

default: ssl off

context: main, server

Enables HTTPS for a server.
```

### ssl_certificate

```nginx
syntax: ssl_certificate file

default: ssl_certificate cert.pem

context: main, server

指示此虚拟服务器的带PEM格式证书的文件。同一个文件可以包含其他证书，以及PEM格式的密钥。由于版本0.6.7，文件路径相对于nginx配置文件nginx的目录。但不是nginx前缀目录。
```

### ssl_certificate_key

```nginx
syntax: ssl_certificate_key file

default: ssl_certificate_key cert.pem

context: main, server
表示此虚拟服务器的密钥为PEM格式的文件。由于版本0.6.7，文件名路径相对于nginx配置文件nginx的目录。但不是nginx前缀目录。
```

### ssl_client_certificate

```nginx
syntax: ssl_client_certificate file

default: none

context: main, server
表示带有证书CA的PEM格式文件，用于检查客户端证书
```

### ssl_dhparam

```nginx
syntax: ssl_dhparam file

default: none

context: main, server
表示带Diffie-Hellman参数的PEM格式文件，用于协商TLS会话密钥。
```

### ssl_ciphers

```nginx
syntax: ssl_ciphers file

default: ssl_ciphers ALL:!ADH:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP

context: main, server

指令描述了允许的密码。密码以OpenSSL支持的格式分配，例如:
ssl_ciphersALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP;
可以使用以下命令查看完整列表:
openssl ciphers
```

### ssl_crl

```nginx
syntax: ssl_crl file

default: none

context: http, server
这个指令(0.8.7+)在PEM中指定了一个具有已撤销证书(CRL)的文件，该文件用于检查客户端证书。
```

### ssl_prefer_server_ciphers

```nginx
syntax: ssl_prefer_server_ciphers [on|off]

default: ssl_prefer_server_ciphers off

context: main, server
要求协议SSLv3和TLSv1服务器密码优先于客户机的密码。
```

### ssl_protocols

```nginx
syntax: ssl_protocols [SSLv2] [SSLv3] [TLSv1]

default: ssl_protocols SSLv2 SSLv3 TLSv1

context: main, server

指令启用所指示的协议。
```

### ssl_verify_client

```nginx
syntax: ssl_verify_client on|off|ask

default: ssl_verify_client off

context: main, server
指令允许验证客户端证书。参数“ask”检查客户端证书是否提供。
```

### ssl_verify_depth

```nginx
syntax: ssl_verify_depth number

default: ssl_verify_depth 1

context: main, server
设置客户端证书链中的深度检查。
```

### ssl_session_cache

```nginx
syntax: ssl_session_cache off|none|builtin:size and/or shared:name:size

default: ssl_session_cache off

context: main, server
该指令设置用于存储SSL会话的缓存的类型和大小。
缓存类型为:
off -- Hard off:nginx明确地告诉客户端会话不能被重用。
none -- Soft off:nginx对客户端说，会话可以被重新使用，但nginx实际上从不重复使用它们。这是针对一些邮件客户端的解决方案，因为ssl_session_cache可以在邮件代理中使用，也可以在HTTP服务器中使用。
builtin -- the OpenSSL builtin cache:只在一个工作进程内使用.缓存大小根据会话的数量分配。注意:使用此方法时可能会出现内存碎片问题，请在使用此方法时加以考虑。
shared -- 缓存在所有工作进程之间共享:缓存的大小是以字节为单位分配的，1 MB的缓存可以包含大约4000个会话。每个共享缓存必须具有任意名称。具有相同名称的缓存可以在多个虚拟服务器中使用。

可以同时使用这两种类型的缓存，例如:
ssl_session_cache  builtin:1000  shared:SSL:10m;
但是，如果没有这个内置组件，共享缓存的使用应该会更有效。
```

### ssl_session_timeout

```nginx
syntax: ssl_session_timeout time

default: ssl_session_timeout 5m

context: main, server
指定客户端可以重复使用会话参数的时间，会话参数存储在缓存中.
该模块支持多个非标准错误代码，可以借助error_page指令进行调试:
	495 - error checking client certificate
	496 - client did not grant the required certificate
	497 - normal request was sent to HTTPS
调试是在请求完全解除之后完成的，可以通过$request_uri、$uri、$arg等变量进行访问。内置变量模块ngx_http_ssl_module支持多个内置变量:
	$ssl_cipher returns the line of those utilized it is cipher for established SSL-connection
	$ssl_client_serial returns the series number of client certificate for established SSL-connection
	$ssl_client_s_dn returns line subject DN of client certificate for established SSL-connection
	$ssl_client_i_dn returns line issuer DN of client certificate for established SSL-connection
	$ssl_protocol returns the protocol of established SSL-connection
```

### 官方链接:http://nginx.org/ru/docs/http/ngx_http_ssl_module.html

