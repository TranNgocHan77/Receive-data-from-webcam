# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 16:47:01 2024

@author: trann
"""

import cv2 
import os

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Unable to read camera feed")
    
output_dir = 'output_images'

os.makedirs(output_dir, exist_ok = True)

img_counter = 0

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    cv2.imshow('webcam', frame)
    
    k = cv2.waitKey(1)
    
    if k%256 == 27:
        print("Escape hit, closing..")
        break 
    elif k%256 == ord('s'): # 's' key to save the frame 
        img_name = os.path.join(output_dir, "opencv_frame_{}.png".format(img_counter))
        cv2.imwrite(img_name, frame)
        print("{}writen!".format(img_name))
        img_counter +=1

cap.release()
cv2.destroyAllWindows()


# import cv2
# import os

# # Đường dẫn cố định do người dùng cung cấp
# output_dir = r"C:\\Users\\trann\\OneDrive\\Máy tính\\Yolo8\\Receive data from webcam\\output_images"

# # Nếu người dùng không nhập, sử dụng thư mục mặc định
# if not output_dir:
#     output_dir = 'output_images'

# # Tạo thư mục nếu nó chưa tồn tại
# os.makedirs(output_dir, exist_ok=True)

# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("Unable to read camera feed")

# img_counter = 0

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break
#     cv2.imshow('webcam', frame)

#     k = cv2.waitKey(1)

#     if k % 256 == 27:
#         print("Escape hit, closing..")
#         break
#     elif k % 256 == ord('s'):  # 's' key to save the frame
#         img_name = os.path.join(output_dir, "opencv_frame_{}.png".format(img_counter))
#         cv2.imwrite(img_name, frame)
#         print("{} written!".format(img_name))
#         img_counter += 1

# cap.release()
# cv2.destroyAllWindows()

        


