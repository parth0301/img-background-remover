import cv2
import numpy as np
from easygui import fileopenbox, filesavebox

def open_image():
    input_path = fileopenbox(title='Select image file')
    return cv2.imread(input_path)

def save_image(image, output_path):
    cv2.imwrite(output_path, image)

def remove_background(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_white = np.array([0, 0, 200], dtype=np.uint8)
    upper_white = np.array([180, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_white, upper_white)
    result = cv2.bitwise_and(image, image, mask=mask)
    return result

if __name__ == '__main__':
    input_image = open_image()
    output_image = remove_background(input_image)
    output_path = filesavebox(title='Save file to..')
    save_image(output_image, output_path)