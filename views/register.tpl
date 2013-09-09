<html>
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<script src="//code.jquery.com/jquery.js"></script>
		<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css"/>
	</head>
	<body>
		<div class="jumbotron">
			<div class="container">
				<h2>Register</h2>
				<p> You are not signed in. Please enter an email address to record your actions </p>
				<form action="/register" method="post" role="form" class="form-horizontal">
				   <div class="form-group">
				   	<label for="mbox" class="col-lg-2 control-label">Name</label>
				   	<div class="col-lg-10">
				   		<input name="mbox" type="email" class="form-control" placeholder="Enter email">
				   	</div>
				   </div>
				   <div class="form-group">
				   	<div class="col-lg-offset-2 col-lg-10">
				   		<button type="submit" class="btn btn-default">Register</button>
				   	</div>
				   </div>				   		
				</form>
				<a href='/'>Home</a>
		</div>
		</div>
	</body>
</html>