from flask import Flask
app = Flask(_name_)
@app.route('/')
def home():
    return "Welcome to Online Stock Trading System"
if _name_ == '_main_':
    app.run(debug=True)
