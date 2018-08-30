from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello", methods=['POST', 'GET'])
def index():

	greeting = "Hello World"

	if request.method == "POST":
		name = request.form['name']
		greet = request.form['greet']
		greeting = f"{greet}, {name}"
		return render_template("index.html", greeting=greeting)
	else:
		return render_template("hello_form.html")

	#obtaining data via URL in browser http://localhost:5000/hello?name=Frank&greet=Hola
	# name = request.args.get('name', 'Nobody')
	# greet = request.args.get('greet', 'Hello')
	# greeting = f"{greet}, {name}"

	#default greeting generator
	# if name:
	# 	greeting = f"Hello, {name}"
	# else:
	# 	greeting = "Hello World"

	# return render_template("index.html", greeting=greeting)

# @app.route('/')
# def index():
# 	greeting = "Hello World"
# 	return render_template("index.html", greeting=greeting)

if __name__ == '__main__':
	app.run()