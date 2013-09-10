from bottle import Bottle, run, route, request, response, static_file, template, redirect
import datetime
import qrcode
import urllib
import requests
import json
import os

app = Bottle()

INFO_DOMAIN = 'http://localhost:8099/info/'
QUIZ_TEMPLATE = """<html>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="//code.jquery.com/jquery.js"></script>
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css"/>
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
		]

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
			<h1>{{partname}} Quiz</h1>
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
</html>"""

INSTRUCTION_TEMPLATE = """<html>
<title>{0}</title>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="//code.jquery.com/jquery.js"></script>
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css"/>
</head>
<body>
    <div class="jumbotron">
		<div class="container">
		<h2>{1}</h2>
		<p>{2}</p>
		<p><a href='/info/{3}'>info</a></p>
		</div>	
</div>
<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
</body>
</html>
"""
INFO_TEMPLATE = """<html>
<title>{0}</title>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="//code.jquery.com/jquery.js"></script>
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css"/>
</head>
<body>
    <div class="jumbotron">
		<div class="container">
		<h2>{1}</h2>
		<p>{2}</p>
		<p><a href='/instructions/{3}'>instructions</a></p>
		<p><a href='/quiz/{4}'>quiz</a></p>
		<p><a href='/static/{5}'>qrcode</a></p>
		<p><a href='/'>home</a></p>
		</div>	
</div>
<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
</body>
</html>
"""

@app.route('/')
def index():
	mbox = request.cookies.account	
	if mbox:
		pages = []
		for root, dirs, filenames in os.walk('static'):
			for f in filenames:
				pages.append({urllib.unquote_plus(f[:-4]): f[:-4]})		
		return template('returning', mbox=mbox, pages=pages)
	else:
		return template('register')

@app.route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root='./static')

@app.route('/info/<partname>')
def get_info(partname):
	return template(partname + '_info')

@app.route('/instructions/<partname>')
def get_instructions(partname):
	return template(partname + '_instructions')

@app.route('/quiz/<partname>', method='GET')
def get_quiz(partname):
	return template(partname + '_questions', partname=urllib.unquote_plus(partname))

@app.route('/quiz/<partname>', method='POST')
def get_quiz(partname):
	answer1 = request.forms.get('answer1')
	answer2 = request.forms.get('answer2')
	answer3 = request.forms.get('answer3')
	answer4 = request.forms.get('answer4')
	answer5 = request.forms.get('answer5')
	
	type1 = request.forms.get('type1')
	type2 = request.forms.get('type2')
	type3 = request.forms.get('type3')
	type4 = request.forms.get('type4')
	type5 = request.forms.get('type5')

	response1 = request.forms.get('question1')
	response2 = request.forms.get('question2')
	response3 = request.forms.get('question3')
	response4 = request.forms.get('question4')
	response5 = request.forms.get('question5')

	actor = 'mailto:' + request.cookies.get('account')
	if not actor:
		actor = 'mailto:test@test.com'

	quiz_name = 'activity:qr_demo_%s_quiz' % partname
	display_name = urllib.unquote_plus(partname) + ' quiz'
	data = [{'actor': {'mbox': actor}, 'verb': {'id': 'http://adlnet.gov/expapi/verbs/attempted', 'display':{'en-US': 'attempted'}}, 'object':{'id':quiz_name,
		'definition':{'name':{'en-US':display_name}}}}]

	resp1 = {'actor': {'mbox': actor}, 'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
			'object':{'id':quiz_name + '_question1', 'definition':{'name':{'en-US':display_name + ' question1'}}}, 
			'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
			'result':{'success': True, 'response': response1,'extensions': {'answer:correct_answer': answer1}}}
	resp2 = {'actor': {'mbox': actor}, 'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
			'object':{'id':quiz_name + '_question2', 'definition':{'name':{'en-US':display_name + ' question2'}}},
			'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
			'result':{'success': True, 'response': response2,'extensions': {'answer:correct_answer': answer2}}}
	resp3 = {'actor': {'mbox': actor}, 'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
			'object':{'id':quiz_name + '_question3', 'definition':{'name':{'en-US':display_name + ' question3'}}},
			'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
			'result':{'success': True, 'response': response3,'extensions': {'answer:correct_answer': answer3}}}
	resp4 = {'actor': {'mbox': actor}, 'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
			'object':{'id':quiz_name + '_question4', 'definition':{'name':{'en-US':display_name + ' question4'}}},
			'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
			'result':{'success': True, 'response': response4,'extensions': {'answer:correct_answer': answer4}}}
	resp5 = {'actor': {'mbox': actor}, 'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
			'object':{'id':quiz_name + '_question5', 'definition':{'name':{'en-US':display_name + ' question5'}}},
			'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
			'result':{'success': True, 'response': response5,'extensions': {'answer:correct_answer': answer5}}}
	
	err = '';
	wrong = 0
	if type1 != 'short answer':
		if answer1 != response1:
			resp1['result']['success'] = False
			wrong += 1
	else:
		if not set(answer1.split(',')).issubset(response1.split()):
			resp1['result']['success'] = False
			wrong += 1			
	data.append(resp1)
	
	if type2 != 'short answer':
		if answer2 != response2:
			resp2['result']['success'] = False
			wrong += 1
	else:
		if not set(answer2.split(',')).issubset(response2.split()):
			resp2['result']['success'] = False
			wrong += 1			
	data.append(resp2)
	
	if type3 != 'short answer':
		if answer3 != response3:
			resp3['result']['success'] = False
			wrong += 1
	else:
		if not set(answer3.split(',')).issubset(response3.split()):
			resp3['result']['success'] = False
			wrong += 1			
	data.append(resp3)

	if type4 != 'short answer':
		if answer4 != response4:
			resp4['result']['success'] = False
			wrong += 1
	else:
		if not set(answer4.split(',')).issubset(response4.split()):
			resp4['result']['success'] = False
			wrong += 1			
	data.append(resp4)

	if type5 != 'short answer':
		if answer5 != response5:
			resp5['result']['success'] = False
			wrong += 1
	else:
		if not set(answer5.split(',')).issubset(response5.split()):
			resp5['result']['success'] = False
			wrong += 1			
	data.append(resp5)

	result_data = {'actor': {'mbox': actor}, 'verb': {'id': 'http://adlnet.gov/expapi/verbs/passed', 'display':{'en-US': 'passed'}},
		'object':{'id':'activity:qr_demo_quiz', 'definition':{'name':{'en-US':display_name + ' quiz'}}}, 'result':{'score':{'min': 0, 'max': 5, 'raw': 5 - wrong}}}
	
	if wrong >= 3:
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
	return template('quiz_results', partname=partname)

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
	qrdata =  INFO_DOMAIN + url_name
	img = qrcode.make(qrdata)
	
	with open('static/%s' % qrname, 'w+') as qr:
		img.save(qr, 'PNG')

	info_template_name = url_name + '_info.tpl'
	with open('views/%s' % info_template_name, 'w+') as tpl:
		tpl.write(INFO_TEMPLATE.format(name, name + ' Info', info, url_name, url_name, qrname))

	instruction_template_name = url_name + '_instructions.tpl'
	with open('views/%s' % instruction_template_name, 'w+') as tpl:
		tpl.write(INSTRUCTION_TEMPLATE.format(name, name + ' Instructions', instructions, url_name))

	question_template_name = url_name + '_questions.tpl'
	with open ('views/%s' % question_template_name, 'w+') as tpl:
		tpl.write(QUIZ_TEMPLATE)

	return redirect('/info/' + url_name)

@app.route('/register', method='POST')
def do_reg():
	mbox = request.forms.get('mbox')
	response.set_cookie('account', mbox)

	pages = []
	for root, dirs, filenames in os.walk('static'):
		for f in filenames:
			pages.append({urllib.unquote_plus(f[:-4]): f[:-4]})

	return template('returning', mbox=mbox, pages=pages)

@app.route('/signout')
def signout():
	# figure out how to delete a cookie
	acc_cookie = request.cookies.get('account', None)
	if acc_cookie:
		response.set_cookie('account', '', expires=datetime.datetime.now())
	redirect('/') 

run(app, server='gunicorn', host='localhost', port=8099, debug=True, reloader=True)