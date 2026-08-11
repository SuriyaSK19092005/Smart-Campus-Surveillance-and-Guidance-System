from flask import Flask, render_template, Response
from camera import detect_objects
import threading
from sensors import motion_sensor_check

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/video_feed')
def video_feed():
    return Response(detect_objects(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    threading.Thread(target=motion_sensor_check, daemon=True).start()
    app.run(debug=True)