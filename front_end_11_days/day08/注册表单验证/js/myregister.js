//真实项目的时候,js必须放到外面,使用外链式的方式写
//不行就先写js.html的复制粘贴进来
//首先加载进来
$(function() {
	//用户名
	var oUser = $('#user_name')
	//密码
	var oPwd = $('#pwd')
	//确认密码
	var oCpwd = $('#cpwd')
	//邮箱
	var oEmail = $('#email')
	//是否同意
	var oCheck = $('#allow')
	//表单
	var oForm = $('form')

	//校验
	//用户名验证：(数字字母或下划线6到20位)
	var reUser = /^\w{6,20}$/;

	//邮箱验证：      会有.com.cn的情况.不过一般都是.com或者.cn一级的
	var reMail = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/i;

	//密码验证：
	var rePass = /^[\w!@#$%^&*]{6,20}$/;

	//手机号码验证：  一共11位,第二位是3或者4或者5或者7或者8剩下的是数字就行.
	var rePhone = /^1[34578]\d{9}$/;
	
	//如果表单校验成功返回true,否则返回false
	var cUser = false
	var cPwd = false
	var cCpwd = false
	var cEmail = false
	//默认都必须选中 注意:只有检查为true
	var cCheck = true

	//失去焦点的时候校验
	//失去焦点,校验
	oUser.blur(function() {
		//获取用户名
		var tVal = $(this).val()
		//失去焦点的时候找到兄弟span标签
		var oSpan = $(this).siblings('span')
		//判断用户名是否为空
		if(tVal == '') {
			oSpan.show().html('请输入用户名')
			//说明用户名校验失败
			cUser = false
			//为空,结束
			return
		}
		//判断输入是否正确
		//语法: 规则.test(表示值)
		if(reUser.test(tVal)) {
			//匹配成功,隐藏span提示信息
			oSpan.hide()
			//说明校验成功
			cUser = true
		} else {
			//匹配不成功
			oSpan.show().html('请输入数字和字母6-20位')
			//说明校验失败
			cUser = false
			
		}
	})
	
	//密码校验
	oPwd.blur(function(){
		//拿到密码的内容
		var tVal = $(this).val()
		var oSpan = $(this).siblings('span')
		if (tVal=='') {
			oSpan.show().html('请输入密码')
			cPwd = false
			return
		}
		//注意:先输入确认密码,密码会有错
		if (oCpwd!='') {
			//如果确认密码为空,不需要校验
			//如果不为空,需要校验两次密码是否一致
			if (tVal!=oCpwd.val()) {
				cPwd = false
				//不一致,给提示
				oCpwd.siblings('span').show().html('两次密码不一致')
			} else{
				oCpwd.siblings('span').hide()
				cCheck = true
			}
		}
		
		
		
		if (rePass.test(tVal)) {
			//成功
			oSpan.hide()
			cPwd = true
		} else{
			//失败
			oSpan.show().html('请输入密码,6-20位')
			cPwd = false
		}
	})
	
	//确认密码失去焦点
	oCpwd.blur(function(){
		var tVal = $(this).val()
		var oSpan = $(this).siblings('span')
		
		if (tVal=='') {
			oSpan.show().html('请输入确认密码')
			cCpwd = false
			return
		}
		
		//注意:
		//因为确认密码必须和密码保持一致,所以只需要和密码保持一致即可
		//所以只需和密码比较
		if (tVal == oPwd.val()) {
			//说明两个值保持一致
			oSpan.hide()
			cCpwd = true
		} else{
			oSpan.show().html('两次密码不一致')
			cCpwd = false
		}
		
	})
	
	
	//邮箱
	oEmail.blur(function(){
		
		var tVal = $(this).val()
		var oSpan = $(this).siblings('span')
		
		if (tVal=='') {
			oSpan.show().html('请输入邮箱')
			cEmail = false
			return
		}
		
		
		if (reMail.test(tVal)) {
			//说明两个值保持一致
			oSpan.hide()
			cEmail = true
		} else{
			oSpan.show().html('请输入正确的邮箱')
			cEmail = false
		}
		
		
	})
	
	//点击同意协议.这个需要注意不是失去焦点,是点击
	oCheck.blur(function(){
		
		var oSpan = $(this).siblings('span')
		//is(':checked') 专门来判断单选框或者复选框是否被选中.
		if ($(this).is(':checked')) {
			oSpan.hide()
			cCheck = true
			
		}
		 else{
			oSpan.show().html('请同意"美多商城用户使用协议"')
			cCheck = false
		}
		
		
	})
	

	//表单提交
	oForm.submit(function() {
		if(cUser && cPwd && cCpwd && cEmail && cCheck) {
			//为true表示表单校验成功,可以提交
			//允许表单提交
			return true
		} else {
			//false校验失败,不可以提交
			alert('请按照规则填写表单')
			//阻止表单提交
			return false
		}
	})

})