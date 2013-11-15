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

				$("input:radio[name=types1]").click(function(){
					if ($(this).val() == 'choice'){
						processCHFields(1)
					}
					else{
						processOtherFields(1)
					}
				});
				$("input:radio[name=types2]").click(function(){
					if ($(this).val() == 'choice'){
						processCHFields(2)
					}
					else{
						processOtherFields(2)
					}
				});
				$("input:radio[name=types3]").click(function(){
					if ($(this).val() == 'choice'){
						processCHFields(3)
					}
					else{
						processOtherFields(3)
					}
				});					  		
				$("input:radio[name=types4]").click(function(){
					if ($(this).val() == 'choice'){
						processCHFields(4)
					}
					else{
						processOtherFields(4)
					}
				});					  		
				$("input:radio[name=types5]").click(function(){
					if ($(this).val() == 'choice'){
						processCHFields(5)
					}
					else{
						processOtherFields(5)
					}
				});					  		
				$("input:radio[name=types6]").click(function(){
					if ($(this).val() == 'choice'){
						processCHFields(6)
					}
					else{
						processOtherFields(6)
					}
				});					  		
				$("input:radio[name=types7]").click(function(){
					if ($(this).val() == 'choice'){
						processCHFields(7)
					}
					else{
						processOtherFields(7)
					}
				});					  		
				$("input:radio[name=types8]").click(function(){
					if ($(this).val() == 'choice'){
						processCHFields(8)
					}
					else{
						processOtherFields(8)
					}
				});					  		
				$("input:radio[name=types9]").click(function(){
					if ($(this).val() == 'choice'){
						processCHFields(9)
					}
					else{
						processOtherFields(9)
					}
				});					  		
				$("input:radio[name=types10]").click(function(){
					if ($(this).val() == 'choice'){
						processCHFields(10)
					}
					else{
						processOtherFields(10)
					}
				});					  		
	  		});
			function processCHFields(num){
				if (!($("#choices" + num + "div").is(":visible"))){
					$("#choices" + num + "div").show();
					$("#question" + num + "choicesinput").attr("required", true)
				}
			}
			function processOtherFields(num){
				if ($("#choices" + num + "div").is(":visible")){
					$("#choices" + num + "div").hide();
					$("#question" + num + "choicesinput").removeAttr('required');
				}
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
		   					<input name="types1" type="radio" value="true/false" checked="checked">true/false
		   					<br>
		   					<input name="types1" type="radio" value="short answer">short answer
		   					<br>
		   					<input name="types1" type="radio" value="choice">choice
				   		</div>
				   	</div>
				   </div>
				   <div class="form-group">
				   		<label for="question1text" class="col-lg-2 control-label">Q1 Text</label>
				   		<div class="col-lg-10">
				   			<input name="question1text" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group">
				   		<label for="question1answer" class="col-lg-2 control-label">Q1 Answer</label>
				   		<div class="col-lg-10">
				   			<input name="question1answer" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group" id="choices1div" hidden>
				   		<label for="question1choices" class="col-lg-2 control-label">Q1 Choices</label>
				   		<div class="col-lg-10">
				   			<input name="question1choices" type="text" class="form-control" id="question1choicesinput">
				   		</div>
				   </div>
				   <div class="form-group">
				   	<label for="question2" class="col-lg-2 control-label">Q2 Type</label>
				   	<div class="input-group">
				   		<div class="btn-group" data-toggle="buttons-radio">
		   					<input name="types2" type="radio" value="true/false" checked="checked">true/false
		   					<br>
		   					<input name="types2" type="radio" value="short answer">short answer
		   					<br>
		   					<input name="types2" type="radio" value="choice">choice
				   		</div>
				   	</div>
				   <div class="form-group">
				   		<label for="question2text" class="col-lg-2 control-label">Q2 Text</label>
				   		<div class="col-lg-10">
				   			<input name="question2text" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group">
				   		<label for="question2answer" class="col-lg-2 control-label">Q2 Answer</label>
				   		<div class="col-lg-10">
				   			<input name="question2answer" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group" id="choices2div" hidden>
				   		<label for="question2choices" class="col-lg-2 control-label">Q2 Choices</label>
				   		<div class="col-lg-10">
				   			<input name="question2choices" type="text" class="form-control" id="question2choicesinput">
				   		</div>
				   </div>				   
				   </div>
				   <div class="form-group">
				   	<label for="question3" class="col-lg-2 control-label">Q3 Type</label>
				   	<div class="input-group">
				   		<div class="btn-group" data-toggle="buttons-radio">
		   					<input name="types3" type="radio" value="true/false" checked="checked">true/false
		   					<br>
		   					<input name="types3" type="radio" value="short answer">short answer
		   					<br>
		   					<input name="types3" type="radio" value="choice">choice
				   		</div>
				   	</div>
				   </div>
				   <div class="form-group">
				   		<label for="question3text" class="col-lg-2 control-label">Q3 Text</label>
				   		<div class="col-lg-10">
				   			<input name="question3text" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group">
				   		<label for="question3answer" class="col-lg-2 control-label">Q3 Answer</label>
				   		<div class="col-lg-10">
				   			<input name="question3answer" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group" id="choices3div" hidden>
				   		<label for="question3choices" class="col-lg-2 control-label">Q3 Choices</label>
				   		<div class="col-lg-10">
				   			<input name="question3choices" type="text" class="form-control" id="question3choicesinput">
				   		</div>
				   </div>				   
				   <div class="form-group">
				   	<label for="question4" class="col-lg-2 control-label">Q4 Type</label>
				   	<div class="input-group">
				   		<div class="btn-group" data-toggle="buttons-radio">
		   					<input name="types4" type="radio" value="true/false" checked="checked">true/false
		   					<br>
		   					<input name="types4" type="radio" value="short answer">short answer
		   					<br>
		   					<input name="types4" type="radio" value="choice">choice
				   		</div>
				   	</div>
				   </div>
				   <div class="form-group">
				   		<label for="question4text" class="col-lg-2 control-label">Q4 Text</label>
				   		<div class="col-lg-10">
				   			<input name="question4text" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group">
				   		<label for="question4answer" class="col-lg-2 control-label">Q4 Answer</label>
				   		<div class="col-lg-10">
				   			<input name="question4answer" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group" id="choices4div" hidden>
				   		<label for="question4choices" class="col-lg-2 control-label">Q4 Choices</label>
				   		<div class="col-lg-10">
				   			<input name="question4choices" type="text" class="form-control" id="question4choicesinput">
				   		</div>
				   </div>				   
				   <div class="form-group">
				   	<label for="question5" class="col-lg-2 control-label">Q5 Type</label>
				   	<div class="input-group">
				   		<div class="btn-group" data-toggle="buttons-radio">
		   					<input name="types5" type="radio" value="true/false" checked="checked">true/false
		   					<br>
		   					<input name="types5" type="radio" value="short answer">short answer
		   					<br>
		   					<input name="types5" type="radio" value="choice">choice
				   		</div>
				   	</div>
				   </div>
				   <div class="form-group">
				   		<label for="question5text" class="col-lg-2 control-label">Q5 Text</label>
				   		<div class="col-lg-10">
				   			<input name="question5text" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group">
				   		<label for="question5answer" class="col-lg-2 control-label">Q5 Answer</label>
				   		<div class="col-lg-10">
				   			<input name="question5answer" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group" id="choices5div" hidden>
				   		<label for="question5choices" class="col-lg-2 control-label">Q5 Choices</label>
				   		<div class="col-lg-10">
				   			<input name="question5choices" type="text" class="form-control" id="question5choicesinput">
				   		</div>
				   </div>
				   <div class="form-group">
				   	<label for="question6" class="col-lg-2 control-label">Q6 Type</label>
				   	<div class="input-group">
				   		<div class="btn-group" data-toggle="buttons-radio">
		   					<input name="types6" type="radio" value="true/false" checked="checked">true/false
		   					<br>
		   					<input name="types6" type="radio" value="short answer">short answer
		   					<br>
		   					<input name="types6" type="radio" value="choice">choice
				   		</div>
				   	</div>
				   </div>
				   <div class="form-group">
				   		<label for="question6text" class="col-lg-2 control-label">Q6 Text</label>
				   		<div class="col-lg-10">
				   			<input name="question6text" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group">
				   		<label for="question6answer" class="col-lg-2 control-label">Q6 Answer</label>
				   		<div class="col-lg-10">
				   			<input name="question6answer" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group" id="choices6div" hidden>
				   		<label for="question6choices" class="col-lg-2 control-label">Q6 Choices</label>
				   		<div class="col-lg-10">
				   			<input name="question6choices" type="text" class="form-control" id="question6choicesinput">
				   		</div>
				   </div>				   
				   <div class="form-group">
				   	<label for="question7" class="col-lg-2 control-label">Q7 Type</label>
				   	<div class="input-group">
				   		<div class="btn-group" data-toggle="buttons-radio">
		   					<input name="types7" type="radio" value="true/false" checked="checked">true/false
		   					<br>
		   					<input name="types7" type="radio" value="short answer">short answer
		   					<br>
		   					<input name="types7" type="radio" value="choice">choice
				   		</div>
				   	</div>
				   </div>
				   <div class="form-group">
				   		<label for="question7text" class="col-lg-2 control-label">Q7 Text</label>
				   		<div class="col-lg-10">
				   			<input name="question7text" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group">
				   		<label for="question7answer" class="col-lg-2 control-label">Q7 Answer</label>
				   		<div class="col-lg-10">
				   			<input name="question7answer" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group" id="choices7div" hidden>
				   		<label for="question7choices" class="col-lg-2 control-label">Q7 Choices</label>
				   		<div class="col-lg-10">
				   			<input name="question7choices" type="text" class="form-control" id="question7choicesinput">
				   		</div>
				   </div>				   
				   <div class="form-group">
				   	<label for="question8" class="col-lg-2 control-label">Q8 Type</label>
				   	<div class="input-group">
				   		<div class="btn-group" data-toggle="buttons-radio">
		   					<input name="types8" type="radio" value="true/false" checked="checked">true/false
		   					<br>
		   					<input name="types8" type="radio" value="short answer">short answer
		   					<br>
		   					<input name="types8" type="radio" value="choice">choice
				   		</div>
				   	</div>
				   </div>
				   <div class="form-group">
				   		<label for="question8text" class="col-lg-2 control-label">Q8 Text</label>
				   		<div class="col-lg-10">
				   			<input name="question8text" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group">
				   		<label for="question8answer" class="col-lg-2 control-label">Q8 Answer</label>
				   		<div class="col-lg-10">
				   			<input name="question8answer" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group" id="choices8div" hidden>
				   		<label for="question8choices" class="col-lg-2 control-label">Q8 Choices</label>
				   		<div class="col-lg-10">
				   			<input name="question8choices" type="text" class="form-control" id="question8choicesinput">
				   		</div>
				   </div>				   
				   <div class="form-group">
				   	<label for="question9" class="col-lg-2 control-label">Q9 Type</label>
				   	<div class="input-group">
				   		<div class="btn-group" data-toggle="buttons-radio">
		   					<input name="types9" type="radio" value="true/false" checked="checked">true/false
		   					<br>
		   					<input name="types9" type="radio" value="short answer">short answer
		   					<br>
		   					<input name="types9" type="radio" value="choice">choice
				   		</div>
				   	</div>
				   </div>
				   <div class="form-group">
				   		<label for="question9text" class="col-lg-2 control-label">Q9 Text</label>
				   		<div class="col-lg-10">
				   			<input name="question9text" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group">
				   		<label for="question9answer" class="col-lg-2 control-label">Q9 Answer</label>
				   		<div class="col-lg-10">
				   			<input name="question9answer" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group" id="choices9div" hidden>
				   		<label for="question9choices" class="col-lg-2 control-label">Q9 Choices</label>
				   		<div class="col-lg-10">
				   			<input name="question9choices" type="text" class="form-control" id="question9choicesinput">
				   		</div>
				   </div>				   
				   <div class="form-group">
				   	<label for="question10" class="col-lg-2 control-label">Q10 Type</label>
				   	<div class="input-group">
				   		<div class="btn-group" data-toggle="buttons-radio">
		   					<input name="types10" type="radio" value="true/false" checked="checked">true/false
		   					<br>
		   					<input name="types10" type="radio" value="short answer">short answer
		   					<br>
		   					<input name="types10" type="radio" value="choice">choice
				   		</div>
				   	</div>
				   </div>
				   <div class="form-group">
				   		<label for="question10text" class="col-lg-2 control-label">Q10 Text</label>
				   		<div class="col-lg-10">
				   			<input name="question10text" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group">
				   		<label for="question10answer" class="col-lg-2 control-label">Q10 Answer</label>
				   		<div class="col-lg-10">
				   			<input name="question10answer" type="text" class="form-control" required>
				   		</div>
				   </div>
				   <div class="form-group" id="choices10div" hidden>
				   		<label for="question10choices" class="col-lg-2 control-label">Q10 Choices</label>
				   		<div class="col-lg-10">
				   			<input name="question10choices" type="text" class="form-control" id="question10choicesinput">
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