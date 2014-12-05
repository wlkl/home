from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='abra-kadabra',
    USERNAME='wlkl',
    PASSWORD='wen1k0'
))