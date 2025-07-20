from flask import Flask
import simulator
app = Flask(__name__)

@app.route('/')
def index():
    match = simulator.main()
    return '<br>'.join(match.output)