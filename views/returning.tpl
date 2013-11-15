<html>
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<script src="//code.jquery.com/jquery.js"></script>
		<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap.min.css"/>
	</head>
	<body>
		<div class="jumbotron">
			<div class="container">
				<h2>Welcome</h2>
				<p> Hello {{name}} ({{mbox}}) </p>
				<p><a href="/signout">sign out</a></p>
				<p><a href="/makeqr">Create QR</a/></p>
				% for page in pages:
					<p><a href="/info/{{page.values()[0]}}">{{page.keys()[0]}}</a></p>
				% end
		</div>
		</div>
	</body>
</html>