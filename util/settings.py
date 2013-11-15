import base64

INFO_DOMAIN = 'http://some/domain/info/'

CREATE_PASSWORD = 'password'

LRS_STATEMENT_ENDPOINT = 'http://localhost:8000/xapi/statements'

ENDPOINT_AUTH_USERNAME = 'lou'

ENDPOINT_AUTH_PASSWORD = 'password'

AUTHORIZATION = "Basic %s" % base64.b64encode("%s:%s" % (ENDPOINT_AUTH_USERNAME, ENDPOINT_AUTH_PASSWORD))

HEADERS = {        
                'Authorization': AUTHORIZATION,
                'content-type': 'application/json',        
                'X-Experience-API-Version': '1.0.0'
        }

QUIZ_TEMPLATE = """<html>
<head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="//code.jquery.com/jquery.js"></script>
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap.min.css"/>
        <script type="text/javascript">
                var data = %s

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
                                                $('#radioDiv' + display_value + '-' + (i + 1)).append('<label><input type="radio" name="' + ('question' + display_value) +'" value="'+ v +'" required>'+ v +'</label>')
                                        });
                                }
                                else{
                                        $('#fg' + display_value).append('<input class="form-control "type="text" name="' + ('question' + display_value) + '" required>');
                                }
                                $('#fg' + display_value).append('<input type="hidden" name="' + ('answer' + display_value) + '" value="' + value['correct'] + '">');
                                $('#fg' + display_value).append('<input type="hidden" name="' + ('type' + display_value) + '" value="' + value['type'] + '">');
                                $('#fg' + display_value).append('<input type="hidden" name="' + ('questionasked' + display_value) + '" value="' + value['question'] + '">');
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
<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.2/js/bootstrap.min.js"></script>
</body>
</html>"""

INSTRUCTION_TEMPLATE = """<html>
<title>{0}</title>
<head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="//code.jquery.com/jquery.js"></script>
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap.min.css"/>
</head>
<body>
    <div class="jumbotron">
                <div class="container">
                <h2>{1}</h2>
                <p>{2}</p>
                <p><a href='/info/{3}'>info</a></p>
                </div>        
</div>
<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.2/js/bootstrap.min.js"></script>
</body>
</html>
"""

INFO_TEMPLATE = """<html>
<title>{0}</title>
<head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="//code.jquery.com/jquery.js"></script>
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap.min.css"/>
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
<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.2/js/bootstrap.min.js"></script>
</body>
</html>
"""        