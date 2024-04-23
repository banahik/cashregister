from ultralytics import YOLO
import torch

YOLOmodel = YOLO('/Users/aleksandrgordejcik/Yandex.Disk-banahikk.localized/masters/samsung/cashregister/models/best_hand.pt')  # load a pretrained model (recommended for training)


results = YOLOmodel('/Users/aleksandrgordejcik/Yandex.Disk-banahikk.localized/masters/samsung/cashregister/123.jpeg')



result_value = {}
for result in results:
    value, product = torch.sort(results[0].probs.data,descending = True)
    
    for item in zip(value, product):
        result_value[result.names[int(item[1])]] = float(item[0])

print(max(result_value, key=result_value.get))

