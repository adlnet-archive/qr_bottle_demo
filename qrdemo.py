from bottle import Bottle, run, route, request, response, static_file, template, redirect
import datetime
import util
import qrcode
import pdb
import urllib

app = Bottle()

@app.route('/')
def index():
	mbox = request.cookies.account	
	if mbox:
		return template('returning.tpl', mbox=mbox)
	else:
		return template('register.tpl')

@app.route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root='./static')

@app.route('/css/<filename>')
def server_css(filename):
	return static_file(filename, root='./css')

@app.route('/test')
def test():
	return template('test.tpl')

@app.route('/info/<partname>')
def get_info(partname):
	return template(partname + '_info')

@app.route('/instructions/<partname>')
def get_instructions(partname):
	return template(partname + '_instructions')

@app.route('/quiz/<partname>', method='GET')
def get_quiz(partname):
	return template(partname + '_questions')

@app.route('/quiz/<partname>', method='POST')
def get_quiz(partname):
	return """<p> You passed the exam!!</p><br/><p><a href='/info/%s'>info</a></p>""" % partname

@app.route('/makeqr')
def form_qr():
	return template('makeqr.tpl')

@app.route('/makeqr', method='POST')
def create_qr():
	name = request.forms.get('name')
	url_name = urllib.quote_plus(name)
	instructions = request.forms.get('instructions')
	info = request.forms.get('info')

	qrname = url_name + '.png'
	qrdata = 'http://localhost:8099/info/' + url_name
	img = qrcode.make(qrdata)
	
	with open('static/%s' % qrname, 'w+') as qr:
		img.save(qr, 'PNG')

	info_template_name = url_name + '_info.tpl'
	with open('views/%s' % info_template_name, 'w+') as tpl:
		tpl.write("<title>%s</title>\n<p>%s</p>\n<p><a href='/instructions/%s'>instructions</a></p>\n<p><a href='/quiz/%s'>quiz</a></p>\n<p><a href='/static/%s'>qrcode</a></p>" % (name, info, url_name, url_name, qrname))

	instruction_template_name = url_name + '_instructions.tpl'
	with open('views/%s' % instruction_template_name, 'w+') as tpl:
		tpl.write("<title>%s</title>\n<p>%s</p>\n<p><a href='/info/%s'>info</a></p>" % (name, instructions, url_name))

	question_template_name = url_name + '_questions.tpl'
	with open ('views/%s' % question_template_name, 'w+') as tpl:
		tpl.write(QUIZ_TEMPLATE)

	return redirect('/info/' + url_name)


@app.route('/register', method='POST')
def do_reg():
	valid, mbox = util.validate_and_format_mbox(request.forms.get('mbox'))
	if valid:
		response.set_cookie('account', mbox)
		return """<p>Ok. You are registered</p>
		          <p><a href='/makeqr'>Create QR Codes</a></p>"""
	else:
		return '''<p>oh man, you fail</p>
					<p> Enter an email address to record your actions</p>
					<form action="/register" method="post">
					   email: <input name="mbox" type="text" />
					   <input value="Register" type="submit" />
					</form>
				'''

@app.route('/signout')
def signout():
	# figure out how to delete a cookie
	acc_cookie = request.cookies.get('account', None)
	if acc_cookie:
		response.set_cookie('account', '', expires=datetime.datetime.now())
	redirect('/') 
QUIZ_TEMPLATE = """<head>
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
	<script type="text/javascript">
		var data = [
			{'type': 'choice', 'question': '', 'answers': [], 'correct': ''},
			{'type':'true/false','question': '', 'answers': [], 'correct': ''},
			{'type':'true/false','question': '', 'answers': [], 'correct': ''},
			{'type':'choice','question': '', 'answers': [], 'correct': ''},
			{'type': 'choice', 'question': '', 'answers': [], 'correct': ''},
			{'type':'true/false','question': '', 'answers': [], 'correct': ''},
			{'type':'true/false','question': '', 'answers': [], 'correct': ''},
			{'type':'choice','question': '', 'answers': [], 'correct': ''},
			{'type':'short answer','question': '', 'correct': []},
			{'type':'short answer','question': '', 'correct': []}
		];

		$(document).ready(function(){
			$.each(data, function(index, value){
				display_value = index + 1
				if (value['type'] != 'short answer'){
					$('#quiz').append('<tr><td>' + display_value + '.</td>' + '<td>' + value['question'] + '</td></tr>');
					$.each(value['answers'], function(i, v){
						$('#quiz').append('<input type="radio" name="' + ('question' + display_value) +'" value="'+ v +'">'+ v +'<br>')
					});
				}
				else{
					$('#quiz').append('<tr><td>' + display_value + '.</td>' + '<td>' + value['question'] + '</td><td><input type="text" name="' + ('question' + display_value) + '"></td></tr>');
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

			if (question1 != answer1) {err = err+='\\nQuestion 1 is wrong. Answer is ' + answer1}
			if (question2 != answer2) {err = err+='\\nQuestion 2 is wrong. Answer is ' + answer2}
			if (question3 != answer3) {err = err+='\\nQuestion 3 is wrong. Answer is ' + answer3}
			if (question4 != answer4) {err = err+='\\nQuestion 4 is wrong. Answer is ' + answer4}
			if (question5 != answer5) {err = err+='\\nQuestion 5 is wrong. Answer is ' + answer5}
			if (question6 != answer6) {err = err+='\\nQuestion 6 is wrong. Answer is ' + answer6}
			if (question7 != answer7) {err = err+='\\nQuestion 7 is wrong. Answer is ' + answer7}
			if (question8 != answer8) {err = err+='\\nQuestion 8 is wrong. Answer is ' + answer8}
			
			$.each(answer9, function(index, value){
				if ($.inArray(value, question9) == -1){
					err = err+='\\nQuestion 9 is wrong.'
					return false;
				}
			});

			$.each(answer10, function(index, value){
				if ($.inArray(value, question10) == -1){
					err = err+='\\nQuestion 10 is wrong.'
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
<form onsubmit="return validateSubmit(this);" action="#" method="post" id="quiz">
</form>"""

run(app, server='gunicorn', host='localhost', port=8099, debug=True, reloader=True)