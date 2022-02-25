import cv2
import numpy as np
import math

class ımage():
    def crop_image(self, im, unet_input_size, shift_x, shift_y):
        size_im = im.shape
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        pad_size_x, pad_size_y = 0, 0
        if size_im[0] % unet_input_size != 0:
            pad_size_y = (size_im[0] // unet_input_size + 1) * unet_input_size - size_im[0]
        if size_im[1] % unet_input_size != 0:
            pad_size_x = (size_im[1] // unet_input_size + 1) * unet_input_size - size_im[1]

        pad_im = np.pad(im, ((shift_y, pad_size_y + shift_y), (shift_x, pad_size_x + shift_x)),
                        mode='mean')  # )mode='constant',constant_values=0
        size_pad_im = pad_im.shape
        x_div, y_div = np.int64(size_pad_im[1] / unet_input_size), np.int64(size_pad_im[0] / unet_input_size)

        im_cropped = []
        count = 0
        for j in range(y_div):
            for i in range(x_div):
                cropped = pad_im[j * unet_input_size:(j + 1) * unet_input_size,
                          i * unet_input_size:(i + 1) * unet_input_size]
                im_cropped.append(np.uint8(cropped))
                count = count + 1

        return im_cropped


    def merge_image(self, images, cr_sizeX, cr_sizeY, fullResX, fullResY, shift_x, shift_y):
        v_images = []
        y_scan = fullResY // cr_sizeY + 1
        x_scan = fullResX // cr_sizeX + 1
        for i in range(y_scan):
            v_img = cv2.hconcat(images[(i * x_scan):((i * x_scan) + x_scan)])
            v_images.append(v_img)
        image_full = cv2.vconcat(v_images)
        return image_full[shift_y:fullResY + shift_y, shift_x:fullResX + shift_x]