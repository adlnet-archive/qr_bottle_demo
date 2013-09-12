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
				<p> Thanks for taking the quiz!! You scored {{score}} out of 5</p>
				% if score > 3:
				<p style="color:green">Congratulations! You passed the quiz!</p>
				% else:
				<p style="color:red">Sorry, you failed the quiz. Study harder next time</p>
				% end
				<p>{{st1}}</p>
				<p>{{st2}}</p>
				<p>{{st3}}</p>
				<p>{{st4}}</p>
				<p>{{st5}}</p>
				<p>{{st6}}</p>
				<p>{{st7}}</p>
				% end
				<p><a href='/info/{{partname}}'>info</a></p>
		</div>
		</div>
	</body>
</html>