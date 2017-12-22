196.71.52.225

<html>
<head>
<title>Quiz</title>
<script>
        function verify(form){
                var myXMLHttp = new XMLHttpRequest();
                //var rep = document.getElementById('choice').value;
		var reps = document.getElementsByName('choice'); 
		var rep;
		for(var i = 0; i < reps.length; i++){
			if(reps[i].checked){
				rep = reps[i].value; break; 
			} 
		}
		var cor = document.getElementById('correct').value;
		var uri="/cgi-bin/wbalbal/correct.py";
		myXMLHttp.open("POST", uri , false);
                myXMLHttp.send("rep="+rep+"&cor="+cor);
                document.getElementById("result").innerHTML = myXMLHttp.responseText;
		if(document.getElementById("result").innerHTML[0]=="t"){
			//document.getElementById("score").value = "123"
			document.getElementById("score").value = parseInt(document.getElementById('score').value)+1;
			document.getElementById("result").innerHTML = "Reponse Correct";
		}else{
			document.getElementById("result").innerHTML = "Reponse False<br/> Reponse correcte"+document.getElementById('correct').value;
		}
		//alert(document.getElementById("result").innerHTML[0]);
		stopWorker();
		form.disabled = true;
		document.getElementById("next").disabled = false;
        }
	var w;
	var mySwitch=0;
            function startWorker() {
                if(typeof(Worker) != "undefined") {
                    w = new Worker("/~wbalbal/compteur1.js");
                    w.onmessage = function(e) { 
			if(parseInt(e.data)>=0) //--le du timer
	                    document.getElementById("timer").innerHTML = e.data;
			else{ //si timer arrive à 0 i switch disable entre verify <->next :)
			    document.getElementById("verify").disabled = true;
			    document.getElementById("next").disabled = false;
			    if(document.getElementById("result").innerHTML[0]!='R'){
				document.getElementById("result").innerHTML="Temps ecoulé <br/>Correction : "
					+document.getElementById('correct').value;
			    }
			}

			//decorataion du timer
			if(e.data<6 && e.data>=0){
			    document.getElementById("timerP").style.color = "Red";
			    var div = document.getElementById("timerP");
		            var currentFont = div.style.fontSize.replace("px", "");
			    if(mySwitch==0){
				//div.style.fontSize = 0*parseInt(currentFont) + parseInt(17) + "px";
				div.style.color = "DarkOrange";
				mySwitch = 1; //rj3
			    }else{
				//div.style.fontSize = parseInt(currentFont) - parseInt(5) + "px";
				div.style.color= "Red";
				mySwitch = 0;
			    }
//			    div.style.fontSize = parseInt(currentFont) + parseInt(2) + "px";
			}
                    };
                
                } else {
                    document.getElementById("timer").innerHTML = "srry ur browser is too old";
                }
            }
        
        function stopWorker() { 
            w.terminate();
        }
</script>
</head>
<body onload="startWorker()">

<h2>quiz1</h2>
<div id="timerP" style="position: absolute;font-size:16px;"><p>Il vous reste encore : <output id="timer"></output> secondes</p></div>
<br/><br/><br/>
score =  0

	    <script>
		window.location = "./gameover.py?score= 0 "
	    </script>
	
</body></html>
