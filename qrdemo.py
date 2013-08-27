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
		return template('''you have returned as {{mbox}}<br/>
			<a href="/signout">sign out</a><br/>
			scan a "code" <a href="/info/vcr">A code</a><br/>
			<a href="/makeqr">create a qr code<a/>''', mbox=mbox)
	else:
		return template('''
				<p> you are not signed in </p>
				<p> Enter an email address to record your actions</p>
				<form action="/register" method="post">
				   email: <input name="mbox" type="text" />
				   <input value="Register" type="submit" />
				</form>
			''')

@app.route('/info/<partname>')
def get_info(partname):
	return template(partname + '_info')

@app.route('/instructions/<partname>')
def get_instructions(partname):
	return template(partname + '_instructions')

@app.route('/makeqr')
def form_qr():
	return template('''
			<p>Enter data for QR code</p>
			<form action="/makeqr" method="post">
			   name: <input name="name" type="text" />
			   <br/>
			   info: <textarea cols="40" rows="5" name="info"></textarea>
			   <br/>
			   instructions: <textarea cols="40" rows="5" name="instructions"></textarea>
			   <br/>			   
			   <input value="Create" type="submit" />
			</form><br/><a href='/'>Home</a>
		''')

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
		tpl.write("<ul><li>%s</li><li>%s</li><li><a href='/instructions/%s'>instructions</a></li><li><a href='/static/%s'>qrcode</a></li></ul>" % (name, info, url_name, qrname))

	instruction_template_name = url_name + '_instructions.tpl'
	with open('views/%s' % instruction_template_name, 'w+') as tpl:
		tpl.write("<ul><li>%s</li><li>%s</li><li><a href='/info/%s'>info</a></li></ul>" % (name, instructions, url_name))

	# return redirect('/static/' + qrname)
	return redirect('/info/' + url_name)

@app.route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root='./static')

@app.route('/register', method='POST')
def do_reg():
	valid, mbox = util.validate_and_format_mbox(request.forms.get('mbox'))
	if valid:
		response.set_cookie('account', mbox)
		return """<p>Ok. You are registered</p>
		          <p><a href='/instructions/vcr'>vcr instructions</a><br/>
		             <a href='/info/vcr'>vcr info</a><br/><br/>
		             <a href='/instructions/tv'>tv instructions</a><br/>
		             <a href='/info/tv'>tv info</a></p>"""
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

run(app, server='gunicorn', host='localhost', port=8099, debug=True, reloader=True)