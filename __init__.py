from distutils.log import debug
from flask import Flask

app = Flask(__name__)
app.secret_key = "keep it shecret, keep it shafe"