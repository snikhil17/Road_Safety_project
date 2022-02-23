import cv2
import numpy as np
import os


#loading data

last_n_frames=8 #number of last frames to use for labeling

data=[] #hold data points, to be stacked later
folder=r'C:\Users\ASUS\Desktop\Omdena_Scraping\Video Scraping (Omdena_roadsafety)\Vids'
vid_titles=[]

for file in os.listdir(folder):
    videoPATH= os.path.join(folder, file)
    vid_titles.append(file)
    video=cv2.VideoCapture(videoPATH)
    video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

    #get last 10 frames
    numFrames=video.get(7)
    video.set(1,numFrames-last_n_frames)


    frameMatrix=[] #hold vector for each frame

    for i in range(last_n_frames):
        ret,frame=video.read()
        try:
            frame = cv2.resize(frame, (360, 640))
            frameMatrix.append(np.array(frame).reshape(1,-1))
        except:
            frameMatrix.append(np.random.randint(0,255,(1,360*640*3)))


    data_point=np.hstack(frameMatrix) #stack all 10 frames into one data point
    data.append(data_point) #append datapoints
    video.release()

dataset=np.vstack(data) #stack datapoints into dataset



#active learning
#0=no accident, 1=accident
num_iters=5
num_to_label=10 #how many vids to manually label after each iter
from sklearn.semi_supervised import LabelSpreading
from scipy import stats
labels=np.zeros(len(dataset))
labels[:]=-1
#preliminary labels
for j in range(10):
    vid_to_label = vid_titles[j]
    newLabel = input(vid_to_label)
    labels[j] = int(newLabel)


#model starts
model=LabelSpreading(gamma=0.5, max_iter=20, n_jobs=-1)

for i in range(num_iters):
    model.fit(dataset,labels)
    probs=model.label_distributions_
    probs=np.apply_along_axis(lambda x: x/np.sum(x) if np.sum(x)!=0 else x+0.5, 1, probs)
    entropies=stats.distributions.entropy(probs.T)
    uncertainty_ranks=np.argsort(entropies)[::-1]
    to_label=uncertainty_ranks[:num_to_label]

    for j in to_label:
        vid_to_label=vid_titles[j]
        newLabel=input(vid_to_label)
        labels[j]=int(newLabel)


model.fit(dataset,labels)
final_labels=model.predict(dataset)


#write
import json

labeled_data=json.dumps({vid_titles[i]:final_labels[i] for i in range(len(final_labels))})

with open('labels.json', 'w+') as outfile:
    outfile.write(labeled_data)