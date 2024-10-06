# EyeTrack
Eye-Controlled Mouse with Blink to Click
This project implements an Eye-Controlled Mouse using a webcam and facial landmark detection. It allows users, especially individuals with limited hand mobility, to control the mouse pointer using their eyes and perform mouse clicks by blinking. The project utilizes OpenCV, Mediapipe, and PyAutoGUI for computer vision and mouse control.

Features
Eye Movement Control: Moves the mouse cursor by tracking the user's eye movements in real-time.
Blink for Click: Detects blinks by analyzing specific facial landmarks and simulates a mouse click when the user blinks.
Hands-Free Interaction: Provides a hands-free solution for controlling the computer, making it an assistive tool for people with physical disabilities.
Visual Feedback: Displays visual markers on the face to provide feedback for eye tracking and blink detection.
How It Works
Face Landmark Detection: The program captures video input from the webcam and uses Mediapipe's FaceMesh solution to identify key facial landmarks.
Mouse Movement: By tracking landmarks around the eyes (specifically around the iris), the mouse cursor is moved proportionally to the user's gaze.
Blink Detection: The program detects blinks by measuring the vertical distance between specific landmarks on the user's left eye. If the eye remains closed for a short period, the program simulates a mouse click.
Real-Time Updates: The system continuously updates the user's gaze direction and blink state, enabling smooth and responsive control.
Technology Stack
OpenCV: Used for capturing video from the webcam and displaying frames with visual feedback.
Mediapipe: A machine learning framework used for detecting facial landmarks, including eye and iris tracking.
PyAutoGUI: A library that allows programmatic control of the mouse cursor and simulates clicks.
Requirements
Before running the project, make sure you have the following dependencies installed:

bash
Copy code
pip install opencv-python mediapipe pyautogui
Usage
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/eye-controlled-mouse.git
Navigate to the project directory:
bash
Copy code
cd eye-controlled-mouse
Run the script:
bash
Copy code
python eye_controlled_mouse.py
Control the mouse:
Move the mouse with your eyes.
Blink to click!
Important Notes
Ensure that your webcam is working and accessible by OpenCV.
The blink sensitivity may need to be fine-tuned depending on lighting and the distance between the user and the camera.
The script is currently configured for left eye detection. You can extend it to detect blinking from both eyes.
Future Improvements
Eye Calibration: Implement calibration to increase the accuracy of eye tracking for different users.
Dual Eye Detection: Add support for detecting blinks from both eyes.
Custom Actions: Map additional eye gestures (e.g., double blink) to other mouse actions like right-click or scrolling.
