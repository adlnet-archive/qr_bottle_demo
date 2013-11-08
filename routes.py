import datetime
import qrcode
import urllib
import requests
import json
from bottle import Bottle, run, route, request, response, static_file, template, redirect
import util
from util import settings

app = Bottle()

@app.route('/')
def index():
    mbox = request.cookies.account
    name = request.cookies.name
    if mbox and name:
        return redirect('/home')
    return redirect('/register')

@app.route('/home')
def home():
    mbox = request.cookies.account
    name = request.cookies.name
    if not (mbox and name):
        return redirect('/register')
    return template('returning', mbox=mbox, name=name, pages=util.get_existing_pages())

@app.route('/home', method='POST')
def home():
    mbox = request.forms.get('mbox')
    name = request.forms.get('name')
    response.set_cookie('account', mbox)
    response.set_cookie('name', name)
    return template('returning', mbox=mbox, name=name, pages=util.get_existing_pages())    

@app.route('/register')
def register():
    mbox = request.cookies.account
    name = request.cookies.name
    if mbox and name:
        return redirect('/home')    
    return template('register')

@app.route('/signout')
def signout():
    acc_cookie = request.cookies.get('account', None)
    name_cookie = request.cookies.get('name', None)
    if acc_cookie:
        response.set_cookie('account', '', expires=datetime.datetime.now())
    if name_cookie:
        response.set_cookie('name', '', expires=datetime.datetime.now())
    redirect('/register') 

@app.route('/static/<filename>')
def server_static(filename):
    if not request.cookies.get('account') or not request.cookies.get('name'):
            redirect('/register')    
    return static_file(filename, root='./static')

@app.route('/info/<partname>')
def get_info(partname):
    if not request.cookies.get('account') or not request.cookies.get('name'):
            redirect('/register')

    actor = 'mailto:' + request.cookies.get('account')
    actor_name = request.cookies.get('name')
    display_name = urllib.unquote_plus(partname)

    data = {
            'actor': {'mbox': actor, 'name': actor_name},
            'verb': {'id': 'http://adlnet.gov/expapi/verbs/visited', 'display':{'en-US': 'visited'}},
            'object':{'id': settings.INFO_DOMAIN + '/info/' + partname,
                'definition':{'name':{'en-US':display_name + ' info page'}}}
            }
    post_resp = requests.post(settings.LRS_STATEMENT_ENDPOINT, data=json.dumps(data), headers=settings.HEADERS, verify=False)
    return template(partname + '_info')

@app.route('/instructions/<partname>')
def get_instructions(partname):
    if not request.cookies.get('account') or not request.cookies.get('name'):
            redirect('/register')

    actor = 'mailto:' + request.cookies.get('account')
    actor_name = request.cookies.get('name')        
    display_name = urllib.unquote_plus(partname)

    data = {
            'actor': {'mbox': actor, 'name': actor_name},
            'verb': {'id': 'http://adlnet.gov/expapi/verbs/visited', 'display':{'en-US': 'visited'}},
            'object':{'id': settings.INFO_DOMAIN + '/instructions/' + partname,
                'definition':{'name':{'en-US':display_name + ' instructions page'}}}
            }
    post_resp = requests.post(settings.LRS_STATEMENT_ENDPOINT, data=json.dumps(data), headers=settings.HEADERS, verify=False)
    return template(partname + '_instructions')

@app.route('/quiz/<partname>')
def get_quiz(partname):
    if not request.cookies.get('account') or not request.cookies.get('name'):
            redirect('/register')
    return template(partname + '_questions', partname=urllib.unquote_plus(partname))

@app.route('/quiz/<partname>', method='POST')
def get_quiz(partname):
    if not request.cookies.get('account') or not request.cookies.get('name'):
            redirect('/register')

    answers = []
    answers.append(request.forms.get('answer1'))
    answers.append(request.forms.get('answer2'))
    answers.append(request.forms.get('answer3'))
    answers.append(request.forms.get('answer4'))
    answers.append(request.forms.get('answer5'))

    types = []
    types.append(request.forms.get('type1'))
    types.append(request.forms.get('type2'))
    types.append(request.forms.get('type3'))
    types.append(request.forms.get('type4'))
    types.append(request.forms.get('type5'))

    responses = []
    responses.append(request.forms.get('question1'))
    responses.append(request.forms.get('question2'))
    responses.append(request.forms.get('question3'))
    responses.append(request.forms.get('question4'))
    responses.append(request.forms.get('question5'))

    actor = 'mailto:' + request.cookies.get('account')
    actor_name = request.cookies.get('name')
    quiz_name = 'activity:qr_demo_%s_quiz' % partname
    display_name = urllib.unquote_plus(partname) + ' quiz'
    
    wrong, data = util.get_result_statements(responses, answers, types, actor, actor_name, quiz_name, display_name)
    post_resp = requests.post(settings.LRS_STATEMENT_ENDPOINT, data=json.dumps(data), headers=settings.HEADERS, verify=False)
    status = post_resp.status_code
    content = post_resp.content

    stmts, sens = util.retrieve_statements(status, content)    

    return template('quiz_results', partname=partname, status=status, score=(5 - wrong), content=content, stmts=stmts, sens=sens)

@app.route('/makeqr')
def form_qr():
    if not request.cookies.get('account') or not request.cookies.get('name'):
            redirect('/register')
    return template('makeqr.tpl', pw=settings.CREATE_PASSWORD)

@app.route('/makeqr', method='POST')
def create_qr():
    if not request.cookies.get('account') or not request.cookies.get('name'):
            redirect('/register')

    name = request.forms.get('name')

    if name in [d.keys()[0] for d in util.get_existing_pages()]:
        return redirect('/tryagain')

    url_name = urllib.quote_plus(name)
    instructions = request.forms.get('instructions')
    info = request.forms.get('info')

    qrname = url_name + '.png'
    qrdata =  settings.INFO_DOMAIN + url_name
    img = qrcode.make(qrdata)
    
    with open('static/%s' % qrname, 'w+') as qr:
            img.save(qr, 'PNG')

    info_template_name = url_name + '_info.tpl'
    with open('views/%s' % info_template_name, 'w+') as tpl:
            tpl.write(settings.INFO_TEMPLATE.format(name, name + ' Info', info, url_name, url_name, qrname))

    instruction_template_name = url_name + '_instructions.tpl'
    with open('views/%s' % instruction_template_name, 'w+') as tpl:
            tpl.write(settings.INSTRUCTION_TEMPLATE.format(name, name + ' Instructions', instructions, url_name))

    question_template_name = url_name + '_questions.tpl'
    with open ('views/%s' % question_template_name, 'w+') as tpl:
            tpl.write(settings.QUIZ_TEMPLATE)
    return redirect('/info/' + url_name)  

@app.route('/tryagain')
def try_again():
    if not request.cookies.get('account') or not request.cookies.get('name'):
            redirect('/register')    
    return template('try_again')

run(app, server='gunicorn', host='localhost', port=8099, debug=True, reloader=True)