import picamera
import time
import io
from flask import Flask, send_file, render_template

app = Flask(__name__)

def send_screenshot(resolution=(1280, 720)):
    with picamera.PiCamera() as camera:
        camera.hflip = True
        camera.vflip = True
        camera.resolution = resolution

        stream = io.BytesIO()
        camera.capture(stream, format='png')
        stream.seek(0)

        return send_file(stream,
                mimetype="image/png")

@app.route("/fig/screenshot")
def screenshot():
    return send_screenshot()

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
