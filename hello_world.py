from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Ohai, would you like to see a cute kitten?
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())

@app.route("/jedi/<f_name>/<l_name>")
def jedi_name(f_name, l_name):
    def convert_name(f_name, l_name):
        first = f_name[0:2]
        last = l_name[0:3]
        return last + first
    jedi = convert_name(f_name, l_name)
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Your Jedi name is:
            {}
    """
    return html.format(f_name.title(), jedi)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
