import sys  
from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QPixmap, QResizeEvent, QImage, QFont
from PySide6.QtWidgets import QLabel

from ultralytics import YOLO
import cv2
import torch

CAMERA = 0
detection_threshold = 0.95
detection_threshold_hand = 0.9

work_online = False

cl = ['Carrot','Cucumber', 'Potato']
cl_dict = {i: c for i, c in enumerate(cl)}
YOLOmodel = YOLO('models/best.pt')  # load a pretrained model (recommended for training)
YoloHand = YOLO('models/best_hand.pt')  # load a pretrained model (recommended for training)



class Info(QtWidgets.QWidget):
    """
    Класс для отображения инфо окна
    """
    def __init__(self,):
            super().__init__()
  

            layout = QtWidgets.QVBoxLayout()
            self.label = QLabel(self)
            self.label.setFixedSize(640, 480)
            self.work_online = QtWidgets.QPushButton()

            layout.addWidget(self.label)
            layout.addWidget(self.work_online)


            self.setLayout(layout)


            self.cap = cv2.VideoCapture(CAMERA)

            # Создание таймера
            self.timer = QtCore.QTimer(self)
            self.timer.timeout.connect(self.img_update)


            self.work_online.clicked.connect(self.change_work)

    def MY2(self,model,model_hand,image):
        result_value = {}

        
        results_hand = model_hand(image, device='mps')

        for result_hand in results_hand:
            value, product = torch.sort(result_hand[0].probs.data,descending = True)
            print(value,product)
            

            
            max_product_h = result_hand.names[int(product)]
            max_score_h = float(value)
            if max_score_h > detection_threshold_hand:
                
                cv2.putText(image,f"  {max_product_h} {max_score_h}",(int(200), int(100)),cv2.FONT_HERSHEY_COMPLEX, 1.5 ,thickness = 2, color=(0,0,0))


        results = model(image, device='mps')
        for result in results:
            value, product = torch.sort(results[0].probs.data,descending = True)
    
            for item in zip(value, product):
                result_value[result.names[int(item[1])]] = float(item[0])
            
            max_product = max(result_value, key=result_value.get)
            max_score = result_value[max_product]
            if max_score > detection_threshold:
                

                cv2.putText(image,f"  {max(result_value, key=result_value.get)}",(int(20), int(40)),cv2.FONT_HERSHEY_COMPLEX, 1.5 ,thickness = 2, color=(0,0,0))
                cv2.putText(image,f"  {result_value}",(int(200), int(40)),cv2.FONT_HERSHEY_COMPLEX, 1.5 ,thickness = 2, color=(0,0,0))
                print('!!!!!!!')
                print(max_product_h)
                if max_product_h == 'hand' and max_score_h > detection_threshold_hand:
                    return None
                else:
                    return max_product

        return None




    def img_update(self):
        """
        Обновить изображение
        """
  
        ret, frame = self.cap.read()
        data = self.MY2(YOLOmodel,YoloHand,frame)

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
        
        return(data)

    def change_work(self):
        """
        Смена работы с непрерывной на разовое измерение
        """

        if self.work_online:
            self.work_online = False
            self.timer.stop()
        else:
            self.work_online = True
            self.timer.start()



def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Info()
    main.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
