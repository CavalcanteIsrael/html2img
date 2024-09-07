from html2image import Html2Image
from flask import Flask, request, jsonify, send_from_directory

# Create Flask API

app = Flask(__name__)

app.config['SERVER_NAME'] = 'uncraft.com.br:9000'

@app.route ("/html2img", subdomain='html2image', methods=["POST"])
def html2img():
    html = request.form.get("html")
    css = request.form.get("css")
    
    hti = Html2Image(size=(900, 900))

    hti.screenshot(html_str=html, css_str=css, save_as='test_page.png')
    
    return send_from_directory("""""","test_page.png", as_attachment = True)
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9000)