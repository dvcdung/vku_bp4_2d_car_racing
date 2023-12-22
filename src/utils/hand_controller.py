import math
import cv2
from threading import Thread
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

class VideoGet:
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):
        Thread(target=self.get, args=()).start()
        return self

    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()
                          
    def stop(self):
        self.stopped = True 

class VideoShow:
    def __init__(self, frame=None):
        self.frame = frame
        self.stopped = False

    def start(self):
        Thread(target=self.show, args=()).start()
        return self

    def show(self):
        while not self.stopped:
            if self.frame is not None:
                height, width, _ = self.frame.shape
                new_height = int(height * 0.5)
                new_width = int(width * 0.5)
                resized_frame = cv2.resize(self.frame, (new_width, new_height))

                # Display the resized frame
                cv2.imshow("Video", cv2.flip(resized_frame, 1))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.stopped = True

    def stop(self):
        self.stopped = True   
       
class ThreadVideo:
    def __init__(self):
        source=0
        self.video_getter = VideoGet(source).start()
        self.video_shower = VideoShow(self.video_getter.frame).start()
        self.dist = 100

    def start(self):
        Thread(target=self.show, args=()).start()
        return self   

    def show(self):
        with mp_hands.Hands(
        static_image_mode=False,
        model_complexity=1,
        max_num_hands=2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
            while True:
                if self.video_getter.stopped or self.video_shower.stopped:
                    self.video_shower.stop()
                    self.video_getter.stop()
                    break

                image = self.video_getter.frame
                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = hands.process(image)

                # Draw the hand annotations on the image.
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                dist = 0
                height, width, _ = image.shape
                x1, y1 = 0, height//2
                x2, y2 = width, height//2

                cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

                first_hand_index = None
                first_hand_label = None
                if results.multi_hand_landmarks and len(results.multi_hand_landmarks) == 2:
                    for idx, hand in enumerate(results.multi_hand_landmarks):
                        mp_drawing.draw_landmarks(
                            image,
                            hand,
                            mp_hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style())
                        lm_hand = results.multi_handedness[idx].classification[0].label
                        
                        if first_hand_index is None:
                            first_hand_index = idx
                            first_hand_label = lm_hand
                        
                        if first_hand_label == "Left":
                            hand_landmarks_1 = results.multi_hand_landmarks[1].landmark
                            hand_landmarks_2 = results.multi_hand_landmarks[0].landmark
                            for id, lm in enumerate(hand.landmark):
                                h, w, _ = image.shape
                                x, y = int(lm.x * w), int(lm.y * h)
                                hand_1_point1 = (int(hand_landmarks_1[8].x * w), int(hand_landmarks_1[8].y * h))
                                hand_2_point1 = (int(hand_landmarks_2[8].x * w), int(hand_landmarks_2[8].y * h))
                                if id == 8:
                                    cv2.circle(image, (x, y), 10, (0, 255, 0), cv2.FILLED)
                                    cv2.line(image, hand_1_point1, hand_2_point1, (0, 255, 0), 2)


                            if hand_landmarks_1[8].y < 0.5 and hand_landmarks_2[8].y < 0.5 or hand_landmarks_2[8].y > 0.5 and hand_landmarks_1[8].y > 0.5:
                                # up
                                dist = 0
                            elif hand_landmarks_1[8].y > 0.5 and hand_landmarks_2[8].y < 0.5:
                                # right
                                dist = 1
                            elif hand_landmarks_1[8].y < 0.5 and hand_landmarks_2[8].y > 0.5:
                                # left
                                dist = 2
                            else:
                                # stop
                                dist = 3
                        
                        elif first_hand_label == "Right":
                            hand_landmarks_1 = results.multi_hand_landmarks[0].landmark
                            hand_landmarks_2 = results.multi_hand_landmarks[1].landmark
                            for id, lm in enumerate(hand.landmark):
                                h, w, _ = image.shape
                                x, y = int(lm.x * w), int(lm.y * h)
                                hand_1_point1 = (int(hand_landmarks_1[8].x * w), int(hand_landmarks_1[8].y * h))
                                hand_2_point1 = (int(hand_landmarks_2[8].x * w), int(hand_landmarks_2[8].y * h))
                                if id == 8:
                                    cv2.circle(image, (x, y), 10, (0, 255, 0), cv2.FILLED)
                                    cv2.line(image, hand_1_point1, hand_2_point1, (0, 255, 0), 2)

                            if hand_landmarks_1[8].y < 0.5 and hand_landmarks_2[8].y < 0.5 or hand_landmarks_2[8].y > 0.5 and hand_landmarks_1[8].y > 0.5:
                                # up
                                dist = 0
                            elif hand_landmarks_1[8].y > 0.5 and hand_landmarks_2[8].y < 0.5:
                                # right
                                dist = 1
                            elif hand_landmarks_1[8].y < 0.5 and hand_landmarks_2[8].y > 0.5:
                                # left
                                dist = 2
                            else:
                                # stop
                                dist = 3

                else:
                    # stop
                    dist = 3     

                self.video_shower.frame = image
                self.dist = dist

# if __name__ == '__main__':   
#     threadVideo().start()
