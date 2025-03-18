Emotion Recognition and Driver Safety Mechanism Using Python 🚗

Table of Contents

1 Features

2 Prerequisites

3 Installation

4 Usage

5 Technical Architecture

6 Troubleshooting

7 Development Setup

8 Testing

9 Contributing

10 License

11 Acknowledgments

12 FAQ

1 Features

🎥 Real-time face detection using Haar Cascades

😴 Drowsiness detection based on facial emotions

🔔 Instant alert system with buzzer sound

🖥️ Live monitoring through webcam

🚦 Head position alert for safety

📊 Detection of drowsy emotions such as tiredness, sadness, anger, and fear

2 Prerequisites

Requirement

Description

🐍 Python 3.11

Version 3.11.9 required

📸 Webcam

Built-in or external

💾 Storage

500MB+ free disk space

💻 RAM

4GB+ recommended

3 Installation

git clone https://github.com/Siddharthrk17/driver-safety-monitoring.git
cd driver-safety-monitoring
pip install -r requirements.txt

4 Usage

Run the script to start monitoring:

python driver_monitor.py

Press q to exit the monitoring system.

5 Technical Architecture

graph TD;
    A[Webcam] --> B[Frame Capture];
    B --> C[Gray Conversion];
    C --> D[Face Detection];
    D --> E{Face Found?};
    E -->|Yes| F[Emotion Analysis];
    E -->|No| G[Trigger Alert];
    F --> H{Drowsy Emotion Detected?};
    H -->|Yes| I[Trigger Buzzer];
    H -->|No| J[Display Status];
    J --> K[Live Feed Display];
    K --> L{Head Tilt Detected?};
    L -->|Yes| M[Trigger Head Position Alert];
    L -->|No| N[Continue Monitoring];

6 Troubleshooting

6.1 🎥 Webcam Not Detected

# Check if webcam is connected
ls /dev/video*

6.2 🐐 Performance Issues

# Reduce frame processing rate
python driver_monitor.py --fps 30

6.3 🔊 Buzzer Not Working

Ensure your system supports winsound (Windows only). If using another OS, replace with an alternative sound alert.

7 Development Setup

Clone the repository.

Set up a virtual environment and install dependencies.

Modify and test the code with sample video inputs.

8 Testing

Run the script with a webcam to verify real-time monitoring.

Test different emotional expressions to validate detection accuracy.

Simulate drowsy conditions to confirm alert triggers.

9 Contributing

Feel free to fork this repository and contribute to improving the system.

9.1 🔄 Contribution Workflow

📌 Create an issue describing your proposal

🍔 Fork the repository

🌱 Create a feature branch (git checkout -b feat/new-feature)

🐜 Commit changes with semantic messages

✅ Push to branch and create a PR

10 License

This project is licensed under the MIT License.

11 Acknowledgments

🎥 OpenCV for face detection

🤖 DeepFace for emotion analysis

🐍 Python community for supporting libraries

12 FAQ

12.1 🎮 Q1: Can I use this with recorded videos?

A: Yes! Modify the code to accept video files using the below code:

# Replace
cap = cv2.VideoCapture(0)

# With
cap = cv2.VideoCapture("input.mp4")

12.2 🎯 Q2: How to improve accuracy?

A: Follow these steps:

📸 Ensure proper face positioning in front of the camera.

💡 Maintain even lighting conditions.

👶️ Remove facial accessories like glasses or masks.

⚠️ Use higher resolution input (may impact performance).

12.3 📱 Q3: Does this work on mobile devices?

A: Currently, it is optimized for desktops. Mobile support requires adjustments to camera access and UI design.

