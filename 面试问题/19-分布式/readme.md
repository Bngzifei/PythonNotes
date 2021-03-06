## 分布式

https://www.zhihu.com/question/20004877

### 1、分布式与集群的区别是什么？

```
集群是个物理形态,分布式是个工作方式。
只要是一堆机器，就可以叫集群，他们是不是一起协作干活，这个谁也不知道；一个程序或系统，只要运行在不同的机器上，就可以叫分布式，C/S架构也可以叫分布式。

集群一般是物理集中、统一管理的，而分布式系统则不强调这一点。

所以，集群可能运行着一个或者多个分布式系统，也可能根本没有运行分布式系统；分布式系统可能运行在一个集群上，也可能运行在不属于一个集群的多台(2台也算多台)机器上。

分布式的目标是去中心化.没有去中心化的系统不能称之为分布式系统。

最直白的解释:

分布式:一个业务分拆多个子业务,部署在不同的服务器上。
集群：同一个业务，部署在多个服务器上。

集群是同一个业务部署在多台机器上,提高系统可用性。（容灾能力）
分布式是不同的业务模块拆分到不同的机器上，解决高并发/并行（parallel）的问题。
```

### 2、集群式部署在多个服务器上。那假如有10个服务器，同时开始做一个任务，最后做完了，我们只需要一个服务器给的结果，其他9个服务器的结果不就浪费了吗？

```
你这样理解就错了，不是10个服务器做通一个任务，而是有10个任务分布在10台机器上同时处理。

比如：你前台页面有10个用户，分别发送了1个请求，那么如果不是集群的话，那这10个请求需要并行在一台机器上处理，如果每个请求都是1秒钟，那么就会有一个人等待10秒钟，有一个人等待9秒钟，以此类推；那么现在在集群环境下，10个任务并分发到10台机器同时进行，那么每个人的等待时间都还是1秒钟；

当然，你说的浪费确实是，如果系统的并发不是很高，只有一台或者两台机器就能处理的话，那确实是有很大的浪费。
```

### 3、分布式与微服务的区别？

```
分布式的核心就一个字:拆。只要是将一个项目拆分成了多个模块，并将这些模块分开部署，那就算是分布式。

如何拆呢？有两种方式：水平拆分或者垂直拆分，具体如下：

水平拆分：根据“分层”的思想进行拆分。例如，可以将一个项目根据“三层架构” 拆分成 表示层(jsp+servlet)、业务逻辑层（service)和数据层(dao)，然后再分开部署：
    把表示层部署在服务器A上，把service和dao层部署在服务器B上,然后服务器A和服务器B之间通过dubbo等RPC进行整合。

垂直拆分：根据业务进行拆分。例如，可以根据业务逻辑，将“电商项目”拆分成“订单项目”，“用户项目”，和“秒杀项目”。显然这三个拆分后的项目，仍然可以作为独立的项目使用。像这种拆分的方法，就成为垂直拆分。


什么是微服务?
    微服务是非常微小的服务。
    微服务可以理解为一种非常细粒度的垂直拆分。例如上面的订单项目本来就是垂直拆分后的子项目，但实际上“订单项目”还能进一步拆分为“购物项目”，“结算项目”，“售后项目”
    
    “订单项目”完全可以作为一个分布式项目的组成元素，但就不适合作为微服务的组成元素了（因为它还能再拆，而微服务应该是不能再拆的“微小”服务，类似于“原子性”）。
```

总结：

#### 分布式：拆了就行

#### 微服务：细粒度的垂直拆分