<html>
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<script src="//code.jquery.com/jquery.js"></script>
		<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css"/>
		<script type="text/javascript">
	  		$(document).ready(function(){
		        $('#st1').html("<pre>" + JSON.stringify({{!st1}}, null, 4) + "</pre>");
		        $('#st2').html("<pre>" + JSON.stringify({{!st2}}, null, 4) + "</pre>");
		        $('#st3').html("<pre>" + JSON.stringify({{!st3}}, null, 4) + "</pre>");
		        $('#st4').html("<pre>" + JSON.stringify({{!st4}}, null, 4) + "</pre>");
		        $('#st5').html("<pre>" + JSON.stringify({{!st5}}, null, 4) + "</pre>");
		        $('#st6').html("<pre>" + JSON.stringify({{!st6}}, null, 4) + "</pre>");
		        $('#st7').html("<pre>" + JSON.stringify({{!st7}}, null, 4) + "</pre>");
	  		});
	  	</script>
	</head>
	<body>
		<div class="jumbotron">
			<div class="container">
				<h2>Results</h2>
                % if status != 200:
            	<p>Something went wrong with POSTing the quiz results to the LRS.</p>
            	<p>{{status}} - {{content}}</p>
                % else:
            	<p> Thanks for taking the quiz!! You scored {{score}} out of 5</p>
                % if score > 3:
            	<p style="color:green">Congratulations! You passed the quiz!</p>
                % else:
            	<p style="color:red">Sorry, you failed the quiz. Study harder next time</p>
                % end
                <p id="st1"></p>
                <p id="st2"></p>
                <p id="st3"></p>
                <p id="st4"></p>
                <p id="st5"></p>
                <p id="st6"></p>
                <p id="st7"></p>
                % end
            	<p><a href='/info/{{partname}}'>info</a></p>
			</div>
		</div>
	</body>
</html>