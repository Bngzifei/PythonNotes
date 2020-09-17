https://www.cnblogs.com/fundebug/p/details-about-6-web-security.html

常见六大Web安全攻防:

1、XSS 跨站脚本攻击
XSS (Cross-Site Scripting)，因为缩写和 CSS重叠，所以只能叫 XSS。

2、CSRF CSRF(Cross Site Request Forgery)，即跨站请求伪造


3、点击劫持
点击劫持是一种视觉欺骗的攻击手段。攻击者将需要攻击的网站通过 iframe 嵌套的方式嵌入自己的网页中，
并将 iframe 设置为透明，在页面中透出一个按钮诱导用户点击。


4、URL跳转漏洞
定义：借助未验证的URL跳转，将应用程序引导到不安全的第三方区域，从而导致的安全问题。



5、SQL注入
SQL注入是一种常见的Web安全漏洞，攻击者利用这个漏洞，可以访问或修改数据，或者利用潜在的数据库漏洞进行攻击。



6、OS命令注入攻击

OS命令注入和SQL注入差不多，只不过SQL注入是针对数据库的，而OS命令注入是针对操作系统的。OS命令注入攻击指通过Web应用，
执行非法的操作系统命令达到攻击的目的。只要在能调用Shell函数的地方就有存在被攻击的风险。倘若调用Shell时存在疏漏，就可以执行插入的非法命令。







