import re

'''
scheme    = $2
authority = $4
path      = $5
query     = $7
fragment  = $9
'''
SCHEME = 2
EMAIL = 5
uri_re = re.compile('^(([^:/?#\s]+):)?(//([^/?#\s]*))?([^?#\s]*)(\?([^#\s]*))?(#([^\s]*))?')

def validate_uri(s):
	res = uri_re.match(s)
	return res.group(SCHEME) != None and res.group(0) == s

def validate_email(s):
	res = uri_re.match(s)
	return res.group(EMAIL) != None

def validate_and_format_mbox(field):
	if not field or field.strip() == "" or not validate_email(field):
		return (False, None)
	if field.startswith('mailto:'):
		return (True, field)
	else:
		return (True, "mailto:%s" % field)