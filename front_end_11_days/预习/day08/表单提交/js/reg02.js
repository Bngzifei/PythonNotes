$(function(){
	var $user = $('#user_name');
	var reUser = /^\w{6,20}$/;
	
	var userCheck = false;
	
	$user.blur(function(){
		
		var tVal = $(this).val();
		var tNext = $(this).next();
		
		if( tVal == '' ){
			tNext.html('请输入内容').show();
			return;
		}
		
		if(reUser.test( tVal )){
			tNext.hide();
			userCheck = true;
		}else{
			tNext.html('请输入数字字母或下划线6到20位').show();
		}
		
	}).click(function(){
		$(this).next().hide();
	})
	
	$('#allow').click(function(){
		if($(this).is(':checked') == true){
			
		}else{
			$(this).next().next().html('请同意协议');
		}
	})
	
	$('form').submit(function(){
		
		if(userCheck == true){
			return true;
		}else{
			alert('请正确输入信息');
			return false;
		}
		
	})
	
	
})
