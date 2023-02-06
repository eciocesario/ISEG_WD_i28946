from flask import render_template, request
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method=="POST":
        name = request.form["name"]
        return "Hello" + name
    return render_template("form.html")
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class NameForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField ("submit")
    
