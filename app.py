from flask import Flask, render_template, request, flash
from config import Config
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from web_model_generator import init_model, generate_response

DEBUG = True
app = Flask(__name__)
app.config.from_object(Config)

sess, context, saver, output, enc = init_model()

class ReusableForm(Form):
    prompt = TextField('', validators=[validators.required()])

    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
        result_text = ''
        if request.method == 'POST':
            prompt = request.form['prompt']
            print(prompt)

            if form.validate():
                result_text =  generate_response(prompt, sess, context, saver, enc, output)
                result_text = prompt + result_text
            else:
                flash('All Fields Are Required')

        return render_template('index.html', form=form, result_text=result_text)

if __name__ == "__main__":
    app.run()