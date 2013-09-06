<html>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="//code.jquery.com/jquery.js"></script>
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css"/>
	<script type="text/javascript">
		var data = [
			{'type': 'choice', 'question': 'how many settings does the ipod have?', 'answers': [1, 2, 3, 4], 'correct': 2},
			{'type':'true/false','question': 'True or False, most ipods are white.', 'answers': [true, false], 'correct': true},
			{'type':'true/false','question': 'True or False, this one is white.', 'answers': [true, false], 'correct': false},
			{'type':'choice','question': 'how many GB is this ipod?', 'answers': [16, 32, 80, 120], 'correct': 80},
			{'type': 'choice', 'question': 'how many pictures does the ipod have?', 'answers': [10, 20, 30, 40], 'correct': 40},
			{'type':'true/false','question': 'True or False, most ipods are black.', 'answers': [true, false], 'correct': false},
			{'type':'true/false','question': 'True or False, this one is black.', 'answers': [true, false], 'correct': true},
			{'type':'choice','question': 'how many songs are on this ipod?', 'answers': [1600, 4500, 7000, 120000], 'correct': 4500},
			{'type':'short answer','question': 'Explain why ipod is better than zune.', 'correct': ['zune', 'sucks']},
			{'type':'short answer','question': 'Explain why this ipod is black.', 'correct': ['out', 'of', 'white']}
		];

		$(document).ready(function(){
			var question_list = []
			var rand_array = []
			while(rand_array.length < 5){
				var rand_num = Math.floor(Math.random()*10)
				var found = false
				for(i = 0; i < rand_array.length; i++){
					if(rand_array[i] == rand_num){
						found = true
						break
					}
				}
				if(!found)rand_array[rand_array.length] = rand_num;
			}
			$.each(rand_array, function(index, value){
				question_list.push(data[value]);
			});

			$.each(question_list, function(index, value){
				display_value = index + 1
				$('#fg' + display_value).append('<label for="' + ('question' + display_value) +'">' + display_value + '. ' + value['question'] + '</label>');
				if (value['type'] != 'short answer'){
					$.each(value['answers'], function(i, v){
						$('#fg' + display_value).append('<div class="radio" id="radioDiv' + display_value +'-' + (i + 1) + '"></div>');
						$('#radioDiv' + display_value + '-' + (i + 1)).append('<label><input type="radio" name="' + ('question' + display_value) +'" value="'+ v +'">'+ v +'</label>')
					});
				}
				else{
					$('#fg' + display_value).append('<input class="form-control "type="text" name="' + ('question' + display_value) + '">');
				}
				$('#fg' + display_value).append('<input type="hidden" name="' + ('answer' + display_value) + '" value="' + value['correct'] + '">');
				$('#fg' + display_value).append('<input type="hidden" name="' + ('type' + display_value) + '" value="' + value['type'] + '">');
			});
			$('#buttonDiv').append('<button type="submit" class="btn btn-default" action="#" method="post">Submit</button>')
		});
	</script>
</head>
<body>
    <div class="jumbotron">
		<div class="container">
			<h1>Quiz</h1>
	 		<form action="#" method="post" id="quiz" role="form">
				<div class="form-group" id="fg1">
				</div>
				<div class="form-group" id="fg2">
				</div>
				<div class="form-group" id="fg3">
				</div>
				<div class="form-group" id="fg4">
				</div>
				<div class="form-group" id="fg5">
				</div>
				<div class="form-group">
					<div class="col-lg-offset-2 col-lg-10" id="buttonDiv">
					</div>
				</div>															
			</form> 
		</div>	
</div>
<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
</body>
</html>