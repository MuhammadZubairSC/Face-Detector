import cv2


def FaceDetection(file):
    face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    picture=cv2.imread(file)
    grayImage=cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(grayImage,
    scaleFactor=1.01,
    minNeighbors=5)
    a=(max(faces[:, 2]) + min(faces[:, 2]))/2
    for x,y,w,h in faces:
        if w>a:
            img=cv2.rectangle(picture, (x,y), (x+w, y+h), (0,255,1), 3)

    resize=cv2.resize(img, (int(img.shape[1]/1), int(img.shape[0]/1)))

    window_name = 'Face Detection'
    cv2.imshow(window_name, resize)

FaceDetection("abc.jpg")
cv2.waitKey(0)
cv2.destroyAllWindows()
