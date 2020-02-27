#import xml.dom.minidom
import numpy as np
#from skimage.draw import rectangle
import cv2
from PIL import Image, ImageDraw
#import matplotlib.pyplot as plt
#from matplotlib.patches import Rectangle
import os

dir_img = '/home/anwesha/Downloads/Mlt/IMAGE/'
dir_mask = '/home/anwesha/Downloads/Mlt/mask/'

files = os.listdir('/home/anwesha/Downloads/Mlt/GT/')
path = '/home/anwesha/Downloads/Mlt/GT'
dest_path = '/home/anwesha/Downloads/Mlt/AR'



# for i in l:
#     if(i[(len(i)-4):] == '.JPG'):
#         print(i)
#         image_list.append(i)
# i=0
# for i in l:
#     if(i[(len(i)-4):] == '.jpg'):
#         print(i)
#         image_list.append(i)
# print(image_list)
image_list = os.listdir(dir_img)
for i in image_list:
    print(i)
    im = Image.open(dir_img+i)
    width, height = im.size
    img=np.zeros((height,width))
    # doc = xml.dom.minidom.parse(dir_img+i[:(len(i)-4)]+".xml")
    # lines = doc.getElementsByTagName("character")
    # points = []
    # for elements in lines:
    #     charData = []
    #     charData.append(elements.getAttribute("x"))
    #     charData.append(elements.getAttribute("y"))
    #     charData.append(elements.getAttribute("width"))
    #     charData.append(elements.getAttribute("height"))
    #     points.append(charData)
    for txts in files:
        if i[:(len(i)-4)] == txts[:(len(txts)-4)]:
            paths = path + '/' + txts
            if txts.endswith(".txt"):
                f = open(paths,'r')
                points = []
                for line in f:
                    lists = line.split(',')
                    points.append(lists[0])
                    points.append(lists[1])
                    points.append(lists[4])
                    points.append(lists[5])
                # print(points)
                # print(points.index('70'))
            no_of_words=len(points)
            for x in range(0,no_of_words,4):
            #     ## plt.gca().add_patch(Rectangle((int(points[x][0]),int(points[x][1])),int(points[x][2]),int(points[x][3]),linewidth=1,edgecolor='w',facecolor='w'))
                
                leftx=int(points[x])
                lefty=int(points[x+1])
                rightx = int(points[x+2])
                righty = int(points[x+3])

            # #     rightx=int(points[x][0])+int(points[x][2])
            # #     righty=int(points[x][1])+int(points[x][3])
                img[lefty:righty,leftx:rightx]=255#to make white rectangles
            cv2.imwrite(dir_mask+i,img)
            img1 = cv2.imread(dir_img+i)
            img2 = cv2.imread(dir_mask+i)
            
            dst = cv2.bitwise_and(img2, img1, mask = None)
            
            cv2.imwrite(dest_path + '/' + i, dst)
            
            # cv2.imshow('dst',dst)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()


#print(img)
#im = Image.open('P090912072.jpg')

#img = Image.new('RGB', (width,height), (0, 0,0))
#img=np.zeros((height,width))
#print(img)
#img.save("bl.jpg")

#img  = Image.open("P090912072.jpg")
#draw = ImageDraw.Draw(img)
#plt.imshow(Image.open('bl.jpg'))






#print (points)







