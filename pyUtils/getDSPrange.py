import os
from tifffile import tifffile
import  numpy as np
from glob import glob
from tqdm import tqdm
import matplotlib.pyplot as plt

src_dir = '/home/jarvis2019/research/data/igrass/Track2-Truth/'
all_disp_img = glob(src_dir+'JAX*LEFT_DSP.tif')
all_disp_img.sort()

# maxVal = -999
# minVal = 999
maxVal = []
minVal = []

for i in tqdm(all_disp_img):
    img = tifffile.imread(i)
    img = img[img>-999]
    maxDsp = img.max()
    minDsp = img.min()
    maxVal.append(maxDsp)
    minVal.append(minDsp)
    # if maxDsp > maxVal:
    #     maxVal = maxDsp
    # if img.min() < minVal:
    #     minVal = minDsp

plt.figure()
plt.plot(maxVal,minVal)
plt.show()

