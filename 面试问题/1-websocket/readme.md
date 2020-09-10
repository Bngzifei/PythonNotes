# 详细介绍:

[http://www.ruanyifeng.com/blog/2017/05/websocket.html](http://www.ruanyifeng.com/blog/2017/05/websocket.html)
[https://www.cnblogs.com/lsdb/p/10949766.html](https://www.cnblogs.com/lsdb/p/10949766.html)
[https://blog.csdn.net/larry_zeng1/article/details/82285265](https://blog.csdn.net/larry_zeng1/article/details/82285265)
[https://www.zhihu.com/question/20215561/answer/40316953](https://www.zhihu.com/question/20215561/answer/40316953)
[http://fullstackpython.atjiang.com/websockets.html](http://fullstackpython.atjiang.com/websockets.html)
[http://www.52im.net/thread-1341-1-1.html](http://www.52im.net/thread-1341-1-1.html)
[https://www.cnblogs.com/JetpropelledSnake/p/9033064.html](https://www.cnblogs.com/JetpropelledSnake/p/9033064.html)



初次接触 WebSocket 的人，都会问同样的问题：我们已经有了 HTTP 协议，为什么还需要另一个协议？它能带来什么好处？

答案很简单，因为 HTTP 协议有一个缺陷：通信只能由客户端发起。

举例来说，我们想了解今天的天气，只能是客户端向服务器发出请求，服务器返回查询结果。HTTP 协议做不到服务器主动向客户端推送信息
没有其他能像 WebSocket 一样实现全双工传输的技术了，迄今为止，大部分开发者还是使用 Ajax 轮询来实现，但这是个不太优雅的解决办法，
WebSocket 虽然用的人不多，可能是因为协议刚出来的时候有安全性的问题以及兼容的浏览器比较少，但现在都有解决。如果你有这些需求可以考虑使用 WebSocket：

多个用户之间进行交互；

需要频繁地向服务端请求更新数据。

比如弹幕、消息订阅、多玩家游戏、协同编辑、股票基金实时报价、视频会议、在线教育等需要高实时的场景。