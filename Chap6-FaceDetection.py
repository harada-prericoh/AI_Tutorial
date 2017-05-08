# #Practice1
# import cv2
# cap = cv2.VideoCapture(0)
# cap.set(3, 1280)  # 横サイズ
# cap.set(4, 1024)  # 縦サイズ
#
# while (True):
#     ret, frame = cap.read()
#     cv2.imshow("webcam", frame)
#
#     key = cv2.waitKey(100) & 0xFF
#     # q を押したら終了
#     if key == ord('q'):
#         break

# #Practice2
# import cv2
# import numpy
#
# cap=cv2.VideoCapture(0)
# cap.set(3,1280)
# cap.set(4,1024)
#
# gamma=1.8
# lookUpTable = numpy.zeros((256,1),dtype='uint8')
# for i in range(256):
#     lookUpTable[i][0]=255*pow(float(i)/255,1.0/gamma)
#
# while(True):
#     ret,frame=cap.read()
#     frame = cv2.flip(frame,1)
#     frame = cv2.LUT(frame,lookUpTable)
#
#     cv2.imshow("webcam",frame)
#
#     key = cv2.waitKey(100)&0xFF
#
#     if key == ord('q'):
#         break

# #Practice3
# import cv2
# import numpy
# import dlib
#
# cap=cv2.VideoCapture(0)
# cap.set(3,1280)
# cap.set(4,1024)
#
# gamma=1.8
# lookUpTable = numpy.zeros((256,1),dtype='uint8')
# for i in range(256):
#     lookUpTable[i][0]=255*pow(float(i)/255,1.0/gamma)
#
# detector = dlib.get_frontal_face_detector()
#
# while(True):
#     ret,frame=cap.read()
#     frame = cv2.flip(frame,1)
#     frame = cv2.LUT(frame,lookUpTable)
#
#     dets = detector(frame)
#     for d in dets:
#         cv2.rectangle(frame,(d.left(),d.top()),(d.right(),d.bottom()),(0,0,255),1)
#
#
#     cv2.imshow("webcam",frame)
#
#     key = cv2.waitKey(100)&0xFF
#
#     if key == ord('q'):
#         break

#Practice4
import cv2
import numpy
import dlib

cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,1024)

gamma=1.8
lookUpTable = numpy.zeros((256,1),dtype='uint8')
for i in range(256):
    lookUpTable[i][0]=255*pow(float(i)/255,1.0/gamma)

detector = dlib.get_frontal_face_detector()
predictor_path = "..\\dlib_data\\shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_path)

while(True):
    ret,frame=cap.read()
    frame = cv2.flip(frame,1)
    frame = cv2.LUT(frame,lookUpTable)

    dets = detector(frame)
    for d in dets:
        cv2.rectangle(frame,(d.left(),d.top()),(d.right(),d.bottom()),(0,0,255),1)

        shape = predictor(frame,d)
        for x in range(0,16): cv2.line(frame, (shape.part(x).x,shape.part(x).y), (shape.part(x+1).x,shape.part(x+1).y),(0,0,255),1)
        for x in range(17,21): cv2.line(frame, (shape.part(x).x,shape.part(x).y), (shape.part(x+1).x,shape.part(x+1).y),(0,0,255),1)
        for x in range(22,26): cv2.line(frame, (shape.part(x).x,shape.part(x).y), (shape.part(x+1).x,shape.part(x+1).y),(0,0,255),1)
        for x in range(27,30): cv2.line(frame, (shape.part(x).x,shape.part(x).y), (shape.part(x+1).x,shape.part(x+1).y),(0,0,255),1)
        for x in range(31,35): cv2.line(frame, (shape.part(x).x,shape.part(x).y), (shape.part(x+1).x,shape.part(x+1).y),(0,0,255),1)
        for x in range(36,41): cv2.line(frame, (shape.part(x).x,shape.part(x).y), (shape.part(x+1).x,shape.part(x+1).y),(0,0,255),1)
        for x in range(42,47): cv2.line(frame, (shape.part(x).x,shape.part(x).y), (shape.part(x+1).x,shape.part(x+1).y),(0,0,255),1)
        for x in range(48,53): cv2.line(frame, (shape.part(x).x,shape.part(x).y), (shape.part(x+1).x,shape.part(x+1).y),(0,0,255),1)
        for x in range(54,59): cv2.line(frame, (shape.part(x).x,shape.part(x).y), (shape.part(x+1).x,shape.part(x+1).y),(0,0,255),1)
        for x in range(60,64): cv2.line(frame, (shape.part(x).x,shape.part(x).y), (shape.part(x+1).x,shape.part(x+1).y),(0,0,255),1)
        for x in range(65,67): cv2.line(frame, (shape.part(x).x,shape.part(x).y), (shape.part(x+1).x,shape.part(x+1).y),(0,0,255),1)


    cv2.imshow("webcam",frame)

    key = cv2.waitKey(100)&0xFF

    if key == ord('q'):
        break