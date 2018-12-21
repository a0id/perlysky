from flask import Flask, render_template, flash, request, redirect, url_for, session, send_from_directory, logging
app = Flask(__name__, static_url_path='/static')
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, FileField
from werkzeug.utils import secure_filename
import random, os, json
from switch import Switch, process
from add import Add

class EncryptForm(Form):
    text = TextAreaField("", [validators.DataRequired()])

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/decrypt", methods=["GET", "POST"])
def decrypt():
    if request.method == "POST":
        form = request.form
        text = form["input"]
        m_processed = Switch(text)
        processed = m_processed.switch()
        print("processed:", processed)
        return render_template("decrypt.html", processed=processed, raw=text)
    return render_template("decrypt.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        form = request.form
        
        perly = process(form["perly"])
        english = form["english"]
        name = form["name"]
        with open("static/names.txt", "a+") as f:
            f.write(name + "\n")
        Add(perly, english)
    return render_template("add.html")
@app.route("/view", methods=["GET"])
def view():
    phrases = { }
    header = ' \
        <table class="table"> \
            <thead> \
                <tr> \
                    <th scope="col">Perly Text</th> \
                    <th scope="col">English</th> \
                </tr> \
            </thead> \
            <tbody>'
    content = ''
    
    with open("static/phrases.json", "r") as f:
        phrases = json.loads(f.read())
    for phrase in phrases:
        content += "<tr>"
        content += '<td>' + phrase + '</td>'
        content += '<td>' + phrases[phrase] + '</td>'
        content += "</tr>"
    footer = "</tbody></table>"
    


    # <tr> \
    #             <td>Mark</td> \
    #             <td>Otto</td>
    #             <td>@mdo</td>
    #         </tr>
    #     "
    rendered = header + content + footer
    print(rendered)
    return render_template("view.html", rendered = rendered)

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(
        host='0.0.0.0',
        port='3030',
        debug=True
    )