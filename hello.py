from flask import Flask, render_template, request
from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['API'], os.environ['DOMAIN'], os.environment['EMAIL'])
import requests
app = Flask("adpicturebooks")
# app = Flask("lina_app")

def send_simple_message(email):
    return requests.post(
        s3.DOMAIN+"messages",
        auth=("api", s3.API),
        data={"from": "Excited User <"+s3.DOMAIN+">",
              "to": [s3.EMAIL],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

@app.route("/")
def hello():
	return "Hi"

@app.route("/<name>")
def hello_someone(name):

	return render_template("hello.html", name=name.title())

@app.route("/signup", methods=["POST"])
def sign_up():
  # print "Thank you!"
  # return "bla bla bla"
  form_data = request.form
  print form_data["email"]
  send_simple_message(email)
  return "Email Sent to: {}".format(email)
  # return render_template('hello.html',message="back to basics");
app.run(debug=True)

