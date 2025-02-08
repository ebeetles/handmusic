import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hand = mp_hands.Hands()

while True:
    success, frame = cap.read()
    if success:
        RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hand.process(RGB_frame)
        
        if result.multi_hand_landmarks and result.multi_handedness:
            for hand_idx, (hand_landmarks, handedness) in enumerate(zip(result.multi_hand_landmarks, result.multi_handedness)):
                hand_label = handedness.classification[0].label  # "Left" or "Right"
                print(f"Hand {hand_idx + 1} ({hand_label}):")
                
                for idx, landmark in enumerate(hand_landmarks.landmark):
                    print(f"  Landmark {idx}: (x={landmark.x:.4f}, y={landmark.y:.4f}, z={landmark.z:.4f})")
                
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
        cv2.imshow("capture image", frame)
        if cv2.waitKey(1) == ord('q'):
            break
