$( document ).ready(function() {

	$(".confirm-delete").on("click", function(){
		return confirm('Are you sure you want to delete this?');
	})
});