## HttpAuthBasic模块

该模块可以使你使用用户名和密码基于 HTTP 基本认证方法来保护你的站点或其部分内容。

实例配置

```nginx
location  /  {
: auth_basic            "Restricted";
: auth_basic_user_file  conf/htpasswd;
}
```

### auth_basic

**语法：** *auth_basic [ text|off ]*

**默认值：** *auth_basic off*

**作用域：** *http, server, location, limit_except*

该指令包含用于 HTTP 基本认证 的测试名和密码。分配的参数用于认证领域。值 "off" 可以使其覆盖来自上层指令的继承性。

### auth_basic_user_file

**语法：** *auth_basic_user_file the_file*

**默认值：** *no*

**作用域：** *http, server, location, limit_except*

该指令为某认证领域指定 htpasswd 文件名。

文件格式类似于下面的内容：

```nginx
用户名:密码
用户名2:密码2:注释
用户名3:密码3
```

密码必须使用函数 crypt(3) 加密。 你可以使用来自 Apache 的 htpasswd 工具来创建密码文件。

你也可以使用perl 创建密码文件,pw.pl 的内容：

```nginx
#!/usr/bin/perl
use strict;

my $pw=$ARGV[0] ;
print crypt($pw,$pw)."\n";
```

然后执行:

```nginx
chmod +x pw.pl
./pw.pl password
papAq5PwY/QQM
```

papAq5PwY/QQM 就是password 的crypt()密码。