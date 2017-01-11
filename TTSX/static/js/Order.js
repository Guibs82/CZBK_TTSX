$(function(){
	div = $('#loop');
	div.delegate('a', 'click', function(event) {					
			text = $(this).text()
			num = $('#loop1').prop("name");
			if(text == '<上一页'){
				nums = parseInt(num)-1
				if(nums == 0){
					nums = 1
				}
			}
			else if(text == '下一页>'){
				nums = parseInt(num) +1
			}
			else{
				nums = text
			};
			$(this).attr({href:'/orderInfo/'+nums+'/'});
  });
  num1 = $('#loop1').prop("name");
  $('#loop a').eq(num1).addClass('active').siblings().removeClass('active');

});
