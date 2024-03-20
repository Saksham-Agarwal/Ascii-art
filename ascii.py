from PIL import Image
import numpy as np
import os 

def get_list_images():
    pwd = os.getcwd()
    # print(pwd)
    dir_list = os.listdir(pwd + "\images")
    count = 0
    alt = []
    for i in range(len(dir_list)):
        word = dir_list[i]
        # print(word[-4::])
        if word[-4::] in [".jpg", ".png", "jpeg"]:
            print(" {}. {} ".format(count, word[0:-4]))
            alt.append(word)
            count += 1

    inp  = int(input("Enter the image number: "))

    if (inp <= len(alt) - 1):
        return alt[inp]

    


image = get_list_images()
print(image)
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