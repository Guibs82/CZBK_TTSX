$(function(){
	Order = $('#Order').text();
	res=Order.split('元', 1);
	// toFixed()是保留两位小数的意思
	nums = (parseFloat(res)+10).toFixed(2)

	Orders = $('#Orders').text(nums+'元');
});