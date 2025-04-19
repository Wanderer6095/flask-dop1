from flask import Flask, url_for, request
import os

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)


@app.route('/home', methods=['POST', 'GET'])
def astronaut_selection():
    
    if request.method == "POST":
        file = (request.files.get("file"))
        with open(url_for('static', filename='img/MARS-6.png')[1:], "wb") as out_file:
            out_file.write(file.read())
    url_style = url_for('static', filename='css/style2.css')
    with open("5.html", encoding="utf-8") as file:
        html = file.read()
    html = html.replace("{style}", url_style)
    return html



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
