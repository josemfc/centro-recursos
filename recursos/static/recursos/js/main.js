var $ = django.jQuery;

$(document).ready(function(){
	// Mostrar y ocultar
	$("[id^='toggler-container']").hide(0);
	$("[id^='toggler-btn']").on("click", function (e) {
		var str_id = this.id.toString();
		var num = str_id.substr(str_id.length - 1);

		$("#toggler-container"+num).toggle('fast');
	});
});

