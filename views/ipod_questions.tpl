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

		function validateSubmit(obj){
			var err = '';
			answer1 = data[0]['correct']
			answer2 = data[1]['correct'].toString();
			answer3 = data[2]['correct'].toString();
			answer4 = data[3]['correct']
			answer5 = data[4]['correct']
			answer6 = data[5]['correct'].toString();
			answer7 = data[6]['correct'].toString();
			answer8 = data[7]['correct']
			answer9 = data[8]['correct']
			answer10 = data[9]['correct']

			question1 = $("input:radio[name='question1']:checked").val()
			question2 = $("input:radio[name='question2']:checked").val()
			question3 = $("input:radio[name='question3']:checked").val()
			question4 = $("input:radio[name='question4']:checked").val()
			question5 = $("input:radio[name='question5']:checked").val()
			question6 = $("input:radio[name='question6']:checked").val()
			question7 = $("input:radio[name='question7']:checked").val()
			question8 = $("input:radio[name='question8']:checked").val()
			question9 = $("input:text[name='question9']").val().split(/ +/)
			question10 = $("input:text[name='question10']").val().split(/ +/)

			if (question1 != answer1) {err = err+='\nQuestion 1 is wrong. Answer is ' + answer1}
			if (question2 != answer2) {err = err+='\nQuestion 2 is wrong. Answer is ' + answer2}
			if (question3 != answer3) {err = err+='\nQuestion 3 is wrong. Answer is ' + answer3}
			if (question4 != answer4) {err = err+='\nQuestion 4 is wrong. Answer is ' + answer4}
			if (question5 != answer5) {err = err+='\nQuestion 5 is wrong. Answer is ' + answer5}
			if (question6 != answer6) {err = err+='\nQuestion 6 is wrong. Answer is ' + answer6}
			if (question7 != answer7) {err = err+='\nQuestion 7 is wrong. Answer is ' + answer7}
			if (question8 != answer8) {err = err+='\nQuestion 8 is wrong. Answer is ' + answer8}
			
			$.each(answer9, function(index, value){
				if ($.inArray(value, question9) == -1){
					err = err+='\nQuestion 9 is wrong.'
					return false;
				}
			});

			$.each(answer10, function(index, value){
				if ($.inArray(value, question10) == -1){
					err = err+='\nQuestion 10 is wrong.'
					return false;
				}
			});

			if (err.length){
				alert('Problem:' + err);
				return false;
			}
			else{
				alert('Good Job');
				return true;
			}
		}
	</script>
</head>
<title>ipod Quiz</title>
<form onsubmit="return validateSubmit(this);" action="#" method="post" id="quiz">
</form>