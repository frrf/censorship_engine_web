from flask import Flask, render_template, url_for, request
from censorship_engine import censor_text

# App config.
app = Flask(__name__)
app.static_folder = 'static'

#render index
@app.route("/")
def index():
  return render_template("index.html")

@app.route("/", methods=["POST"])
def user_input_post():
  text = request.form["text"]
  processed_text = censor_text(text)
  return render_template("result.html", text=text, processed_text = processed_text)

@app.route("/#")
def again():
  return render_template("again.html")

@app.route("/#", methods=["POST"])
def user_input_post_again():
  text = request.form["text"]
  processed_text = censor_text(text)
  return render_template("result.html", text=text, processed_text = processed_text)

if __name__ == "__main__":
  app.run(debug=True)