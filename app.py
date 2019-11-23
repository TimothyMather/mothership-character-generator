import os
import random
import character_creator
from flask import Flask, render_template, send_file, current_app

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/generate', methods=['GET'])
def generate():
    character_creator.create_character()
    try:
        return send_file(os.path.join(current_app.root_path,'filled/mothership_character_sheet.pdf'))
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run()
