import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors as mcolors
from Ritoapi import Ritoapi

#map data domains
xmin = -120
xmax = 14870
ymin = -120
ymax = 14980

xdomain =  xmax - xmin
ydomain = ymax - ymin

# plot range = image pixels w & h
xrange = 512
yrange = 512

# domain to range ratio
xdom2range = xdomain/xrange
ydom2range = ydomain/yrange

# plot limits
plt.xlim(0,xrange) 
plt.ylim(0,yrange)

data = np.zeros(shape=(1000,2)) 

api = Ritoapi('') #api key goes here
r = api.get_summoner_by_name('Captain DaGOn')
account = r['accountId']
matches = api.get_past_ranked_solo(account)

i = 0
for match in matches['matches']:
    time.sleep(1)
    info = api.get_match(match['gameId'])
    timeline = api.get_timeline(match['gameId'])
    frames = timeline['frames']
    participantId = 6

    for frame in frames:
        for event in frame['events']:
            if event['type'] == 'CHAMPION_KILL':
                if event['victimId'] == participantId:
                    print (event['position'])
                    data[i][0] = (event['position']['x']-xmin)
                    data[i][1] = (event['position']['y']-ymin)
                    i += 1

for values in data:
    values[0] = values[0]/xdom2range
    values[1] = values[1]/ydom2range
print(data)

# scatter plot over map image   
plt.figure(1)
img=mpimg.imread('map11.png')
imgplot = plt.imshow(img, aspect='equal')
plt.scatter(* data.T)

# dataset heat map 
# bins = range/2
plt.figure(2)
heatmap, xedges, yedges = np.histogram2d(data[:,0],data[:,1], bins=(256,256))
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
plt.clf()
plt.imshow(heatmap.T, extent=extent, origin='lower')

plt.show()
