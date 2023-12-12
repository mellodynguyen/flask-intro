"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <title>Home Page</title>
      <body> 
        <h1>
          This is the Home Page
        </h1>
        Hi! This is the home page.
        <br>
        <a href=/hello>Click here!</a>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          

          Select a compliment:
          <input type="radio" name="compliment" value="nice" id="nice">
          <label for="nice">nice</label>

          <input type="radio" name="compliment" value="pretty" id="pretty">
          <label for="pretty">pretty</label>

          <input type="radio" name="compliment" value="smart" id="smart">
          <label for="smart">smart</label>

          <input type="submit" value="Submit">
        </form>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          Select an insult:
          <input type="radio" name="insult" value="stupid" id="stupid">
          <label for="stupid">stupid</label>

          <input type="radio" name="insult" value="ugly" id="ugly">
          <label for="ugly">ugly</label>

          <input type="radio" name="insult" value="bad" id="bad">
          <label for="bad">bad</label>

          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    

    # compliment = choice(AWESOMENESS)
    compliment = request.args.get("compliment")
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route("/diss")
def insult_person():
    player = request.args.get("person")

    insult = request.args.get("insult")
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
