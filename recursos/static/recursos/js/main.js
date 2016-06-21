var $ = django.jQuery;

$(document).ready(function(){
	// Secciones
	$('.btn-toggle').click(function(e){
		e.preventDefault();

		var $this_toggle = $(this).parent().find('.toggle');
		$(".toggle").not($this_toggle).hide();				// Si se despliega uno, el resto se oculta
		$(".btn-toggle > i").not($(this).children()).removeClass( "fa-caret-down" ).addClass( "fa-caret-right" );

		$this_toggle.slideToggle();
		var $icono = $(this).parent().find('.btn-toggle > .fa');
		$icono.toggleClass('fa-caret-right fa-caret-down');
	});
	
	// Secciones dentro de secciones
	$('.btn-toggle2').click(function(e){
		e.preventDefault();

		var $this_toggle2 = $(this).parent().find('.toggle2');
		$(".toggle2").not($this_toggle2).hide();
		$(".btn-toggle2 > i").not($(this).children()).removeClass( "fa-angle-down" ).addClass( "fa-angle-right" );

		$this_toggle2.slideToggle();
		var $icono2 = $(this).parent().find('.btn-toggle2 > .fa');
		$icono2.toggleClass('fa-angle-right fa-angle-down');
	});
	
	$('.btn-amarillo').click(function(e){
		$(".pensando").show();
	});
});

