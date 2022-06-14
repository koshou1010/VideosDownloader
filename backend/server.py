from flask import Flask, render_template, jsonify, request
import os
import backend.src.utils as utils




template_dir = os.path.abspath('./frontend/templates')
static_dir = os.path.abspath('./frontend/static')
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir, static_url_path='')

@app.route("/", methods=['GET', 'POST'])
def index():   
    if request.method == 'POST':
      if request.json['btn'] == 'download':
        input_url = request.json['input_url']
        utils.doing_download(utils.extractor_selector(input_url))
        
    return render_template('index.html')

def start_server():
    app.run(port = 5000)
    
    
if __name__ =='__main__':
    start_server()

