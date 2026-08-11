# 🚨 Smart Campus Surveillance and Guidance System

A Python-based Smart Campus Surveillance and Guidance System designed to monitor a campus environment using camera-based object detection, simulated motion sensors, real-time alerts, and a web-based dashboard.

## 📌 Project Overview

The system combines:

- 📹 Live camera monitoring
- 🔍 Object detection
- 🚨 Motion detection alerts
- 🌐 Flask web dashboard
- 📡 Simulated IoT sensor monitoring

The application uses a webcam as the video source and processes the video using TensorFlow and OpenCV. Detected video frames are streamed to a Flask web dashboard.

## ✨ Features

- 📹 Real-time webcam monitoring
- 🔍 Person detection
- 🧠 TensorFlow-based object detection
- 🚨 Motion sensor simulation
- 📧 Simulated email alerts
- 🌐 Flask web dashboard
- 📊 Centralized campus monitoring

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Flask | Web application and dashboard |
| TensorFlow | Object detection |
| SSD MobileNet V2 FPNLite | Object detection model |
| OpenCV | Camera and video processing |
| NumPy | Numerical processing |
| HTML | Dashboard interface |

## 🧠 Object Detection

The project uses the **SSD MobileNet V2 FPNLite 320x320** TensorFlow SavedModel for object detection.

Currently, the detection configuration includes:

```python
category_index = {1: 'person'}
```

The system processes frames from the webcam and checks detection confidence scores. :contentReference[oaicite:1]{index=1}

## 📂 Project Structure

```text
Smart-Campus-Surveillance-and-Guidance-System/
│
├── model/
│   └── ssd_mobilenet_v2_fpnlite_320x320/
│       └── saved_model/
│
├── templates/
│   └── dashboard.html
│
├── alerts.py
├── app.py
├── camera.py
├── sensors.py
├── requirements.txt
├── .gitignore
└── README.md
```

> The `model/` directory is required by `camera.py` because the TensorFlow SavedModel is loaded from this path. :contentReference[oaicite:2]{index=2}

## 🔄 System Workflow

```text
              Webcam
                 │
                 ▼
        ┌─────────────────┐
        │  OpenCV Camera  │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ TensorFlow SSD  │
        │ Object Detection│
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Detection Result│
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Flask Dashboard │
        └─────────────────┘


        Motion Sensor Simulation
                 │
                 ▼
        ┌─────────────────┐
        │ sensors.py      │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Alert Generation│
        └─────────────────┘
```

## 🖥️ Application Modules

### 1. Camera Monitoring

The camera module opens the system webcam using OpenCV and continuously captures frames. :contentReference[oaicite:3]{index=3}

### 2. Object Detection

Captured frames are passed to the TensorFlow detection model. The system checks detection scores and identifies configured objects such as people. :contentReference[oaicite:4]{index=4}

### 3. Web Dashboard

The Flask application provides the main dashboard page and a video streaming endpoint.

The dashboard is available through:

```text
/
```

and the video stream through:

```text
/video_feed
```

:contentReference[oaicite:5]{index=5}

### 4. Motion Sensor Simulation

The sensor module simulates motion detection using randomly generated sensor states. When motion is detected, an alert is triggered. :contentReference[oaicite:6]{index=6}

### 5. Alert System

The alert module currently provides a simulated email alert by printing the alert message to the console. :contentReference[oaicite:7]{index=7}

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/SuriyaSK19092005/Smart-Campus-Surveillance-and-Guidance-System.git
```

### 2. Navigate to the Project

```bash
cd Smart-Campus-Surveillance-and-Guidance-System
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 📦 Required Dependencies

The project requires:

```text
Flask
TensorFlow
OpenCV
NumPy
```

These dependencies are listed in `requirements.txt`.

## 🤖 Model Setup

The application expects the TensorFlow SavedModel at:

```text
model/ssd_mobilenet_v2_fpnlite_320x320/saved_model
```

Make sure the required model files are available at this location before running the application.

## ▶️ Running the Application

Start the Flask application:

```bash
python app.py
```

The application starts the motion sensor simulation in a background thread and launches the Flask server. :contentReference[oaicite:8]{index=8}

Open the local Flask address displayed in the terminal.

## 📹 Camera Requirements

The camera module currently uses:

```python
cv2.VideoCapture(0)
```

Therefore, a webcam/camera connected to the computer is required for live video monitoring. :contentReference[oaicite:9]{index=9}

## 🚨 Alert System

The current alert system is a simulation.

When motion is detected, the system generates:

```text
[ALERT] Motion detected near Lab Block! — Email Sent (Simulated)
```

The alert is currently printed to the console rather than sent through a real email service. :contentReference[oaicite:10]{index=10}

## 🎯 Project Objectives

- Improve campus surveillance
- Monitor campus environments through a camera
- Detect people using computer vision
- Simulate motion sensor monitoring
- Generate real-time alerts
- Provide a centralized web dashboard
- Demonstrate the integration of computer vision, web development, and IoT concepts

## 🚀 Future Enhancements

The following features can be added in future versions:

- 👥 Advanced person and object detection
- 🔥 Fire and smoke detection
- 🚨 Real email/SMS notifications
- 📡 Integration with real IoT sensors
- 🗄️ Database integration
- 📊 Detection and alert history
- 👤 Face recognition
- 👥 Crowd detection
- 📱 Mobile application
- ☁️ Cloud deployment
- 📈 Analytics and reporting

## 📸 Project Screenshots

Screenshots can be added here after uploading them to the repository.

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Object Detection

![Object Detection](screenshots/object-detection.png)

### Alert System

![Alert System](screenshots/alerts.png)

## 🔐 Security

Do not upload sensitive information such as:

- Passwords
- API keys
- Email credentials
- Secret keys
- `.env` files

Use `.gitignore` to prevent sensitive or unnecessary files from being committed.

## 👨‍💻 Author

**Suriya SK**

GitHub:

https://github.com/SuriyaSK19092005

## 📄 License

This project was developed for educational and academic purposes.
