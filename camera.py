import cv2
import numpy as np


def find_aruco_marker(frame):
    params = cv2.aruco.DetectorParameters()
    dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    detector = cv2.aruco.ArucoDetector(dictionary=dict, detectorParams=params)
    (corners, ids, rejected) = detector.detectMarkers(frame)


    cv2.aruco.drawDetectedMarkers(frame, corners, ids, (0, 255, 0))

    return frame

def return_area_of_id(frame, id):
    params = cv2.aruco.DetectorParameters()
    thresh_constant = 15
    thresh_win_size_step = 10
    thresh_win_size_min = 30
    thresh_win_size_max = 52
    params.adaptiveThreshConstant = thresh_constant
    params.adaptiveThreshWinSizeStep = thresh_win_size_step
    params.adaptiveThreshWinSizeMin = thresh_win_size_min
    params.adaptiveThreshWinSizeMax = thresh_win_size_max
    dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50)
    detector = cv2.aruco.ArucoDetector(dictionary=dict, detectorParams=params)
    (corners, ids, rejected) = detector.detectMarkers(frame)
    # print(ids)

    if ids is None:
        return None
    else:
        if id in list(ids)[0]:
            return corners[list(ids[0]).index(id)][0]
        return None

