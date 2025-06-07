import os
from glob import glob
import cv2

from matplotlib import pyplot as plt
Path_FCimage_Raw = './DAP/Raw/'

save_path = './DAP/Cropped/'
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Define the region of interest (ROI) - arbitrary coordinates
x_start, y_start, x_end, y_end = 140, 200, 3300, 2300  # Adjust as needed


for imgname in glob(Path_FCimage_Raw + '*')[:2]:
    print(imgname)
    img = cv2.imread(imgname)
    # cropping image by slicing
    cropped_img = img[y_start:y_end, x_start:x_end]

    # resize
    # resized_img = cv2.resize(cropped_img,(360,360))
    
    # Split the image into 4 quadrants
    h, w = cropped_img.shape[:2]
    h_half, w_half = h // 2, w // 2
    top_left = cropped_img[:h_half, :w_half]
    top_right = cropped_img[:h_half, w_half:]
    bottom_left = cropped_img[h_half:, :w_half]
    bottom_right = cropped_img[h_half:, w_half:]

    # # Display the 4 images in row
    # plt.figure(figsize=(10, 10))
    # plt.subplot(2, 2, 1)
    # plt.imshow(top_left, interpolation='nearest')
    # plt.subplot(2, 2, 2)
    # plt.imshow(top_right, interpolation='nearest')
    # plt.subplot(2, 2, 3)
    # plt.imshow(bottom_left, interpolation='nearest')
    # plt.subplot(2, 2, 4)
    # plt.imshow(bottom_right, interpolation='nearest')
    # plt.tight_layout()
    # plt.show()

    # save each 4 quadrants images into new folder

    cv2.imwrite(os.path.join(save_path, os.path.basename(imgname).split('.')[0] + '_tl' + '.jpg'), top_left)
    cv2.imwrite(os.path.join(save_path, os.path.basename(imgname).split('.')[0] + '_tr' + '.jpg'), top_right)
    cv2.imwrite(os.path.join(save_path, os.path.basename(imgname).split('.')[0] + '_bl' + '.jpg'), bottom_left)
    cv2.imwrite(os.path.join(save_path, os.path.basename(imgname).split('.')[0] + '_br' + '.jpg'), bottom_right)

    # break
    
for jsonfile in glob('./DAP/Cropped/*.json'):
    print(jsonfile)
    # json to image
    os.system(f'labelme_export_json {jsonfile}"')

