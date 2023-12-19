from flask import Flask

app = Flask(__name__, static_folder='static')
app.url_map.strict_slashes = False
app.jinja_options = app.jinja_options.copy()
app.jinja_options.update({
    'trim_blocks': True,
    'lstrip_blocks': True
})


app.config['DEBUG'] = True
app.config['SECRET_KEY'] = \
    '116333cef87fdb07af8e7a976ec8666a61bd7d7d75afbb32'


from app import views # noqa
