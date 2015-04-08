$(document).ready(function(){
	$(".jquery-image").click(function(){
		$(".jquery-image").animate({opacity: "0.1", left: "+=400"}, 1200)
		.animate({opacity: "0.4", top: "+=160", height: "20", width: "20"}, "slow")
		.animate({opacity: "1", left: "0", height: "100", width: "100"}, "slow")
		.animate({top: "0"}, "fast")
		.slideUp()
		.slideDown("slow")
		.animate({opacity: "1", top: "0", height: "293", width: "500"}, "slow")
		return false;
	});
	$(".replace-text").click(function(){
		$(this).text("Во всемирной паутине HTML-страницы, как правило, передаются браузерам от сервера по протоколам HTTP или HTTPS, в виде простого текста или с использованием сжатия.");
	});
		$(".hide").click(function(){
		$(this).hide();
	});
});
