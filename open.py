import os 


def print_images(dir_list):
    count = 0
    alt = []
    for i in range(len(dir_list)):
        word = dir_list[i]
        x = word.find(".")
        if word[x::] in [".jpg", ".png", ".jpeg"]:
            print("{}. {}".format(count, word[0: x]))
            alt.append(word)
            count += 1
    return alt



# @brief this basically tracks all the things inside the images folder and provide a list of it for user to choose from.
def get_list_images():
    pwd = os.getcwd()
    # print(pwd)
    dir_list = os.listdir(pwd + "\images")
    alt = print_images(dir_list)
    inp  = int(input("Enter the image number: "))

    if (inp <= len(alt) - 1):
        return alt[inp]
    
    else:
        return -1


    