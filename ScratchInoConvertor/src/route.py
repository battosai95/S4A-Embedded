import bottle
from bottle import request, response

"""
    JS post code:
        //data exemple
        var data = JSON.stringify({
            "objName": "Stage",
        });

        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        xhr.addEventListener("readystatechange", function () {
            if (this.readyState === 4) {
                console.log(this.responseText);
            }
        });

        xhr.open("POST", "http://localhost:8080/arduinize", true);
        xhr.setRequestHeader("content-type", "application/json");
        xhr.onreadystatechange = function () {
            if (xhr.readyState == 4 && xhr.status == 200) {
                console.log(xhr.responseText)
            }
        };
        xhr.send(data);
"""


def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        # allow cross domain
        response.headers['Access-Control-Allow-Origin'] = request.headers["Origin"]
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
        response['Content-Type'] = 'application/json'
        if request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors


app = bottle.app()


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/arduinize', method=['OPTIONS', 'POST'])
@enable_cors
def arduinize():
    """
    @app.route, post send first options method to get headers in order to send the post method with correct headers
    @enable_cors: cross domain
    :return: answer to the server
    """
    print request.json
    return 'json_string'


app.run(host='localhost', port=8080, debug=True)
