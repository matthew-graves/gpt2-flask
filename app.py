from flask import Flask, render_template, request, flash
from config import Config
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from websample import run_model

DEBUG = True
app = Flask(__name__)
app.config.from_object(Config)

class ReusableForm(Form):
    prompt = TextField('', validators=[validators.required()])

    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
        print(form.errors)
        result_text = ''
        if request.method == 'POST':
            prompt = request.form['prompt']
            print(prompt)

            if form.validate():
                result_text = run_model(prompt)
            else:
                flash('All Fields Are Required')

        return render_template('index.html', form=form, result_text=result_text)

if __name__ == "__main__":
    app.run()