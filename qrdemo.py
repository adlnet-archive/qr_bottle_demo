from bottle import Bottle, run, route, request, response, static_file, template, redirect
import datetime
import util
import qrcode
import pdb
import urllib
import requests
import json

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
	err = '';
	answer1 = request.forms.get('answer1')
	answer2 = request.forms.get('answer2')
	answer3 = request.forms.get('answer3')
	answer4 = request.forms.get('answer4')
	answer5 = request.forms.get('answer5')
	answer6 = request.forms.get('answer6')
	answer7 = request.forms.get('answer7')
	answer8 = request.forms.get('answer8')
	answer9 = request.forms.get('answer9')
	answer10 = request.forms.get('answer10')

	response1 = request.forms.get('question1')
	response2 = request.forms.get('question2')
	response3 = request.forms.get('question3')
	response4 = request.forms.get('question4')
	response5 = request.forms.get('question5')
	response6 = request.forms.get('question6')
	response7 = request.forms.get('question7')
	response8 = request.forms.get('question8')
	response9 = request.forms.get('question9')
	response10 = request.forms.get('question10')

	actor = request.cookies.get('account')
	if not actor:
		actor = 'test@test.com'

	quiz_name = 'activity:qr_demo_%s_quiz' % partname

	data = [{'actor': {'mbox': actor}, 'verb': {'id': 'http://adlnet.gov/expapi/verbs/attempted', 'display':{'en-US': 'attempted'}}, 'object':{'id':quiz_name}}]

	resp1 = {'actor': {'mbox': actor}, 'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
			'object':{'id':quiz_name + '_question1'}, 'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
			'result':{'success': True, 'response': response1,'extensions': {'answer:correct_answer': answer1}}}
	resp2 = {'actor': {'mbox': actor}, 'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
			'object':{'id':quiz_name + '_question2'}, 'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
			'result':{'success': True, 'response': response2,'extensions': {'answer:correct_answer': answer2}}}
	resp3 = {'actor': {'mbox': actor}, 'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
			'object':{'id':quiz_name + '_question3'}, 'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
			'result':{'success': True, 'response': response3,'extensions': {'answer:correct_answer': answer3}}}
	resp4 = {'actor': {'mbox': actor}, 'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
			'object':{'id':quiz_name + '_question4'}, 'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
			'result':{'success': True, 'response': response4,'extensions': {'answer:correct_answer': answer4}}}
	resp5 = {'actor': {'mbox': actor}, 'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
			'object':{'id':quiz_name + '_question5'}, 'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
			'result':{'success': True, 'response': response5,'extensions': {'answer:correct_answer': answer5}}}
	resp6 = {'actor': {'mbox': actor}, 'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
			'object':{'id':quiz_name + '_question6'}, 'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
			'result':{'success': True, 'response': response6,'extensions': {'answer:correct_answer': answer6}}}
	resp7 = {'actor': {'mbox': actor}, 'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
			'object':{'id':quiz_name + '_question7'}, 'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
			'result':{'success': True, 'response': response7,'extensions': {'answer:correct_answer': answer7}}}
	resp8 = {'actor': {'mbox': actor}, 'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
			'object':{'id':quiz_name + '_question8'}, 'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
			'result':{'success': True, 'response': response8,'extensions': {'answer:correct_answer': answer8}}}
	resp9 = {'actor': {'mbox': actor}, 'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
			'object':{'id':quiz_name + '_question9'}, 'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
			'result':{'success': True, 'response': response9,'extensions': {'answer:correct_answer': answer9}}}
	resp10 = {'actor': {'mbox': actor}, 'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
			'object':{'id':quiz_name + '_question10'}, 'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
			'result':{'success': True, 'response': response10,'extensions': {'answer:correct_answer': answer10}}}

	wrong = 0
	if answer1 != response1:
		resp1['result']['success'] = False
		wrong += 1
	data.append(resp1)
	
	if answer2 != response2:
		resp2['result']['success'] = False
		wrong += 1
	data.append(resp2)
	
	if answer3 != response3:
		resp3['result']['success'] = False
		wrong += 1
	data.append(resp3)

	if answer4 != response4:
		resp4['result']['success'] = False
		wrong += 1
	data.append(resp4)

	if answer5 != response5:
		resp5['result']['success'] = False
		wrong += 1
	data.append(resp5)

	if answer6 != response6:
		resp6['result']['success'] = False
		wrong += 1
	data.append(resp6)

	if answer7 != response7:
		resp7['result']['success'] = False
		wrong += 1
	data.append(resp7)

	if answer8 != response8:
		resp8['result']['success'] = False
		wrong += 1
	data.append(resp8)

	if answer9.split(',') != response9.split():
		resp9['result']['success'] = False
		wrong += 1
	data.append(resp9)

	if answer10.split(',') != response10.split():
		resp10['result']['success'] = False
		wrong += 1
	data.append(resp10)

	result_data = {'actor': {'mbox': actor}, 'verb': {'id': 'http://adlnet.gov/expapi/verbs/passed', 'display':{'en-US': 'passed'}}, 'object':{'id':'activity:qr_demo_quiz'},
		'result':{'score':{'raw': 10 - wrong}}}
	
	if wrong >= 6:
		result_data['verb']['id'] = 'http://adlnet.gov/expapi/verbs/failed'
		result_data['verb']['display']['en-US'] = 'failed'
	data.append(result_data)

	headers = {	
			'Authorization': 'Basic dG9tOjEyMzQ=',
			'content-type': 'application/json',	
			'X-Experience-API-Version': '1.0.0'
		}

	post_resp = requests.post('https://lrs.adlnet.gov/XAPI/statements', data=json.dumps(data), headers=headers, verify=False)
	print post_resp.status_code	
	print post_resp.content

	return """<p> Thanks for taking the quiz!!</p><br/><p><a href='/info/%s'>info</a></p>""" % partname

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
		tpl.write("<title>%s</title><p>%s</p>\n<p><a href='/instructions/%s'>instructions</a></p>\n<p><a href='/quiz/%s'>quiz</a></p>\n<p><a href='/static/%s'>qrcode</a></p>" % (name, info, url_name, url_name, qrname))

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
			{'type': 'choice', 'question': '', 'answers': [], 'correct': 0},
			{'type':'true/false','question': '', 'answers': [true, false], 'correct': false},
			{'type':'true/false','question': '', 'answers': [true, false], 'correct': false},
			{'type':'choice','question': '', answers: [], 'correct': 0},
			{'type': 'choice', 'question': '', 'answers': [], 'correct': 0},
			{'type':'true/false','question': '', 'answers': [true, false], 'correct': false},
			{'type':'true/false','question': '', 'answers': [true, false], 'correct': false},
			{'type':'choice','question': '', 'answers': [], 'correct': 0},
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
</form>"""

run(app, server='gunicorn', host='localhost', port=8099, debug=True, reloader=True)