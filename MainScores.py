from flask import Flask
import Utils

scorefile = Utils.SCORES_FILE_NAME

app = Flask(__name__)

@app.route('/')
def score_server():
    try:
        score = open(scorefile, "r")
    except BaseException as e:
        return """<html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
        <body>
            <h1><div id="score" style="color:red">""" + Utils.BAD_RETURN_CODE + str(e) + """</div></h1>
        </body>
        </html>
        """
    return """
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>Your score is """ + str(score.readline()) + """ Points</h1>
        </body>
    </html>"""

def score_serve():
    app.run(host='127.0.0.1', debug=False, threaded=False, port=8080)

"""
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=False, threaded=False, port=8080)
"""