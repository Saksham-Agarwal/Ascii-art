from PIL import Image
import numpy as np
try: 
    im = Image.open("sheep_graze640x480.jpg")
    print("Succesfully Loaded image!!")
    print("Image: {}x{}".format(im.size[0], im.size[1]))
    img_rgb = im.convert('RGB')
    img_array = np.array(img_rgb)
    img_final = np.empty((480, 640))
    for i in img_array:
        for j in i:
            # print(img_array[j,i,1])
            img_final[j,i] = (img_array[j,i,0] + img_array[j,i,1] + img_array[j,i,2])/3
    print(img_array.shape)

except:
    print("BEEP BOOP ERROR")

