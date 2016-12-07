var url = window.location;
console.log(url);

var hashId = url.hash;
console.log(hashId);


var $listEstabelecimento = $(".lista-category");
var $teste = $("a"+hashId);
if(hashId){
	console.log("Possui um hash");
	
	// if($("body").find(hashId)){
	// 	$teste.on("click", function(){
	// 		console.log("forcei o evento do click")
	// 	});

	// 	$teste.trigger("click");
	// }
}