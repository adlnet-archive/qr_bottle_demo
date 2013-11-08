import os
import urllib

def get_existing_pages():
    pages = []
    for root, dirs, filenames in os.walk('static'):
        for f in filenames:
            pages.append({urllib.unquote_plus(f[:-4]): f[:-4]})
    return sorted(pages, key=lambda k: k)

def get_result_statements(responses, answers, types, actor, actor_name, quiz_name, display_name):
    data = [
            {
                'actor': {'mbox': actor, 'name': actor_name},
                'verb': {'id': 'http://adlnet.gov/expapi/verbs/attempted', 'display':{'en-US': 'attempted'}},
                'object':{'id':quiz_name,
                    'definition':{'name':{'en-US':display_name}}}
            }
        ]

    data.append({
        'actor': {'mbox': actor, 'name': actor_name},
        'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
        'object':{'id':quiz_name + '_question1', 'definition':{'name':{'en-US':display_name + ' question1'}}}, 
        'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
        'result':{'success': True, 'response': responses[0],'extensions': {'answer:correct_answer': answers[0]}}
        })
    data.append({
        'actor': {'mbox': actor, 'name': actor_name},
        'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
        'object':{'id':quiz_name + '_question2', 'definition':{'name':{'en-US':display_name + ' question2'}}},
        'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
        'result':{'success': True, 'response': responses[1],'extensions': {'answer:correct_answer': answers[1]}}
        })
    data.append({
        'actor': {'mbox': actor, 'name': actor_name},
        'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
        'object':{'id':quiz_name + '_question3', 'definition':{'name':{'en-US':display_name + ' question3'}}},
        'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
        'result':{'success': True, 'response': responses[2],'extensions': {'answer:correct_answer': answers[2]}}
        })
    data.append({
        'actor': {'mbox': actor, 'name': actor_name},
        'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
        'object':{'id':quiz_name + '_question4', 'definition':{'name':{'en-US':display_name + ' question4'}}},
        'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
        'result':{'success': True, 'response': responses[3],'extensions': {'answer:correct_answer': answers[3]}}
        })
    data.append({
        'actor': {'mbox': actor, 'name': actor_name},
        'verb': {'id': 'http://adlnet.gov/expapi/verbs/answered', 'display':{'en-US': 'answered'}},
        'object':{'id':quiz_name + '_question5', 'definition':{'name':{'en-US':display_name + ' question5'}}},
        'context':{'contextActivities':{'parent':[{'id': quiz_name}]}},
        'result':{'success': True, 'response': responses[4],'extensions': {'answer:correct_answer': answers[4]}}
        })

    wrong, data = grade_results(types, answers, responses, data)
    data.append({
                'actor': {'mbox': actor, 'name': actor_name},
                'verb': {'id': 'http://adlnet.gov/expapi/verbs/passed', 'display':{'en-US': 'passed'}},
                'object':{'id':quiz_name, 'definition':{'name':{'en-US':display_name}}},
                'result':{'score':{'min': 0, 'max': 5, 'raw': 5 - wrong}}
                })
    
    if wrong > 2:
        data[6]['verb']['id'] = 'http://adlnet.gov/expapi/verbs/failed'
        data[6]['verb']['display']['en-US'] = 'failed'
    return wrong, data

def grade_results(types, answers, responses, data):
    wrong = 0
    if types[0] != 'short answer':
        if answers[0] != responses[0]:
            data[1]['result']['success'] = False
            wrong += 1
    else:
        if not set(answers[0].split(',')).issubset([str(i).lower().strip() for i in responses[0].split(",")]):
            data[1]['result']['success'] = False
            wrong += 1
    
    if types[1] != 'short answer':
        if answers[1] != responses[1]:
            data[2]['result']['success'] = False
            wrong += 1
    else:
        if not set(answers[1].split(',')).issubset([str(i).lower().strip() for i in responses[1].split(",")]):
            data[2]['result']['success'] = False
            wrong += 1
    
    if types[2] != 'short answer':
        if answers[2] != responses[2]:
            data[3]['result']['success'] = False
            wrong += 1
    else:
        if not set(answers[2].split(',')).issubset([str(i).lower().strip() for i in responses[2].split(",")]):
            data[3]['result']['success'] = False
            wrong += 1

    if types[3] != 'short answer':
        if answers[3] != responses[3]:
            data[4]['result']['success'] = False
            wrong += 1
    else:
        if not set(answers[3].split(',')).issubset([str(i).lower().strip() for i in responses[3].split(",")]):
            data[4]['result']['success'] = False
            wrong += 1

    if types[4] != 'short answer':
        if answers[4] != responses[4]:
            data[5]['result']['success'] = False
            wrong += 1
    else:
        if not set(answers[4].split(',')).issubset([str(i).lower().strip() for i in responses[4].split(",")]):
            data[5]['result']['success'] = False
            wrong += 1
    return wrong, data