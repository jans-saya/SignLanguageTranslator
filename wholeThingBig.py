import cv2
import math
from afterOptimisation import findposition

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    lmList = findposition(frame)

    wordlist = []

    if len(lmList) != 0:

        for lms in lmList:

            if lms[0] == 0:
                wristX, wristY = lms[1], lms[2]

            elif lms[0] == 1:
                thumbCMCX, thumbCMCY = lms[1], lms[2]

            elif lms[0] == 2:
                thumbMCPX, thumbMCPY = lms[1], lms[2]

            elif lms[0] == 3:
                thumbIPX, thumbIPY = lms[1], lms[2]

            elif lms[0] == 4:
                thumbTIPX, thumbTIPY = lms[1], lms[2]

            elif lms[0] == 5:
                indexMCPX, indexMCPY = lms[1], lms[2]

            elif lms[0] == 6:
                indexPIPX, indexPIPY = lms[1], lms[2]

            elif lms[0] == 7:
                indexDIPX, indexDIPY = lms[1], lms[2]

            elif lms[0] == 8:
                indexTIPX, indexTIPY = lms[1], lms[2]

            elif lms[0] == 9:
                middleMCPX, middleMCPY = lms[1], lms[2]

            elif lms[0] == 10:
                middlePIPX, middlePIPY = lms[1], lms[2]

            elif lms[0] == 11:
                middleDIPX, middleDIPY = lms[1], lms[2]

            elif lms[0] == 12:
                middleTIPX, middleTIPY = lms[1], lms[2]

            elif lms[0] == 13:
                ringMCPX, ringMCPY = lms[1], lms[2]

            elif lms[0] == 14:
                ringPIPX, ringPIPY = lms[1], lms[2]

            elif lms[0] == 15:
                ringDIPX, ringDIPY = lms[1], lms[2]

            elif lms[0] == 16:
                ringTIPX, ringTIPY = lms[1], lms[2]

            elif lms[0] == 17:
                pinkyMCPX, pinkyMCPY = lms[1], lms[2]

            elif lms[0] == 18:
                pinkyPIPX, pinkyPIPY = lms[1], lms[2]

            elif lms[0] == 19:
                pinkyDIPX, pinkyDIPY = lms[1], lms[2]

            elif lms[0] == 20:
                pinkyTIPX, pinkyTIPY = lms[1], lms[2]

        dist1A = math.hypot(pinkyDIPX - ringDIPX, pinkyDIPY - ringDIPY)
        dist2A = math.hypot(pinkyTIPX - pinkyMCPX, pinkyTIPY - pinkyMCPY)

        distB = math.hypot(ringDIPX - thumbTIPX, ringDIPY - thumbTIPY)

        #dist2V = math.hypot(ringPIPX - middlePIPX, ringPIPY - middlePIPY)
        #dist3V = math.hypot(pinkyDIPX - thumbTIPX, pinkyDIPY - thumbTIPY)
        #dist4V = math.hypot(middlePIPX - indexPIPX, middlePIPY - indexPIPY)

        dist1E = math.hypot(pinkyTIPX - ringTIPX, pinkyTIPY - ringTIPY)
        dist2E = math.hypot(ringTIPX - middleTIPX, ringTIPY - middleTIPY)
        dist3E = math.hypot(middleTIPX - indexTIPX, middleTIPY - indexTIPY)
        dist4E = math.hypot(middleTIPX - thumbTIPX, middleTIPY - thumbTIPY)

        dist1ZH = math.hypot(pinkyPIPX - ringPIPX, pinkyPIPY - ringPIPY)
        dist2ZH = math.hypot(ringPIPX - middlePIPX, ringPIPY - middlePIPY)
        dist3ZH = math.hypot(middlePIPX - indexPIPX, middlePIPY - indexPIPY)
        dist4ZH = math.hypot(indexPIPX - thumbIPX, indexPIPY - thumbIPY)

        dist1I = math.hypot(pinkyPIPX - ringPIPX, pinkyPIPY - ringPIPY)
        dist2I = math.hypot(ringPIPX - middlePIPX, ringPIPY - middlePIPY)
        dist3I = math.hypot(middlePIPX - indexPIPX, middlePIPY - indexPIPY)
        dist4I = math.hypot(indexPIPX - thumbIPX, indexPIPY - thumbIPY)

        dist2L = math.hypot(ringDIPX - middleDIPX, ringDIPY - middleDIPY)
        dist3L = math.hypot(ringDIPX - thumbIPX, ringDIPY - thumbIPY)
        dist4L = math.hypot(middlePIPX - indexPIPX, middlePIPY - indexPIPY)

        dist2M = math.hypot(ringDIPX - middleDIPX, ringDIPY - middleDIPY)
        dist3M = math.hypot(pinkyDIPX - thumbIPX, pinkyDIPY - thumbIPY)
        dist4M = math.hypot(middlePIPX - indexPIPX, middlePIPY - indexPIPY)

        distN = math.hypot(ringTIPX - thumbTIPX, ringTIPY - thumbTIPY)

        dist1O = math.hypot(pinkyTIPX - ringTIPX, pinkyTIPY - ringTIPY)
        dist2O = math.hypot(ringTIPX - middleTIPX, ringTIPY - middleTIPY)
        dist3O = math.hypot(middleTIPX - indexTIPX, middleTIPY - indexTIPY)
        dist4O = math.hypot(indexTIPX - thumbTIPX, indexTIPY - thumbTIPY)

        dist2P = math.hypot(ringDIPX - middleDIPX, ringDIPY - middleDIPY)
        dist3P = math.hypot(ringDIPX - thumbIPX, ringDIPY - thumbIPY)
        dist4P = math.hypot(middlePIPX - indexPIPX, middlePIPY - indexPIPY)

        distR = math.hypot(middleTIPX - thumbTIPX, middleTIPY - thumbTIPY)

        dist1C = math.hypot(pinkyTIPX - ringTIPX, pinkyTIPY - ringTIPY)
        dist2C = math.hypot(ringTIPX - middleTIPX, ringTIPY - middleTIPY)
        dist3C = math.hypot(middleTIPX - indexTIPX, middleTIPY - indexTIPY)
        dist4C = math.hypot(middleTIPX - thumbTIPX, middleTIPY - thumbTIPY)

        dist2T = math.hypot(ringPIPX - middleDIPX, ringPIPY - middleDIPY)
        dist3T = math.hypot(pinkyTIPX - thumbTIPX, pinkyTIPY - thumbTIPY)
        dist4T = math.hypot(middlePIPX - indexPIPX, middlePIPY - indexPIPY)

        dist1X = math.hypot(pinkyTIPX - ringTIPX, pinkyTIPY - ringTIPY)
        dist2X = math.hypot(ringTIPX - middleTIPX, ringTIPY - middleTIPY)
        dist4X = math.hypot(middleDIPX - thumbTIPX, middleDIPY - thumbTIPY)

        dist2YU = math.hypot(ringPIPX - middlePIPX, ringPIPY - middlePIPY)
        dist3YU = math.hypot(middlePIPX - indexPIPX, middlePIPY - indexPIPY)
        dist4YU = math.hypot(indexPIPX - thumbIPX, indexPIPY - thumbIPY)

        dist2SH = math.hypot(ringPIPX - middleDIPX, ringPIPY - middleDIPY)
        dist3SH = math.hypot(pinkyTIPX - thumbTIPX, pinkyTIPY - thumbTIPY)
        dist4SH = math.hypot(middlePIPX - indexPIPX, middlePIPY - indexPIPY)

        distROCK = math.hypot(middlePIPX - thumbTIPX, middlePIPY - thumbTIPY)

        dist1AE = math.hypot(pinkyTIPX - ringTIPX, pinkyTIPY - ringTIPY)
        dist2AE = math.hypot(ringTIPX - middleTIPX, ringTIPY - middleTIPY)
        dist4AE = math.hypot(middleDIPX - thumbTIPX, middleDIPY - thumbTIPY)

        dist1CH = math.hypot(pinkyTIPX - ringTIPX, pinkyTIPY - ringTIPY)
        dist2CH = math.hypot(ringTIPX - middlePIPX, ringTIPY - middlePIPY)
        dist3CH = math.hypot(middlePIPX - indexPIPX, middlePIPY - indexPIPY)
        dist4CH = math.hypot(indexPIPX - thumbIPX, indexPIPY - thumbIPY)

        dist1F = math.hypot(pinkyPIPX - ringPIPX, pinkyPIPY - ringPIPY)
        dist2F = math.hypot(ringPIPX - middlePIPX, ringPIPY - middlePIPY)
        dist3F = math.hypot(middlePIPX - indexPIPX, middlePIPY - indexPIPY)

        dist2YA = math.hypot(ringDIPX - middleDIPX, ringDIPY - middleDIPY)
        dist3YA = math.hypot(ringDIPX - thumbIPX, ringDIPY - thumbIPY)
        dist4YA = math.hypot(middlePIPX - indexPIPX, middlePIPY - indexPIPY)


        if (pinkyDIPY < wristY) and (pinkyDIPY > pinkyMCPY) and dist1A < 10 and dist2A < 60:
            cv2.putText(frame, 'А', (255,255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('А')
        elif (indexTIPY > indexMCPY and (indexTIPY < wristY) and (indexTIPY < middlePIPY) and (middlePIPY < ringDIPY) and
                (ringPIPY < pinkyPIPY) and (pinkyPIPY < pinkyDIPY) and distB < 30):
            cv2.putText(frame, 'Б', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('Б')
        #elif ((indexPIPY < wristY) and dist3V < 50 and dist2V < 15 and dist4V < 15):
            #cv2.putText(frame, 'V', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 1.0,
                        #(0, 0, 255), 1)
            #print('V')
        elif (indexMCPY > wristY) and (thumbTIPY > wristY) and (thumbTIPY < indexMCPY):
            cv2.putText(frame, 'Г', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('Г')
        elif dist1E < 13 and dist2E < 10 and dist3E < 10 and dist4E < 35:
            cv2.putText(frame, 'Е', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('Е')
        elif thumbTIPY > indexMCPY and dist4ZH < 30 and dist1ZH < 20 and dist2ZH < 20 and dist3ZH < 20 and thumbIPY < wristY:
            cv2.putText(frame, 'Ж', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('Ж')

        elif dist4I < 40 and dist1I > 25 and dist2I > 20 and dist3I < 20 and thumbIPY < wristY:
            cv2.putText(frame, 'И', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('И')

        elif ((indexMCPY > wristY) and dist3L < 40 and dist2L < 75 and dist4L > 50):
            cv2.putText(frame, 'Л', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('Л')

        elif ((indexMCPY > wristY) and dist3M < 40 and dist2M > 49 and dist4M > 40):
            cv2.putText(frame, 'М', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('М')

        elif distN < 20 and middleTIPY < middleMCPY:
            cv2.putText(frame, 'Н', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('Н')

        elif dist1O > 30 and dist2O > 30 and dist3O > 70 and dist4O < 35 and middleTIPY < middleDIPY:
            cv2.putText(frame, 'О', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('О')
        elif ((indexMCPY > wristY) and dist3P < 40 and dist2P < 65 and dist4P < 24):
            cv2.putText(frame, 'П', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('П')
        elif distR < 20 and ringTIPY < ringMCPY:
            cv2.putText(frame, 'Р', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('Р')
        elif dist1C < 25 and dist2C < 10 and dist3C < 10 and dist4C > 45:
            cv2.putText(frame, 'С', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('С')
        elif ((indexMCPY > wristY) and dist3T < 40 and dist2T < 50 and dist4T < 40):
            cv2.putText(frame, 'Т', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('Т')
        elif ((thumbTIPY < wristY) and (pinkyTIPY < pinkyMCPY) and
                (middleTIPY > indexMCPY) and (ringTIPY > indexMCPY) and (indexTIPY > indexMCPY) and
              pinkyTIPY < ringPIPY):
            cv2.putText(frame, 'У', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('У')
        elif indexTIPY < middlePIPY and dist1X < 15 and dist2X < 15 and dist4X < 25:
            cv2.putText(frame, 'Х', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('Х')
        elif pinkyTIPY < pinkyPIPY and dist4YU < 40 and dist2YU < 20 and dist3YU < 20 and thumbIPY < wristY:
            cv2.putText(frame, 'Ю', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('Ю')
        elif ((indexMCPY < wristY) and dist3SH < 30 and dist2SH < 55 and dist4SH < 35):
            cv2.putText(frame, 'Ш', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('Ш')
        elif ((indexTIPY < indexPIPY) and (pinkyTIPY < pinkyPIPY) and
                (middleTIPY > indexPIPY) and (ringTIPY > indexPIPY) and distROCK < 25):
            cv2.putText(frame, 'Ы', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('Ы')
        elif indexTIPY < middlePIPY and dist1AE < 15 and dist2AE < 15 and dist4AE > 25:
            cv2.putText(frame, 'Э', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('Э')
        elif dist4CH < 40 and dist3CH < 20 and thumbIPY < wristY and pinkyTIPY > pinkyMCPY and ringTIPY > ringMCPY:
            cv2.putText(frame, 'Ч', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('Ч')
        elif thumbTIPY < indexMCPY and dist1F < 20 and dist2F < 20 and dist3F < 20 and thumbTIPY < wristY:
            cv2.putText(frame, 'Ф', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('Ф')
        elif ((indexMCPX < wristX) and dist3YA < 60 and dist2YA < 75 and dist4YA < 55):
            cv2.putText(frame, 'Я', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 9.0,
                        (0, 0, 255), 5)
            print('Я')


        else:
            print('Sign not found')


    key = cv2.waitKey(1) & 0xFF
    cv2.imshow('Frame', frame)
    if key == ord("s"):
        break

