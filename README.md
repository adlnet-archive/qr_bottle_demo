qr_bottle_demo
==============

## Contributing to the project
We welcome contributions to this project. Fork this repository, 
make changes and submit pull requests. If you're not comfortable 
with editing the code, please submit an issue and we'll be happy 
to address it. 

## Background

The original idea of the QR generator was to help machinists in a shop easily provide information and instructions about particular pieces of equipment on a mobile device.
When a user logs into the system and creates an information and instructions page, the QR code is generated automatially with all of this information so it can easily be retrieved on any device.
Additionally, a Quiz page is created if the user wants to give a quiz on the information they just supplied. The quiz results are sent to the LRS and are
displayed at the end of it.

This obviously doesn't have to be limited to information and instructions on devices (you can make only quizzes if you want) and is different from the other client side examples
ADL has provided [here](https://github.com/adlnet/experienceapi_client_examples). All of the information sent and received is on the server this time, using the Python requests library; no javascrip involved.

## Installation

#### Installation tested on Ubuntu 12.10 machine with Python 2.7.3

###Software Installation

```shell
sudo apt-get install git fabric
sudo easy_install pip
sudo pip install virtualenv
```

###Setup the environment

```shell
fab setup_env
source ../qrenv/bin/activate
```

###Run

```shell
supervisord
```	

## Use

1. At the main page, sign in with a valid email address (it's just stored as a cookie)
2. Click 'Create QR Code' and fill out the name, information, and operational instructions of the device and click 'Submit'
3. When the information gets submitted, the system creates info, instruction, and questions templates for the device. (If you submit a device with the same name as one that exists already, all existing templates will be overwritten.)
4. Inside of a text editor, open the '<device name>_questions.tpl' file and find the 'data' dictionary in the script at the top of the page.
5. There you will see three types of questions: type, true/false, and short answer. Type the question you want to ask inside of the questions field, and supply the answers (can be either string or numerical) in the answers field. Then supply the correct answer from the answers list in the 'correct' field.
6. Short answer questions are evaluated to see if the user's reponse has ALL of the words in the 'correct' field listed their response so you're gonna want to keep it simple.

## Configuration

### qrdemo.py
Change these constants for LRS endpoints, passwords, and domains

```Python
INFO_DOMAIN = 'http://some/domain/info' #QR code domain to use when created codes
CREATE_PASSWORD = 'password' #Password for people to create QR codes
LRS_STATEMENT_ENDPOINT = 'https://lrs.adlnet.gov/xapi/statements' #LRS statement endpoint
ENDPOINT_AUTH_USERNAME = 'username' #LRS username
ENDPOINT_AUTH_PASSWORD = 'password' #LRS password
AUTHORIZATION = "Basic %s" % base64.b64encode("%s:%s" % (ENDPOINT_AUTH_USERNAME, ENDPOINT_AUTH_PASSWORD))
HEADERS = {        
                'Authorization': AUTHORIZATION,
                'content-type': 'application/json',        
                'X-Experience-API-Version': '1.0.0'
        }
```

### Question data example from the questions template:

```
var data = [
	{'type': 'choice', 'question': 'Which one of these will not work in a fruit blender?', 'answers': ['banana', 'apple', 'screwdriver' ], 'correct': 'screwdriver'},
	{'type':'true/false','question': 'Most blenders blend fruit.', 'answers': [true, false], 'correct': true},
	{'type':'true/false','question': 'This blender will blend meat.', 'answers': [true, false], 'correct': false},
	{'type':'choice','question': 'How many speeds does this blender have?', answers: [1, 2, 3, 4, 5], 'correct': 4},
	{'type': 'choice', 'question': 'Always make sure to add what before blending?', 'answers': ['ice', 'frogs', 'socks', 'dirt'], 'correct': 'ice'},
	{'type':'true/false','question': 'Always make sure the blender is plugged in before using.', 'answers': [true, false], 'correct': true},
	{'type':'true/false','question': 'Always make sure the blender is plugged in while changing blades.', 'answers': [true, false], 'correct': false},
	{'type':'choice','question': 'How many ounces does the blender produce per blend?', 'answers': [8, 16, 32], 'correct': 16},
	{'type':'short answer','question': 'What kind of drinks will this make?', 'correct': ['makes', 'juice', 'smoothie', 'milkshake']},
	{'type':'short answer','question': 'Why should you unplug it while changing blades?', 'correct': ['chop', 'off', 'hand']}
]
```

Five questions are chosen randomly each time to be displayed. If the user misses three or more questions, they fail the quiz; and all results are written to the LRS. Whenever a user visits either an /info or /instructions page, it will also be recorded to the LRS.
