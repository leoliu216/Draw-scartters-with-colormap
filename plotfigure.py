import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.interpolate
import glob,os
import math
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm
import time
from PIL import Image

# %matplotlib inline

# path=os.getcwd()
# file=glob.glob(os.path.join(path, "*.txt"))#read all *.temp files
# file.sort()#sort the file
# print(file)

path=os.getcwd()
file=glob.glob("*.txt")#read all *.temp files
file.sort()#sort the file
print(file)

df = []
for f in file:
    df.append(pd.read_csv(f,sep='\s+', header = None))

df[0]


def xyz(df):
    dfx = df[0]
    dfy = df[1]
    dfz = df[2]
    x=np.asarray(dfx)
    y=np.asarray(dfy)
    z=np.asarray(dfz)
    return x,y,z

top = cm.get_cmap('autumn', 128)
bottom = cm.get_cmap('Greys', 128)

seriesname = "dmg"
imageid = 0

def plotscratter(datafile):
    global imageid
    imageid = imageid + 1
    imagename = seriesname + str(imageid)
    x, y, z = xyz(datafile)
    
 #     negmin = z.min()
 #     zero = 0
 #     posmax = z.max()

    negmin, zero, posmax = -0.1, 0, 0.65
    negfraction = (zero - negmin) / (posmax - negmin)
    range1 = math.ceil(256 * negfraction)
    newcolors = np.vstack((bottom(np.linspace(1, 0.3, range1)),
                   top(np.linspace(1, 0, 256-range1))))
    newcmp = ListedColormap(newcolors, name='Liketure')

    # plt.ion() #开启interactive mode
    
    plt.figure("Hello",figsize = (9.6, 4), dpi = 200)  

#     plt.figure(figsize = (4.8, 2), dpi = 400)
    sc = plt.scatter(x, y, c=z, vmin=negmin, s=0.5, vmax=posmax, cmap=newcmp)
    plt.xlim(x.min(), x.max())
    plt.ylim(y.min(), y.max())
    cbar = plt.colorbar(sc, boundaries=np.linspace(0,0.7,8), extend="max")
#     cbar.set_ticks([0,0.2,0.4,0.6])
#     cbar.set_ticklabels([0,0.2,0.4,0.6])
#     cbar.ax.set_ylim(0, 0.65)


    for index, label in enumerate( cbar.ax.xaxis.get_ticklabels()):
        print(index, label)
        if index == 1:
            label.set_visible(False)
    plt.title(imagename+".png",y=-0.17)        
    plt.savefig(imagename+ '.png',bbox_inches='tight',dpi=300, pad_inches=0.2)
    plt.close()


    im = Image.open(imagename+ '.png')
    plt.imshow(im)
    # plt.show(block=False)
    plt.axis('off')
    plt.pause(1)
    plt.clf() #will make the plot window empty
    im.close()

for image in df:
    plotscratter(image)
    

# plotscratter(df[0])


# file=glob.glob("*.png")#read all *.temp files
# for f in file:
#     im = Image.open(f)
#     plt.imshow(im)
#     # plt.show(block=False)
#     plt.axis('off')
#     plt.pause(1)
#     plt.clf() #will make the plot window empty
#     im.close()