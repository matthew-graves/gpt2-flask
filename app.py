from flask import Flask, render_template, request, flash, redirect, url_for
import yaml
from config import Config
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from web_model_generator import init_model, generate_response
import gpt_mysql_connector


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
            if form.validate():
                result_text = generate_response(prompt, sess, context, saver, enc, output)
                result_text = prompt + result_text
                if gpt_mysql_connector.is_connected():
                    guid, still_available = gpt_mysql_connector.insert_gpt_prompt(prompt, result_text)
                    if still_available:
                        return redirect(url_for('load_guid', guid=guid))
                    else:
                        return render_template('index.html', form=form, result_text=result_text)
                else:
                    return render_template('index.html', form=form, result_text=result_text)
            else:
                flash('All Fields Are Required')

        return render_template('index.html', form=form, result_text=result_text)

    @app.route('/a/<guid>', methods = ['GET'])
    def load_guid(guid):
        form = ReusableForm(request.form)
        if gpt_mysql_connector.is_connected():
            response, still_available = (gpt_mysql_connector.get_gpt_prompt(guid))
            return render_template('index.html', form=form, result_text=response)
            if not still_available:
                db_available = False
        else:
            return render_template('index.html', form=form, result_text='Database Unavailable, Cannot Retrieve Saved Results')


if __name__ == "__main__":
    app.run()