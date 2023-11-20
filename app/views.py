from app import app


@app.route('/')
def home():
    return "Thanyared says 'Hello world!'"
