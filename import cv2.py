import cv2
import mediapipe as mp
import pyautogui

# Initialize camera and face mesh
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

while True:
    # Read frame from camera
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)  # Flip the frame for a mirror-like effect
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect face landmarks
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks

    frame_h, frame_w, _ = frame.shape

    # If face landmarks are detected
    if landmark_points:
        landmarks = landmark_points[0].landmark

        # Loop through specific landmarks around the eyes (for mouse control)
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)  # Draw small green circles for visualization
            if id == 1:  # Move the mouse based on landmark 475
                screen_x = screen_w / frame_w * x
                screen_y = screen_h / frame_h * y
                pyautogui.moveTo(screen_x, screen_y)

        # Detect blinking using the vertical distance between specific left eye landmarks
        left_eye_landmarks = [landmarks[145], landmarks[159]]  # Landmarks for left eye blink detection

        # Get the coordinates of the two landmarks for the left eye
        left_eye_points = []
        for lm in left_eye_landmarks:
            x = int(lm.x * frame_w)
            y = int(lm.y * frame_h)
            left_eye_points.append((x, y))
            cv2.circle(frame, (x, y), 3, (0, 255, 255), -1)  # Draw yellow circles on the left eye landmarks

        # Calculate the vertical distance between the two eye landmarks
        if abs(left_eye_landmarks[0].y - left_eye_landmarks[1].y) < 0.004:
            pyautogui.click()  # Perform a click if blink is detected
            pyautogui.sleep(0.5)  # Short sleep to avoid multiple clicks from one blink

    # Display the frame with landmarks
    cv2.imshow('Eye Controlled Mouse', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close OpenCV window
cam.release()
cv2.destroyAllWindows()
