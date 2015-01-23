from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def default():
    html = """
        <h1>Hi!  You've reached the landing page.</h1>
        <p>Modify your URL to reach the Jedi and Hello applications.</p>
        <p>Simply add /hello, /hello/\<your_name\>, or you can check out the</p>
        <p>Jedi name at /jedi/\<firstname\>/\<lastname\>."</p>
    """
    return html


@app.route("/hello")
def hello_world():
    return "Hello World!"


@app.route("/hello/<name>")
def hello_person(name):
    return render_template('hello.html',
                           name=name,
                           url="http://placekitten.com/g/200/300")


@app.route("/jedi/<f_name>/<l_name>")
def jedi_name(f_name, l_name):
    def convert_name(f_name, l_name):
        first = f_name[0:2]
        last = l_name[0:3]
        return last + first
    jedi = convert_name(f_name, l_name)
    return render_template('jedi.html',
                           name=jedi,
                           l_name=l_name,
                           f_name=f_name,
                           url="http://img1.wikia.nocookie.net/__cb20090320221709/starwars/images/5/59/ThreeJedi.jpg")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
