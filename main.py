import cv2
import mediapipe as mp
import pyautogui

hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
# We will get screen size from pyautogui
screen_width, screen_height = pyautogui.size()

capture = cv2.VideoCapture(0)

while True:
    _, frame = capture.read()
    frame = cv2.flip(frame, 1)  # X -> frame and Y-> 1
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    print(hands)
    frame_height, frame_width, _ = frame.shape
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)  # To draw small landmarks on hands
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)  # Horizontal
                y = int(landmark.y * frame_height)  # Vertical
                print(x, y)

                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=40, color=(0, 255, 255))
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y
                    pyautogui.moveTo(index_x, index_y)  # Through x and y we can move the mouse cursor
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=40, color=(0, 255, 255))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y

    cv2.imshow('AI Virtual Mouse', frame)
    cv2.waitKey(1)
