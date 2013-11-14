<html>
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<script src="//code.jquery.com/jquery.js"></script>
		<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap.min.css"/>
		<script type="text/javascript">
	  		$(document).ready(function(){
				$("#createform").hide();
				$("#target").submit(function( event ) {
					if ($("#passwordbox").val() == '{{pw}}'){			 				  	
						$("#createform").show();
						$("#passwordform").hide();			
					}
					else{
						alert("Wrong-try again.")
					}
				  	event.preventDefault();
				});

				//make sure on initial load boxes are checked and displaying inputs
				for (i=1; i<11; i++){
					processCHFields(i)
				}

				$("input:radio[name=types1]").click(function(){
					var q_type = $(this).val()
					switch (q_type){
						case 'choice':
							processCHFields(1)
							break;
						case 'true/false':
							processTFFields(1)
							break;
						case 'short answer':
							processSAFields(1)
							break;
					}
				});
				$("input:radio[name=types2]").click(function(){
					var q_type = $(this).val()
					switch (q_type){
						case 'choice':
							processCHFields(2)
							break;
						case 'true/false':
							processTFFields(2)
							break;
						case 'short answer':
							processSAFields(2)
							break;
					}
				});
				$("input:radio[name=types3]").click(function(){
					var q_type = $(this).val()
					switch (q_type){
						case 'choice':
							processCHFields(3)
							break;
						case 'true/false':
							processTFFields(3)
							break;
						case 'short answer':
							processSAFields(3)
							break;
					}
				});					  		
				$("input:radio[name=types4]").click(function(){
					var q_type = $(this).val()
					switch (q_type){
						case 'choice':
							processCHFields(4)
							break;
						case 'true/false':
							processTFFields(4)
							break;
						case 'short answer':
							processSAFields(4)
							break;
					}
				});					  		
				$("input:radio[name=types5]").click(function(){
					var q_type = $(this).val()
					switch (q_type){
						case 'choice':
							processCHFields(5)
							break;
						case 'true/false':
							processTFFields(5)
							break;
						case 'short answer':
							processSAFields(5)
							break;
					}
				});					  		
				$("input:radio[name=types6]").click(function(){
					var q_type = $(this).val()
					switch (q_type){
						case 'choice':
							processCHFields(6)
							break;
						case 'true/false':
							processTFFields(6)
							break;
						case 'short answer':
							processSAFields(6)
							break;
					}
				});					  		
				$("input:radio[name=types7]").click(function(){
					var q_type = $(this).val()
					switch (q_type){
						case 'choice':
							processCHFields(7)
							break;
						case 'true/false':
							processTFFields(7)
							break;
						case 'short answer':
							processSAFields(7)
							break;
					}
				});					  		
				$("input:radio[name=types8]").click(function(){
					var q_type = $(this).val()
					switch (q_type){
						case 'choice':
							processCHFields(8)
							break;
						case 'true/false':
							processTFFields(8)
							break;
						case 'short answer':
							processSAFields(8)
							break;
					}
				});					  		
				$("input:radio[name=types9]").click(function(){
					var q_type = $(this).val()
					switch (q_type){
						case 'choice':
							processCHFields(9)
							break;
						case 'true/false':
							processTFFields(9)
							break;
						case 'short answer':
							processSAFields(9)
							break;
					}
				});					  		
				$("input:radio[name=types10]").click(function(){
					var q_type = $(this).val()
					switch (q_type){
						case 'choice':
							processCHFields(10)
							break;
						case 'true/false':
							processTFFields(10)
							break;
						case 'short answer':
							processSAFields(10)
							break;
					}
				});					  		
	  		});
			
			function processCHFields(num){
				$("#question" + num + "tfgroup").hide();
				$("#question" + num + "sagroup").hide();
				$("#question" + num + "chgroup").html('')
				$("#question" + num + "chgroup").append('<div class="form-group"><label for="' + ('question' + num + 'text') + '" class="col-lg-2 control-label">Q' + num + ' Text</label><div class="col-lg-10"><input name="' + ('question' + num + 'text') + '" type="text" class="form-control"></div></div')
				$("#question" + num + "chgroup").append('<div class="form-group"><label for="' + ('question' + num + 'choices') + '" class="col-lg-2 control-label">Q' + num + ' Choices</label><div class="col-lg-10"><input name="' + ('question' + num + 'choices') + '" type="text" class="form-control"></div></div>')
				$("#question" + num + "chgroup").append('<div class="form-group"><label for="' + ('question' + num + 'answer') + '" class="col-lg-2 control-label">Q' + num + ' Answer</label><div class="col-lg-10"><input name="' + ('question' + num + 'answer') + '" type="text" class="form-control"></div></div>')
				$("#question" + num + "chgroup").show()
			}
			function processTFFields(num){
				$("#question" + num + "chgroup").hide();
				$("#question" + num + "sagroup").hide();
				$("#question" + num + "tfgroup").html('')
				$("#question" + num + "tfgroup").append('<div class="form-group"><label for="' + ('question' + num + 'text') + '" class="col-lg-2 control-label">Q' + num + ' Text</label><div class="col-lg-10"><input name="' + ('question' + num + 'text') + '" type="text" class="form-control"></div></div>')
				$("#question" + num + "tfgroup").append('<div class="form-group"><label for="' + ('question' + num + 'answer') + '" class="col-lg-2 control-label">Q' + num + ' Answer</label><div class="col-lg-10"><input name="' + ('question' + num + 'answer') + '" type="text" class="form-control"></div></div>')
				$("#question" + num + "tfgroup").show()
			}
			function processSAFields(num){
				$("#question" + num + "tfgroup").hide();
				$("#question" + num + "chgroup").hide();
				$("#question" + num + "sagroup").html('')
				$("#question" + num + "sagroup").append('<div class="form-group"><label for="' + ('question' + num + 'text') + '" class="col-lg-2 control-label">Q' + num + ' Text</label><div class="col-lg-10"><input name="' + ('question' + num + 'text') + '" type="text" class="form-control"></div></div>')
				$("#question" + num + "sagroup").append('<div class="form-group"><label for="' + ('question' + num + 'answer') + '" class="col-lg-2 control-label">Q' + num + ' Answer</label><div class="col-lg-10"><input name="' + ('question' + num + 'answer') + '" type="text" class="form-control"></div></div>')
				$("#question" + num + "sagroup").show()
			}
  		</script>
	</head>
	<body>
		<div class="jumbotron">
			<div id="passwordform" title="Enter a password" class="container">
				<form id="target" action="" class="form-horizontal">
					<div class="form-group">
						<label for="name" class="col-lg-2 control-label">Password</label>
					   	<div class="col-lg-10">
					   		<input id="passwordbox" type="password" class="form-control">
					   	</div>
					</div>  				
				   <div class="form-group">
				   	<div class="col-lg-offset-2 col-lg-10">
				   		<button type="submit" class="btn btn-default">Go</button>
				   	</div>
				   </div>
				</form>
			</div>
			<div class="container" id="createform">
				<h2>Enter data for QR code</h2>
				<form action="/makeqr" method="post" role="form" class="form-horizontal" id="qrform">
				   <div class="form-group">
				   	<label for="name" class="col-lg-2 control-label">Name</label>
				   	<div class="col-lg-10">
				   		<input name="name" type="text" class="form-control" required>
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
				   	<label for="question1" class="col-lg-2 control-label">Q1 Type</label>
				   	<div class="input-group">
				   		<div class="btn-group" data-toggle="buttons-radio">
		   					<input name="types1" type="radio" value="choice" checked="checked">choice
		   					<br>
		   					<input name="types1" type="radio" value="true/false">true/false
		   					<br>
		   					<input name="types1" type="radio" value="short answer">short answer
				   		</div>
				   	</div>
				   </div>
				   <div class="form-group" id="question1chgroup" style="display: block;"></div>
				   <div class="form-group" id="question1tfgroup"></div>
				   <div class="form-group" id="question1sagroup"></div>
				   <div class="form-group">
				   	<label for="question2" class="col-lg-2 control-label">Q2 Type</label>
				   	<div class="input-group">
				   		<div class="btn-group" data-toggle="buttons-radio">
		   					<input name="types2" type="radio" value="choice" checked="checked">choice
		   					<br>
		   					<input name="types2" type="radio" value="true/false">true/false
		   					<br>
		   					<input name="types2" type="radio" value="short answer">short answer
				   		</div>
				   	</div>
				   </div>				   
				   <div class="form-group" id="question2chgroup" style="display: block;"></div>
				   <div class="form-group" id="question2tfgroup"></div>
				   <div class="form-group" id="question2sagroup"></div>
				   <div class="form-group">
				   	<label for="question3" class="col-lg-2 control-label">Q3 Type</label>
				   	<div class="input-group">
				   		<div class="btn-group" data-toggle="buttons-radio">
		   					<input name="types3" type="radio" value="choice" checked="checked">choice
		   					<br>
		   					<input name="types3" type="radio" value="true/false">true/false
		   					<br>
		   					<input name="types3" type="radio" value="short answer">short answer
				   		</div>
				   	</div>
				   </div>				   
				   <div class="form-group" id="question3chgroup" style="display: block;"></div>
				   <div class="form-group" id="question3tfgroup"></div>
				   <div class="form-group" id="question3sagroup"></div>
				   <div class="form-group">
				   	<label for="question4" class="col-lg-2 control-label">Q4 Type</label>
				   	<div class="input-group">
				   		<div class="btn-group" data-toggle="buttons-radio">
		   					<input name="types4" type="radio" value="choice" checked="checked">choice
		   					<br>
		   					<input name="types4" type="radio" value="true/false">true/false
		   					<br>
		   					<input name="types4" type="radio" value="short answer">short answer
				   		</div>
				   	</div>
				   </div>				   
				   <div class="form-group" id="question4chgroup" style="display: block;"></div>
				   <div class="form-group" id="question4tfgroup"></div>
				   <div class="form-group" id="question4sagroup"></div>
				   <div class="form-group">
				   	<label for="question5" class="col-lg-2 control-label">Q5 Type</label>
				   	<div class="input-group">
				   		<div class="btn-group" data-toggle="buttons-radio">
		   					<input name="types5" type="radio" value="choice" checked="checked">choice
		   					<br>
		   					<input name="types5" type="radio" value="true/false">true/false
		   					<br>
		   					<input name="types5" type="radio" value="short answer">short answer
				   		</div>
				   	</div>
				   </div>				   
				   <div class="form-group" id="question5chgroup" style="display: block;"></div>
				   <div class="form-group" id="question5tfgroup"></div>
				   <div class="form-group" id="question5sagroup"></div>
				   <div class="form-group">
				   	<label for="question6" class="col-lg-2 control-label">Q6 Type</label>
				   	<div class="input-group">
				   		<div class="btn-group" data-toggle="buttons-radio">
		   					<input name="types6" type="radio" value="choice" checked="checked">choice
		   					<br>
		   					<input name="types6" type="radio" value="true/false">true/false
		   					<br>
		   					<input name="types6" type="radio" value="short answer">short answer
				   		</div>
				   	</div>
				   </div>				   
				   <div class="form-group" id="question6chgroup" style="display: block;"></div>
				   <div class="form-group" id="question6tfgroup"></div>
				   <div class="form-group" id="question6sagroup"></div>
				   <div class="form-group">
				   	<label for="question7" class="col-lg-2 control-label">Q7 Type</label>
				   	<div class="input-group">
				   		<div class="btn-group" data-toggle="buttons-radio">
		   					<input name="types7" type="radio" value="choice" checked="checked">choice
		   					<br>
		   					<input name="types7" type="radio" value="true/false">true/false
		   					<br>
		   					<input name="types7" type="radio" value="short answer">short answer
				   		</div>
				   	</div>
				   </div>				   
				   <div class="form-group" id="question7chgroup" style="display: block;"></div>
				   <div class="form-group" id="question7tfgroup"></div>
				   <div class="form-group" id="question7sagroup"></div>
				   <div class="form-group">
				   	<label for="question8" class="col-lg-2 control-label">Q8 Type</label>
				   	<div class="input-group">
				   		<div class="btn-group" data-toggle="buttons-radio">
		   					<input name="types8" type="radio" value="choice" checked="checked">choice
		   					<br>
		   					<input name="types8" type="radio" value="true/false">true/false
		   					<br>
		   					<input name="types8" type="radio" value="short answer">short answer
				   		</div>
				   	</div>
				   </div>				   
				   <div class="form-group" id="question8chgroup" style="display: block;"></div>
				   <div class="form-group" id="question8tfgroup"></div>
				   <div class="form-group" id="question8sagroup"></div>
				   <div class="form-group">
				   	<label for="question9" class="col-lg-2 control-label">Q9 Type</label>
				   	<div class="input-group">
				   		<div class="btn-group" data-toggle="buttons-radio">
		   					<input name="types9" type="radio" value="choice" checked="checked">choice
		   					<br>
		   					<input name="types9" type="radio" value="true/false">true/false
		   					<br>
		   					<input name="types9" type="radio" value="short answer">short answer
				   		</div>
				   	</div>
				   </div>				   
				   <div class="form-group" id="question9chgroup" style="display: block;"></div>
				   <div class="form-group" id="question9tfgroup"></div>
				   <div class="form-group" id="question9sagroup"></div>
				   <div class="form-group">
				   	<label for="question10" class="col-lg-2 control-label">Q10 Type</label>
				   	<div class="input-group">
				   		<div class="btn-group" data-toggle="buttons-radio">
		   					<input name="types10" type="radio" value="choice" checked="checked">choice
		   					<br>
		   					<input name="types10" type="radio" value="true/false">true/false
		   					<br>
		   					<input name="types10" type="radio" value="short answer">short answer
				   		</div>
				   	</div>
				   </div>				   
				   <div class="form-group" id="question10chgroup" style="display: block;"></div>
				   <div class="form-group" id="question10tfgroup"></div>
				   <div class="form-group" id="question10sagroup"></div>
				   
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