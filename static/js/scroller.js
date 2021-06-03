

// A $( document ).ready() block.
$( document ).ready(function() {

function hideFormDefault(second,third,backbtn){
	second.style.display = "none";
	third.style.display = "none";
	backbtn.style.display = "none";
}

function decideCalved(){
	
	//alert(" still here");
	var wasanimalcalved = document.getElementsByName("calved");

	for (var i = 0; i < wasanimalcalved.length; i++) {
		if(wasanimalcalved[i].checked){
			wasanimalcalved = wasanimalcalved[i];
			return wasanimalcalved.value;
		}
	}
	
}

function nextForm(){
	var check = decideCalved();
		if (check == "calved") 
		{
			document.getElementById("firstform").style.display = "none";
			document.getElementById("thirdform").style.display = "block";
			document.getElementById("backBtn").style.display = "block";

		}
		else{
			document.getElementById("firstform").style.display = "none";
			document.getElementById("secondform").style.display = "block";
			document.getElementById("backBtn").style.display = "block";
		}
}

function backForm(){

	var check = decideCalved();
	if (check == "calved") {
		    document.getElementById("firstform").style.display = "block";
			document.getElementById("thirdform").style.display = "none";
			document.getElementById("backBtn").style.display = "none";

	}else{
	    	document.getElementById("firstform").style.display = "block";
			document.getElementById("secondform").style.display = "none";
			document.getElementById("backBtn").style.display = "none";

	}
}

$("#nextBtn").click(nextForm);
$("#backBtn").click(backForm);

hideFormDefault(document.getElementById("secondform"),document.getElementById("thirdform"),document.getElementById("backBtn"));

});