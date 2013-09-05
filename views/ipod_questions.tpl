<head>
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
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
			$.each(data, function(index, value){
				display_value = index + 1
				if (value['type'] != 'short answer'){
					$('#quiz').append('<tr><td>' + display_value + '.</td>' + '<td>' + value['question'] + '</td></tr>');
					$.each(value['answers'], function(i, v){
						$('#quiz').append('<input type="radio" name="' + ('question' + display_value) +'" value="'+ v +'">'+ v +'<br>')
					});
					$('#quiz').append('<input type="hidden" name="' + ('answer' + display_value) + '" value="' + value['correct'] + '">');
				}
				else{
					$('#quiz').append('<tr><td>' + display_value + '.</td>' + '<td>' + value['question'] + '</td><td><input type="text" name="' + ('question' + display_value) + '"></td></tr>');
					$('#quiz').append('<input type="hidden" name="' + ('answer' + display_value) + '" value="' + value['correct'] + '">');
				}
			});
			$('#quiz').append('<input value="Submit when done!" type="submit" />')
		});
	</script>
</head>
<form action="#" method="post" id="quiz">
</form>