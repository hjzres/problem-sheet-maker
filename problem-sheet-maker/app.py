from flask import Flask, render_template, request # type: ignore

app = Flask(__name__)

@app.route("/")
def home():
    pass

if __name__ == "__main__":
    app.run("localhost", 8000, debug=True)