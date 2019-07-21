;(function(){
	
	$(function(){
		//保存选择器
		var oUser = $('#user_name')
		var oPwd = $('#pwd')
		var oCpwd = $('#cpwd')
		var oEmail = $('#email')
		var oCheck = $('#allow')
		var oForm = $('form')
		
		//保存正则规则
		var reUser = /^\w{6,20}$/
		var rePass = /^[\w!@#$%^&*]{6,20}$/
		var reMail = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/i;
		
		
		//保存能够让form表单提交的变量. 开关
		var cUser = false
		var cCheck = true
		var cPwd = false
		var cCpwd = false
		var cMail = false
		
		
		oUser.blur(function(){
			var tVal = $(this).val()
			var oSpan = $(this).siblings('span')
			//判断用户输入的内容不能为空
			if(tVal == ''){
				//不符合时，让开关变为false。提交表单就不会提交了
				cUser = false
				oSpan.show().html('内容不能为空')
				return
			}
			
			//检验用户输入的内容是否符合我的条件
			if(reUser.test( tVal )){
				oSpan.hide()
				cUser = true
			}else{
				//.show()显示     .hide()隐藏 
				cUser = false
				oSpan.show().html('请输入数字字母或下划线6到20位')
			}
			
		})
		
		oPwd.blur(function(){
			var tVal = $(this).val()
			var oSpan = $(this).siblings('span')
			if(tVal == ''){
				cPwd = false
				oSpan.show().html('内容不能为空')
				return
			}
			
			//当确认密码的内容不为空的时候，再加那个密码不一致的判断
			if(oCpwd.val() != ''){
				if(tVal != oCpwd.val()){
					
					oCpwd.siblings('span').show().html('两次输入的密码不一致')
//					cPwd = false
					cCpwd = false
					
				}else{
//					cPwd = true
					cCpwd = true
					oCpwd.siblings('span').hide()
				}
			}
			
			if(rePass.test( tVal )){
				oSpan.hide()
				cPwd = true
			}else{
				//.show()显示     .hide()隐藏 
				cPwd = false
				oSpan.show().html('请输入6-20位密码')
			}
			
		})
		
		oCpwd.blur(function(){
			var tVal = $(this).val()
			var oSpan = $(this).siblings('span')
			if(tVal == ''){
				cCpwd = false
				oSpan.show().html('内容不能为空')
				return
			}
			
			if(tVal == oPwd.val()){
				oSpan.hide()
				cCpwd = true
			}else{
				oSpan.show().html('两次输入的密码不一致')
				cCpwd = false
			}
			
		})
		
		oEmail.blur(function(){
			var tVal = $(this).val()
			var oSpan = $(this).siblings('span')
			
			if(tVal == ''){
				cMail = false
				oSpan.show().html('内容不能为空')
				return
			}
			
			if(reMail.test( tVal )){
				oSpan.hide()
				cMail = true
			}else{
				cMail = false
				oSpan.show().html('请输入正确的邮箱格式')
			}
			
		})
		
		//判断多选框
		oCheck.click(function(){
			var oSpan = $(this).siblings('span')
			//$(this).is(':checked')  专门判断多选框是否被选中
			if($(this).is(':checked')){
				//选中执行的程序
				oSpan.hide()
				cCheck = true
			}else{
				//不选中执行的程序
				oSpan.show().html('请勾选上同意协议')
				cCheck = false
			}
			
		})
		
		//提交表单事件，要选择form标签去提交而不是submit类型表单
		oForm.submit(function(){
			//要根据上面用户输入的内容，全都正确才能提交   return true提交。return false不提交
//			console.log('a:' + cUser + 'b:' + cCheck + 'c:' + cPwd + 'd:' + cCpwd + 'e:' + cMail)
			if(cUser  &&  cCheck  && cPwd && cCpwd && cMail){
				return true
			}else{
				alert('请输入完整的信息')
				return false
			}
		})
	})
	
})()
