import cv2

from roboplatform import Robot
from camera import return_area_of_id

k_for_rotating = 0.5*5
k_for_sizing = 0.0005*40

needed_area = 129600//8
area_allowed_error = 400
angle_allowed_error = 30


robot = Robot((1920, 1080), "COM7", True)


while True:
    frame = robot.get_video_frame()

    cnt = return_area_of_id(frame, 0)

    if cnt is not None:
        M = cv2.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.circle(frame, (cx, cy), 15, (0, 255, 0), 2)
        # print(cv2.contourArea(cnt))
        # print(frame.shape)
        angle_error = 320-cx

        if abs(angle_error) > abs(angle_allowed_error):
            vr = - angle_error * k_for_rotating
            vl = angle_error * k_for_rotating
            # print(angle_error)
        else:
            area_error = needed_area - cv2.contourArea(cnt)
            if abs(area_error) > abs(area_allowed_error):
                vr = area_error * k_for_sizing
                vl = area_error * k_for_sizing
            else:
                vr = 0
                vl = 0

        print(int(vr), int(vl))

    cv2.imshow("frame", frame)

    # robot.send_to_motor(0, 0, 100)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

robot.end()

