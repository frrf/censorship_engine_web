from flask import Flask, render_template, request

# App config.
app = Flask(__name__)

##########################################################################

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/", methods=["POST"])
def user_input_post():
  text = request.form["text"]
  processed_text = text.upper()
  return render_template("index.html", text=text, processed_text = processed_text)



if __name__ == "__main__":
  app.run(debug=True)