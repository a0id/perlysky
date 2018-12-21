from flask import Flask, render_template, flash, request, redirect, url_for, session, send_from_directory, logging
app = Flask(__name__, static_url_path='/static')
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, FileField
from werkzeug.utils import secure_filename
import random, os
from switch import Switch

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

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(
        host='0.0.0.0',
        port='3030',
        debug=True
    )