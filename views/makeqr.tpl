<html>
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<script src="//code.jquery.com/jquery.js"></script>
		<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css"/>
	</head>
	<body>
		<div class="jumbotron">
			<div class="container">
				<h2>Enter data for QR code</h2>
				<form action="/makeqr" method="post" role="form" class="form-horizontal">
				   <div class="form-group">
				   	<label for="name" class="col-lg-2 control-label">Name</label>
				   	<div class="col-lg-10">
				   		<input name="name" type="text" class="form-control">
				   	</div>
				   </div>
				   <div class="form-group">
				   	<label for="info" class="col-lg-2 control-label">Info</label>
				   	<div class="col-lg-10">
				   		<textarea rows="5" name="info" class="form-control"></textarea>
				   	</div>
				   </div>
				   <div class="form-group">
				   	<label for="instructions" class="col-lg-2 control-label">Instructions</label>
				   	<div class="col-lg-10">
				   		<textarea rows="5" name="instructions" class="form-control"></textarea>
				   	</div>
				   </div>
				   <div class="form-group">
				   	<div class="col-lg-offset-2 col-lg-10">
				   		<button type="submit" class="btn btn-default">Create</button>
				   	</div>
				   </div>				
				</form>
				<a href='/'>Home</a>
		</div>
		</div>
	</body>
</html>