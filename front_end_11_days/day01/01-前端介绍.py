print('前端:')
"""
1.>注释标签:ctrl + /

2.>标题标签:h开头 <h1>到<h6>6级  醒目的,引人注意.用在比较醒目的地方.一共有6级.复制当前行的快捷键:先ctrl + c 再 ctrl + v
级别越大,显示出来越小.h1表示最大,h6表示最小.
	添加属性:居中 align="center",默认情况下是居左.align="left",也有居右.
	
3.>段落标签:新闻中很多段落 <p></p>

4.>默认标签:<!doctype html> --> 声明一个html5的文档
	<html> ---> html的开始标签,类似main函数
	<head> ---> 头标签.表示头部  charset编码格式,在开发的时候,只能使用utf-8,绝大多数
			<title> -->标题  是指在网页顶端显示.用在浏览器的上方
	<body> --->身体标签,存放h5代码,所有代码都是在body里面
	
5.>换行标签: <br /> 是一个单个标签.实现一个换行的效果

6.>字体标签: <font color='red',size='1',face='宋体'></font>  size 是1到7 一共7个级别 
	1号字体最小,7号字体最大
	
7.>盒子标签:<div>  ---> 表示盒子标签,是一个透明的盒子 一般没什么效果.实现一个分隔的作用.透明盒子里面可以放各种标签

8.>图片标签:<img src="" title="" alt=""/> ---> src设置图片路径,title-->鼠标在图片上的时候显示文字信息 alt --> 如果图片路径错误,显示alt里面的文字

9.>一般在开发时候都会添加一个div盒子,因为有些标签没有的属性,需要div实现.div实现一个包裹的效果

10.>超链接标签:<a href="http:www.baidu.com" target="_blank"></a>  实现从一个地址跳转到另外一个地址 href --> 要进入的页面地址.超链接标签可以写本地的地址,也可以写网络地址 target表示是否开启一个新的窗口 不设置属性会在当前窗口<会删除之前的页面>设置了会开启一个新页面,一般都会设置.开一个新窗口.<意思就是在浏览器中再开一个显示页面>

11.>友情链接是必备的,写网页的时候.

12.>回到顶部:<p id="top"> id是唯一标识符  <a href="# top"># 表示去寻找id 是top的地方.

13.>空格标签: &nbsp 作用是空格

14.> 大于和小于:&lt 和  &gt       

15.> 格式化代码的快捷键:ctrl + shift + F ,注意这个快捷键是否被其他程序占用

16.> Pycharm中格式化代码: shift + alt + F

17.> Pycharm中运行程序:shift + alt + F6

布局css:
css都放在head标签里面

1.>选择器{属性:值;属性:值;...} 选择器就是body里面的标签.只不过在css里面叫选择器

	<style type="text/css">   div:表示选择器,也叫标签 ,px表示像素,是html长度,高度等表示大小的单位
		div{
		}
	</style>
三种引入方式:
1.内联式 2.嵌入式 3.外链式   推荐使用嵌入式
<link rel=""> 外链式

2.>标签选择器: h2{} 必须和下面的标签保持一致

3.>类选择器:<div class="red"> class是固定的语法
	.red{}
	. 表示寻找class 
4.>层级选择器:也叫做后代选择器 
	div p{}  中间通过空格连接展示, 前面标签是后面标签的父级元素,后面的标签是它的子级元素

5.>css常用属性:
	width  宽
	height  高
	background  背景
	border:1px solid red 边框   
		1px 表示边框的大小 ,solid 表示使用边框的线条<实线> red 绘制边框的颜色
		除了solid外,还有 dotted 点线 ,dashed 虚线,double 双线,在前端里面只有这四种线
		
		border 可以拆分开写.边框属性需要注意:所有的边框可以分开写
		border-top:1px solid red  上边框
		border-bottom:1px solid red  下边框
		border-left:1px dotted blue  左边框
		border-right:1px dashed yellow  右边框
	
	.表示class
	#表示id 
	寻找class前面要加.号 ,寻找id要加#号
	
	float:浮动属性 让标签在一行显示  将多个div并排显示.注意:在设置浮动属性的时候必须所有div标签部分都设置,不能只设置一个,其余的不设置.
	
	文本属性:
		color:颜色
		font-size:大小
		font-family:设置字体样式  如果使用字体标签 是 face ,如果是样式<css里面>里面,设置字体就是font-family
		font-weight:bold  设置文字粗细  bold是加粗的效果 normal默认 bolder是更粗的效果,还可以设置数字表示的粗细程度.设置数字和设置英文是一个意思
		line-height: 90% 行间距,行高 主要作用是用来纵向居中显示,显示效果是一行与一行之间文本的间距.
		text-decoration:none; 设置去掉下划线
		如果在a标签里面不写url地址,可以写个#号进行占位表示,显示效果会有一个下划线,如果想要去掉下划线,使用text-decoration:none;即可.
		text-indent:2em 设置文字首行缩进 2em表示两个空格的位置,两个文本的位置<就是两个字符的位置>
		text-align:center 文本对齐的方式 ,align是使...成一行 的意思.
		
		margin:0px; 使用文字的时候,系统会默认给添加16px的外边距,margin是边缘,临界的意思.
		
"""

多个div并排显示,并换行继续多排显示?
使用float并排显示,使用display:inline...

html里面的div不能指定位置吗?
移动端可以指定位置,有控件可以实现,具体左边上边,下边,右边有多少像素.