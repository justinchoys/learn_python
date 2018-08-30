from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello")
def index():
	name = request.args.get('name', 'Nobody')
	greet = request.args.get('greet', 'Hello')
	greeting = f"{greet}, {name}"

	# if name:
	# 	greeting = f"Hello, {name}"
	# else:
	# 	greeting = "Hello World"

	return render_template("index.html", greeting=greeting)

# @app.route('/')
# def index():
# 	greeting = "Hello World"
# 	return render_template("index.html", greeting=greeting)

if __name__ == '__main__':
	app.run()