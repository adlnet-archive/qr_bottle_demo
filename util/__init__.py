import os
import urllib
import json
import requests

def get_existing_pages():
    pages = []
    for root, dirs, filenames in os.walk('static'):
        for f in filenames:
            pages.append({urllib.unquote_plus(f[:-4]): f[:-4]})
    return sorted(pages, key=lambda k: k)

def get_result_statements(responses, answers, types, questions, actor, actor_name, quiz_name, display_name):
    data = [
            {
                'actor': {'mbox': actor, 'name': actor_name},
                'verb': {'id': 'http://adlnet.gov/expapi/verbs/attempted', 'display':{'en-US': 'attempted'}},
                'object':{'id':quiz_name,
                    'definition':{'name':{'en-US':display_name}}}
            }
        ]

    for x in range(0,5):
        data.append({
            'actor': {'mbox': actor, 'name': actor_name},
            'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
            'object':{'id':quiz_name + '_question1', 'definition':{'name':{'en-US':display_name + ' question1'}, 'description':{'en-US':questions[x]}}}, 
            'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
            'result':{'success': True, 'response': responses[x],'extensions': {'answer:correct_answer': answers[x]}}
            })

    wrong, data = grade_results(types, answers, responses, data)
    data.append({
                'actor': {'mbox': actor, 'name': actor_name},
                'verb': {'id': 'http://adlnet.gov/expapi/verbs/passed', 'display':{'en-US': 'passed'}},
                'object':{'id':quiz_name, 'definition':{'name':{'en-US':display_name}}},
                'result':{'score':{'min': 0, 'max': 5, 'raw': 5 - wrong}}
                })
    
    if wrong >= 2:
        data[6]['verb']['id'] = 'http://adlnet.gov/expapi/verbs/failed'
        data[6]['verb']['display']['en-US'] = 'failed'
    return wrong, data

def grade_results(types, answers, responses, data):
    wrong = 0
    for x in range(0,5):
        if types[x] == 'true/false':
            if answers[x] != responses[x]:
                data[x+1]['result']['success'] = False
                wrong += 1
        elif types[x] == 'choice':
            if answers[x].strip() != responses[x].strip():
                data[x+1]['result']['success'] = False
                wrong += 1
        else:
            if not set(answers[x].lower().strip().split(",")).issubset([str(i).lower().strip() for i in responses[x].split(" ")]):
                data[x+1]['result']['success'] = False
                wrong += 1
    
    return wrong, data

def retrieve_statements(status, post_content):
    stmts = []
    jstmts = []
    sens = []
    if status == 200:
        content = json.loads(post_content)

        for x in range(0,7):
            stmts.append(requests.get(settings.LRS_STATEMENT_ENDPOINT + '?statementId=%s' % content[x], headers=settings.HEADERS, verify=False).content)
            jstmts.append(json.loads(stmts[x]))
        
        sens.append("{0} {1} {2}".format(jstmts[0]['actor']['name'], jstmts[0]['verb']['display']['en-US'], jstmts[0]['object']['definition']['name']['en-US']))
        for x in range(1, 6):
            sens.append("{0} {1} {2} ({3}) with {4}. (Answer was {5})".format(jstmts[x]['actor']['name'], jstmts[x]['verb']['display']['en-US'],
                jstmts[x]['object']['definition']['name']['en-US'], jstmts[x]['object']['definition']['description']['en-US'], jstmts[x]['result']['response'],
                jstmts[x]['result']['extensions']['answer:correct_answer']))
        sens.append("{0} {1} {2}".format(jstmts[6]['actor']['name'], jstmts[6]['verb']['display']['en-US'], jstmts[6]['object']['definition']['name']['en-US']))
    return stmts, sens

def create_questions(form):
    data = []
    q_dict = {}
    for i in range(1,11):
        st_i = str(i)
        q_dict = {}
        q_dict['type'] = form.get('types' + st_i)
        q_dict['question'] = form.get('question' + st_i + 'text')
        
        if q_dict['type'] == 'short answer':
            q_dict['correct'] = form.get('question' + st_i + 'answer').split(' ')
        elif q_dict['type'] == 'true/false':
            q_dict['correct'] = form.get('question' + st_i + 'answer') in ['True', 'true']
            q_dict['answers'] = [True, False]
        else:
            q_dict['correct'] = form.get('question' + st_i + 'answer')
            q_dict['answers'] = form.get('question' + st_i + 'choices').strip().split(',')

        data.append(q_dict)
    return data