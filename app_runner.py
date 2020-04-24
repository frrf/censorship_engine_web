from flask import Flask, render_template, request

# App config.
app = Flask(__name__)

##########################################################################

#render index
@app.route("/")
def index():
  return render_template("index.html")

#censor_text function
#list of censored words
profane_terms = ["fuck"]

#censor multiple
def censor_text(usrtxt):
  censored_text = usrtxt
  for term in profane_terms:
    location = censored_text.find(term)
    if location == -1:
      continue
    else:
      lot = len(term)
      target = censored_text[location:location+lot]
      censored_text = censored_text.replace(term, '####')
  return censored_text

@app.route("/", methods=["POST"])
def user_input_post():
  text = request.form["text"]
  processed_text = censor_text(text)
  return render_template("index.html", text=text, processed_text = processed_text)



if __name__ == "__main__":
  app.run(debug=True)