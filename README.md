qr_bottle_demo
==============

#### Installation tested on Ubuntu 12.10 machine with Python 2.7.3

## Installation

Software Installation

    sudo apt-get install git fabric
    sudo easy_install pip
    sudo pip install virtualenv

Setup the environment

    fab setup_env
    source ../qrenv/bin/activate

Run

	supervisord
	
## Use

1. At the main page, sign in with a valid email address (it's just stored as a cookie)
2. Click 'Create QR Code' and fill out the name, information, and operational instructions of the device and click 'Submit'
3. When the information gets submitted, the system creates info, instruction, and questions templates for the device. (If you submit a device with the same name as one that exists already, all existing templates will be overwritten.)
4. Inside of a text editor, open the '<device name>_questions.tpl' file and find the 'data' dictionary in the script at the top of the page.
5. There are three types of questions; type, true/false, and short answer. Type the question you want to ask inside of the questions field, and supply the answers (can be either string or numerical) in the answers field. Then supply the correct answer from the answers list in the 'correct' field.
6. Short answer questions are evaluated to see if the user's reponse has ALL of the words in the 'correct' field listed their response so you're gonna want to keep it simple.

### Question data example:
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


If you want to change the endpoint the QR codes point to when scanning them, change the INFO_DOMAIN constant at the top of the qrdemo.py file. Same goes for the LRS
endpoint. If you want to change it, just edit the LRS_STATEMENT_ENDPOINT constant at the top of the qrdemo.py file then change your username and password (ENDPOINT_AUTH_USERNAME and ENDPOINT_AUTH_PASSWORD). Creating the templates and QR code is also protected. To change the password, change the CREATE_PASSWORD constant in qrdemo.py.
