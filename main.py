from flask import Flask, request

from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {
                    background-color: #eee
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            <form method="POST">
                <label for="rot-box">Rotate by:</label>
                <input id="rot-box" type="text" name="rot" value="0" />

                <input type="textarea" name ="text" />

                <input type="submit" />
            </form>
        </body>
    </html>
"""

@app.route("/" , methods=["POST"])
def index():
    form_value = request.form["text"]
    return form_value

@app.route("/" , methods=["POST"])
def encrypt():
    rot_var = int(request.form["rot"])
    text_var = request.form["text"]

    garbled = str(rotate_string(text_var, rot_var))

    return garbled

app.run()