<html>
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
	    <script src="//code.jquery.com/jquery.js"></script>
	    <script src="//netdna.bootstrapcdn.com/bootstrap/3.0.2/js/bootstrap.min.js"></script>
	    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap.min.css"/>
		<script type="text/javascript">
	  		$(document).ready(function(){
				$.each({{!stmts}}, function(index, value){
					display_value = index + 1
					//Needed b/c of funky encoding when passing data
					value_obj = JSON.parse(value)
	  				$('#st' + display_value).html("<pre>" + JSON.stringify(value_obj, null, 4) + "</pre>");						
				});
				$.each({{!sens}}, function(index, value){
					display_value = index + 1
	  				$('#sen' + display_value).html(value);						
				});
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
				<div class="panel-group" id="accordion">
				  <div class="panel panel-default">
				    <div class="panel-heading">
				      <h4 class="panel-title">
				        <a data-toggle="collapse" data-parent="#accordion" href="#collapseOne" id="sen1">
				          
				        </a>
				      </h4>
				    </div>
				    <div id="collapseOne" class="panel-collapse collapse in">
				      <div class="panel-body" id="st1">
				        
				      </div>
				    </div>
				  </div>
				  <div class="panel panel-default">
				    <div class="panel-heading">
				      <h4 class="panel-title">
				        <a data-toggle="collapse" data-parent="#accordion" href="#collapseTwo" id="sen2">
				          
				        </a>
				      </h4>
				    </div>
				    <div id="collapseTwo" class="panel-collapse collapse">
				      <div class="panel-body" id="st2">
				        
				      </div>
				    </div>
				  </div>
				  <div class="panel panel-default">
				    <div class="panel-heading">
				      <h4 class="panel-title">
				        <a data-toggle="collapse" data-parent="#accordion" href="#collapseThree" id="sen3">
				          
				        </a>
				      </h4>
				    </div>
				    <div id="collapseThree" class="panel-collapse collapse">
				      <div class="panel-body" id="st3">
				        
				      </div>
				    </div>
				  </div>
				  <div class="panel panel-default">
				    <div class="panel-heading">
				      <h4 class="panel-title">
				        <a data-toggle="collapse" data-parent="#accordion" href="#collapseFour" id="sen4">
				          
				        </a>
				      </h4>
				    </div>
				    <div id="collapseFour" class="panel-collapse collapse">
				      <div class="panel-body" id="st4">
				        
				      </div>
				    </div>
				  </div>
				  <div class="panel panel-default">
				    <div class="panel-heading">
				      <h4 class="panel-title">
				        <a data-toggle="collapse" data-parent="#accordion" href="#collapseFive" id="sen5">
				          
				        </a>
				      </h4>
				    </div>
				    <div id="collapseFive" class="panel-collapse collapse">
				      <div class="panel-body" id="st5">
				        
				      </div>
				    </div>
				  </div>
				  <div class="panel panel-default">
				    <div class="panel-heading">
				      <h4 class="panel-title">
				        <a data-toggle="collapse" data-parent="#accordion" href="#collapseSix" id="sen6">
				          
				        </a>
				      </h4>
				    </div>
				    <div id="collapseSix" class="panel-collapse collapse">
				      <div class="panel-body" id="st6">
				        
				      </div>
				    </div>
				  </div>
				  <div class="panel panel-default">
				    <div class="panel-heading">
				      <h4 class="panel-title">
				        <a data-toggle="collapse" data-parent="#accordion" href="#collapseSeven" id="sen7">
				          
				        </a>
				      </h4>
				    </div>
				    <div id="collapseSeven" class="panel-collapse collapse">
				      <div class="panel-body" id="st7">				        
				      </div>
				    </div>
				  </div>
				</div>
			</div>
                % end
            	<p><a href='/info/{{partname}}'>info</a></p>


		</div>
	</body>
</html>