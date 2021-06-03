
$(document).ready(function(){
  $(".btn").click(function(){
  	$.ajax({
  		url:'hasianda:choosefarm',
  		type: 'get',
  		data: {
  			button_text: $(this).text()
  		},
  		success: function(response){
  			$(".btn").text(response.seconds)
  		}
  	})
  })

  })
  