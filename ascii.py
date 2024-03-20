from PIL import Image
import numpy as np
import os 
import open as op

image = op.get_list_images()

if image == -1:
    print("Exit! Error! Things going WRONG BWAH BWAH BWAHAHAHA")
else:
    image = "images/" + image
# print(image)
    im = Image.open(image)
    print("Succesfully Loaded image!!")
    length = im.size[0]
    breadth = im.size[1]
    print("Image: {}x{}".format(length, breadth))
    img_rgb = im.convert('RGB')
    img_array = np.array(img_rgb)
        
    img_avg = np.empty((breadth, length))
    img_bright = np.empty((breadth, length))
    img_lumous = np.empty((breadth, length))
        
    for i in range(breadth):
        for j in range(length):
                
            # print(img_array[j,i,1])
            img_avg[i,j] = (img_array[i,j,0] + img_array[i,j,1] + img_array[i,j,2])/3
            img_bright[i,j] = (max(img_array[i,j,0] , img_array[i,j,1] ,img_array[i,j,2]) + min(img_array[i,j,0]  ,img_array[i,j,1] , img_array[i,j,2]))/3
            img_lumous[i,j] = 0.21 * img_array[i,j,0]+ 0.72 * img_array[i,j,1] + 0.07 * img_array[i,j,2]
        
    x = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    for i in range(breadth):
        for j in range(length):
            gg = img_lumous[i,j]
            # print(gg)
            gg = gg/255 * 64        
            print(x[round(gg)], end = " ")
        print("/n")