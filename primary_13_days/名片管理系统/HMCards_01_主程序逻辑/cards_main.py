# 主文件: 负责程序的主要业务逻辑
import cards_tool  # 导入模块
"""
无限重复1-3步
1.显示界面
2.获取用户的输入
3.根据用户输入,执行对应的功能
无限循环:  程序的实现要求  一般会有出口(可以退出程序)
死循环: 程序员编程中的bug 
"""
while True:
    # 1.显示界面
    cards_tool.show_menu()
    # 2.获取用户的输入
    cmd_num = input("请选择执行的操作:")
    print("您选择的功能:%s" % cmd_num)
    # 3.条件判断 根据用户输入,执行功能
    if cmd_num == "1":  # TODO 新建名片
        print("新建名片")
    elif cmd_num == "2":  # 显示全部
        print("显示全部")
    elif cmd_num == "3":  # 查询名片
        print("查询名片")
    elif cmd_num == "0":  # 退出系统
        print("欢迎再次使用[名片管理系统]")
        break
    else:  # 输入错误
        print("输入有误,请重新输入")
