<html>
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<script src="//code.jquery.com/jquery.js"></script>
		<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap.min.css"/>
	</head>
	<body>
		<div class="jumbotron">
			<div class="container">
				<h2>Register</h2>
				<p> You are not signed in. Please enter an email address and name to record your actions </p>
				<form action="/home" method="post" role="form" class="form-horizontal">
				   <div class="form-group">
				   	<label for="mbox" class="col-lg-2 control-label">Email</label>
				   	<div class="col-lg-10">
				   		<input name="mbox" type="email" class="form-control" placeholder="Enter email" required>
				   	</div>
				   </div>
				   <div class="form-group">
				   	<label for="name" class="col-lg-2 control-label">Name</label>
				   	<div class="col-lg-10">
				   		<input name="name" type="text" class="form-control" placeholder="Enter name" required>
				   	</div>
				   </div>
				   <div class="form-group">
				   	<div class="col-lg-offset-2 col-lg-10">
				   		<button type="submit" class="btn btn-default">Register</button>
				   	</div>
				   </div>				   		
				</form>
		</div>
		</div>
	</body>
</html>