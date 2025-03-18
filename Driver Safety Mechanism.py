import cv2
from deepface import DeepFace
import numpy as np
import tensorflow as tf
import winsound  # For buzzer sound on Windows
from cv2 import dnn

# Suppress TensorFlow warnings
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

def beep_alert():
    duration = 1000  # milliseconds
    freq = 1000  # Hz
    winsound.Beep(freq, duration)

def monitor_driver():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 100)  # Amplify video processing to 90Hz
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
   
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
   
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break
       
        frame = cv2.convertScaleAbs(frame, alpha=1.5, beta=0)  # Amplify video output
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
       
        if len(faces) == 0:
            cv2.putText(frame, "FACE NOT FOUND!", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            beep_alert()
       
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        try:
            result = DeepFace.analyze(rgb_frame, actions=['emotion'], enforce_detection=False)
            for i, face in enumerate(faces):
                x, y, w, h = face
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
               
                if i < len(result) and 'dominant_emotion' in result[i]:
                    dominant_emotion = result[i]['dominant_emotion']
                    confidence = result[i].get('emotion', {}).get(dominant_emotion, 0)
                   
                    # Display detected emotion
                    cv2.putText(frame, f"{dominant_emotion} ({confidence:.1f}%)", (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                   
                    # Check for drowsiness indicators
                    drowsy_emotions = ['tired', 'sad', 'angry', 'fear', 'disgust']
                    if dominant_emotion in drowsy_emotions and confidence > 50:
                        cv2.putText(frame, "DROWSINESS ALERT!", (x, y + h + 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                        beep_alert()
               
                # Check for head tilt (approximate logic, requires further refinement with pose estimation)
                if y + h > frame.shape[0] * 0.75:
                    cv2.putText(frame, "HEAD POSITION ALERT!", (x, y + h + 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                    beep_alert()
       
        except Exception as e:
            print("Face not detected, skipping frame.")

        cv2.imshow("Driver Safety Monitoring", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    monitor_driver()
