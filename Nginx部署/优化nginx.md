## 优化Nginx

Ngnix使用hash表来协助完成请求的快速处理。

考虑到保存键及其值的hash表存储单元的大小不至于超出设定参数(hash bucket size)， 在启动和每次重新配置时，Nginx为hash表选择尽可能小的尺寸。

直到hash表超过参数(hash max size)的大小才重新进行选择. 对于大多数hash表都有指令来修改这些参数。例如，保存服务器名字的hash表是由指令

```nginx
server_names_hash_max_size
```

和

```nginx
server_names_hash_bucket_size
```

所控制的。参数hash bucket size总是等于hash表的大小，并且是一路处理器缓存大小的倍数。在减少了在内存中的存取次数后，使在处理器中加速查找hash表键值成为可能。如果hash bucket size等于一路处理器缓存的大小，那么在查找键的时候，最坏的情况下在内存中查找的次数为2。第一次是确定存储单元的地址，第二次是在存储单元中查找键值。因此，如果Nginx给出需要增大 hash max size 或 hash bucket size的提示，那么首要的是增大前一个参数的大小。

### 事件模型

Nginx支持如下处理连接的方法（I/O复用方法），这些方法可以通过 use 指令指定.

- select 标准方法。 如果当前平台没有更有效的方法，它是编译时默认的方法。你可以使用配置参数:

  ```nginx
  --with-select_module
  ```

  和

  ```nginx
  --without-select_module
  ```

  来启用或禁用这个模块

- poll 标准方法。如果当前平台没有更有效的方法，它是编译时默认的方法。你可以使用配置参数

  ```nginx
  --with-poll_module
  ```

  和

  ```nginx
  --without-poll_module
  ```

  来启用或禁用这个模块。

- kqueue 高效的方法，使用于 FreeBSD 4.1+, OpenBSD 2.9+, NetBSD 2.0 和 MacOS X. 使用双处理器的MacOS X系统使用kqueue可能会造成内核崩溃。

- epoll 高效的方法，使用于Linux内核2.6版本及以后的系统。在某些发行版本中，如SuSE 8.2, 有让2.4版本的内核支持epoll的补丁。

- rtsig 可执行的实时信号，使用于Linux内核版本2.2.19以后的系统。默认情况下整个系统中不能出现大于1024个POSIX实时(排队)信号。这种情况对于高负载的服务器来说是低效的；所以有必要通过调节内核参数

  ```nginx
  /proc/sys/kernel/rtsig-max
  ```

  来增加队列的大小。可是从Linux内核版本2.6.6-mm2开始， 这个参数就不再使用了，并且对于每个进程有一个独立的信号队列，这个队列的大小可以用 RLIMIT_SIGPENDING 参数调节。当这个队列过于拥塞，nginx就放弃它并且开始使用 poll 方法来处理连接直到恢复正常。

- /dev/poll 高效的方法，使用于 Solaris 7 11/99+, HP/UX 11.22+ (eventport), IRIX 6.5.15+ 和 Tru64 UNIX 5.1A+.

- eventport 高效的方法，使用于 Solaris 10. 为了防止出现内核崩溃的问题， 有必要安装 [这个](http://sunsolve.sun.com/search/document.do?assetkey=1-26-102485-1) 安全补丁。