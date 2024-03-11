import sys  
from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QPixmap, QResizeEvent, QImage, QFont
from PySide6.QtWidgets import QLabel

from ultralytics import YOLO
import cv2

CAMERA = 0
detection_threshold = 0.2

cl = ['mars','Milkyway']
cl_dict = {i: c for i, c in enumerate(cl)}
YOLOmodel = YOLO('/Users/aleksandrgordejcik/Yandex.Disk-banahikk.localized/masters/samsung/cashregister/best-3NEW.pt')  # load a pretrained model (recommended for training)


class Info(QtWidgets.QWidget):
    """
    Класс для отображения инфо окна
    """
    def __init__(self,):
            super().__init__()
  

            layout = QtWidgets.QVBoxLayout()
            self.label = QLabel(self)
            self.label.setFixedSize(640, 480)

            layout.addWidget(self.label)
            self.setLayout(layout)

            self.cap = cv2.VideoCapture(CAMERA)

            # Создание таймера
            timer = QtCore.QTimer(self)
            timer.timeout.connect(self.img_update)
            timer.start(30)

    def MY2(self,model,image):
        # Вывод результатов
        # results = model.predict(image, device='mps')
        results = model(image, device='mps')
        for result in results:
            My_data = {}

            detections = []
            for index, r in enumerate(result.boxes.data.tolist()):
                x1, y1, x2, y2, score, class_id = r
                x1 = int(x1)
                x2 = int(x2)
                y1 = int(y1)
                y2 = int(y2)
                class_id = int(class_id)
                if score > detection_threshold:
                    detections.append([x1, y1, x2, y2, score])
                    score = str(round(score,3))[2:4]
                    text = cl_dict[class_id]
                    cv2.putText(image,f"  {text}",(int(x1), int(y1-10)),cv2.FONT_HERSHEY_COMPLEX, 1.5 ,thickness = 2, color=(0,0,0))
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)),(0.4, 0.5, 0.5), 3)




            # tracker.update(frame, detections)

            # for track in tracker.tracks:

            #     bbox = track.bbox

            #     x1, y1, x2, y2= bbox
            #     name = f'{x1}/{y1}/{x2}/{y2}'
            #     track_id = track.track_id
            #     color = (colors[track_id % len(colors)])

            #     cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)),color, 3)
            #     cv2.putText(frame,str(track_id),(int(x1), int(y1-10)),cv2.FONT_HERSHEY_COMPLEX, 1.5 ,thickness = 2, color=color)




    def img_update(self):
        """
        Обновить изображение
        """
  
        ret, frame = self.cap.read()
        self.MY2(YOLOmodel,frame)

        # Reading frame in gray scale to process the pattern
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

        # Reading the image in RGB to display it
        color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Creating and scaling QImage
        h, w, ch = color_frame.shape
        img = QImage(color_frame.data, w, h, ch * w, QImage.Format_RGB888)
        scaled_img = img.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
        # Emit signal

        


        self.label.setPixmap(QPixmap.fromImage(scaled_img))




def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Info()
    main.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
