<html>
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<script src="//code.jquery.com/jquery.js"></script>
		<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css"/>
	<script type="text/javascript">
  		$(document).ready(function(){
  			$('#st1').html("<pre>" + JSON.stringify({{!st1}}, null, 4) + "</pre>"); 		
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
				<p> Thanks for answering!!</p>
				<p id="st1"></p>
				% end
				<p><a href='/'>back</a></p>
		</div>
		</div>
	</body>
</html>