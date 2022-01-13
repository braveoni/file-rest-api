from flask import Flask
from web.config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

from . import views