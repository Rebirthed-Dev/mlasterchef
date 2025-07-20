from flask import Flask
import simulator
app = Flask(__name__)

@app.route('/')
def index():
    match = simulator.main()
    return '<h1>' + ''.join(str(x) for x in match.output) + '</h1>'