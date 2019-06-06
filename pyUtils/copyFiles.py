import shutil
from tqdm import tqdm
import os
# basename = '/home/jarvis2019/research/data/sar_optical/Renne4_256/'
# basename = '/home/jarvis2019/research/data/sar_optical/yindu#3/'
basename = '/home/jarvis2019/research/data/sar_optical/zhongshan/'
# basename = ['/home/jarvis2019/research/data/sar_optical/Renne1_256/',
#             '/home/jarvis2019/research/data/sar_optical/Renne2_256/',
#             '/home/jarvis2019/research/data/sar_optical/Renne4_256/',
#             '/home/jarvis2019/research/data/sar_optical/Tucson/',
#             '/home/jarvis2019/research/data/sar_optical/zhongshan/']
# targetname = '/home/jarvis2019/research/data/sar_optical/total/'
# optfilelist = []
# sarfilelist = []
# sarAfilelist = []
# for idx,name in enumerate(basename):
#     optfilelist.append(sorted([os.path.join(name,'opt', d) for d in os.listdir(os.path.join(name,'opt'))]))
#     sarfilelist.append(sorted([os.path.join(name,'sar', d) for d in os.listdir(os.path.join(name,'sar'))]))
#     sarAfilelist.append(sorted([os.path.join(name,'sarA', d) for d in os.listdir(os.path.join(name,'sarA'))]))
#
# num = 0
# num1 = 0
# for i in range(4):
#     len1 = int(len(optfilelist[i])*0.75)
#     len2 = len(optfilelist[i])
#     for j in range(len1):
#         shutil.copyfile(optfilelist[i][j],os.path.join(targetname,'trainA',str(j+num)+'.png'))
#     for j in range(len1,len2):
#         shutil.copyfile(optfilelist[i][j],os.path.join(targetname,'testA',str(j+num1)+'.png'))
#     num+=len1
#     num1+=len2-len1
#
# num = 0
# num1 = 0
# for i in range(4):
#     len1 = int(len(sarfilelist[i])*0.75)
#     len2 = len(sarfilelist[i])
#     for j in range(len1):
#         shutil.copyfile(sarfilelist[i][j],os.path.join(targetname,'trainB',str(j+num)+'.png'))
#     for j in range(len1,len2):
#         shutil.copyfile(sarfilelist[i][j],os.path.join(targetname,'testB',str(j+num1)+'.png'))
#     num+=len1
#     num1+=len2-len1
#
# num = 0
# num1 = 0
# for i in range(4):
#     len1 = int(len(sarAfilelist[i])*0.75)
#     len2 = len(sarAfilelist[i])
#     for j in range(len1):
#         shutil.copyfile(sarAfilelist[i][j],os.path.join(targetname,'trainC',str(j+num)+'.png'))
#     for j in range(len1,len2):
#         shutil.copyfile(sarAfilelist[i][j],os.path.join(targetname,'testC',str(j+num1)+'.png'))
#     num+=len1
#     num1+=len2-len1

# oldfolder = '/home/jarvis2019/research/data/sar_optical/Renne1_256/opt/'
# oldfolder = '/home/jarvis2019/research/data/sar_optical/Renne1_256/sar/'
# newfolder = '/home/jarvis2019/research/data/sar_optical/Renne1_256/trainB/'
# newfolder = '/home/jarvis2019/research/data/sar_optical/Renne1_256/testB/'
# newfolder = '/home/jarvis2019/research/data/sar_optical/Renne1_256/testA/'
# filelist = os.listdir(oldfolder)
#
# filelist.sort()

trainA_path = os.path.join(basename, 'trainA')
trainB_path = os.path.join(basename, 'trainB')
testA_path = os.path.join(basename, 'testA')
testB_path = os.path.join(basename, 'testB')
valA_path = os.path.join(basename, 'valA')
valB_path = os.path.join(basename, 'valB')
if not os.path.isdir(trainA_path):
    os.mkdir(trainA_path)
if not os.path.isdir(trainB_path):
    os.mkdir(trainB_path)
if not os.path.isdir(testA_path):
    os.mkdir(testA_path)
if not os.path.isdir(testB_path):
    os.mkdir(testB_path)
if not os.path.isdir(valA_path):
    os.mkdir(valA_path)
if not os.path.isdir(valB_path):
    os.mkdir(valB_path)



# for file in tqdm(filelist[2000:3000]):

# for i in tqdm(range(2096)):
for i in tqdm(range(1800)):
    oldname1 = os.path.join(basename,'opt',str(i+1)+'.png')
    oldname2 = os.path.join(basename,'sarA',str(i+1)+'.png')
    newname1 = os.path.join(basename,'trainA','opt{:04d}.png'.format(i+1))
    newname2 = os.path.join(basename,'trainB','sar{:04d}.png'.format(i+1))

    shutil.copyfile(oldname1,newname1)
    shutil.copyfile(oldname2,newname2)

for i in tqdm(range(1800,2200)):

    oldname1 = os.path.join(basename,'opt',str(i+1)+'.png')
    oldname2 = os.path.join(basename,'sarA',str(i+1)+'.png')
    newname1 = os.path.join(basename,'testA','opt{:04d}.png'.format(i+1))
    newname2 = os.path.join(basename,'testB','sar{:04d}.png'.format(i+1))

    shutil.copyfile(oldname1,newname1)
    shutil.copyfile(oldname2,newname2)
for i in tqdm(range(2200,len(os.listdir(basename+'opt')))):

    oldname1 = os.path.join(basename,'opt',str(i+1)+'.png')
    oldname2 = os.path.join(basename,'sarA',str(i+1)+'.png')
    newname1 = os.path.join(basename,'valA','opt{:04d}.png'.format(i+1))
    newname2 = os.path.join(basename,'valB','sar{:04d}.png'.format(i+1))

    shutil.copyfile(oldname1,newname1)
    shutil.copyfile(oldname2,newname2)
