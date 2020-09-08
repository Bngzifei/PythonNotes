## HttpAccess模块

此模块提供了一个简易的基于主机的访问控制.

ngx_http_access_module 模块使有可能对特定IP客户端进行控制. 规则检查按照第一次匹配的顺序

配置样例:

```nginx
location / {
: deny    192.168.1.1;
: allow   192.168.1.0/24;
: allow   10.1.1.0/16;
: deny    all;
}
```

在上面的例子中,仅允许网段 10.1.1.0/16 和 192.168.1.0/24中除 192.168.1.1之外的ip访问.

当执行很多规则时,最好使用 ngx_http_geo_module 模块.

### 放行

**syntax:** *allow [ address | CIDR | all ]*

**default:** *no*

**context:** *http, server, location, limit_except*

以上描述的网络地址有权直接访问

### 禁止

**syntax:** *deny [ address | CIDR | all ]*

**default:** *no*

**context:** *http, server, location, limit_except*

以上描述的网络地址拒绝访问。

LNMP代表的就是：Linux系统下Nginx+MySQL+PHP这种网站服务器架构。

