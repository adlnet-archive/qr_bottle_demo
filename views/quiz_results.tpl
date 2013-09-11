<html>
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<script src="//code.jquery.com/jquery.js"></script>
		<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css"/>
	</head>
	<body>
		<div class="jumbotron">
			<div class="container">
				<h2>Results</h2>
				% if status != 200:
				<p>Something went wrong with POSTing the quiz results to the LRS.</p>
				<p>{{status}} - {{content}}</p>
				% else:
				<p> Thanks for taking the quiz!! View your results on the LRS!</p>
				% for c in content:
				<li>ID - {{c}}</li>
				% end
				<p><a href='/info/{{partname}}'>info</a></p>
		</div>
		</div>
	</body>
</html>