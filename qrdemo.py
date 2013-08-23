from bottle import Bottle, run, route, request, response, static_file, template, redirect
import datetime
import util

app = Bottle()

@app.route('/')
def index():
	mbox = request.cookies.account
	if mbox:
		return template('''you have returned as {{mbox}}<br/>
			<a href="/signout">sign out</a><br/>
			scan a "code" <a href="/info/vcr">A code</a>''', mbox=mbox)
	else:
		return template('''
				<p> you are not signed in </p>
				<p> Enter an email address to record your actions</p>
				<form action="/register" method="post">
				   email: <input name="mbox" type="text" />
				   <input value="Register" type="submit" />
				</form>
			''')

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

@app.route('/<action>/<item>')
def item_api(action='list', item='all'):
	# return items[action][item]
	mbox = request.cookies.get('account', 'unknown')
	return template('Action was {{action}}<br/>Item was {{item}}<br/>Mbox was {{mbox}}', action=action, item=item, mbox=mbox)

run(app, server='gunicorn', host='localhost', port=8099, debug=True, reloader=True)