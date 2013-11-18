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
2. Click 'Create QR Code' and fill out the name, information, and operational instructions of the device.
3. Fill out the 10 questions to add to the quiz (if you create a 'choice' question, separate the choices by commas).
4. Short answer questions are evaluated to see if the user's reponse has ALL of the words in the 'answer' field listed their response so you're gonna want to keep it simple.
5. When the information gets submitted, the system creates info, instruction, and questions templates for the device.

## Configuration

### util/settings.py
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


NOTE: Five questions are chosen randomly each time to be displayed on each quiz page. If the user misses three or more questions, they fail the quiz; and all results are written to the LRS. Whenever a user visits either an /info or /instructions page, it will also be recorded to the LRS.
