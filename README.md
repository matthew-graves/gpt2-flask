# gpt2-flask
Nonsense Flask App for GPT-2 Phrase Generator

**Instructions for use:**

Recommend using virtualenv over systemwide installs

**Create Virtual Environment:**

python3 -m venv "environment name"

**Activate Virtual Env:**

source "environment name"/env/activate

**to deactivate, type deactivate**

**Install python packages via pip:**

pip3 install -r requirements.txt

**Download 345M Model to models folder:**

See instructions: https://github.com/openai/gpt-2

Place 345M folder in models folder

**To run code for testing:**

flask run

**To run code in prod environment with gunicorn:**

gunicorn -w 1 -b 0.0.0.0:8000 app:app -t 120

Since this uses tensorflow, tensorflow-gpu is compatible but not required. 
