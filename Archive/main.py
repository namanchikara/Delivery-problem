''' Old solution of the same, using sample_d file with only distance(MaxOrder per truck) constrain'''


from collections import defaultdict
import csv

from math import cos, asin, sqrt
def distance(lat1, lon1, lat2, lon2):
	# Function to determine the distance between two lat and long of two points.
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a)) #2*R*asin...


''' Line 14 to 45 are part of creating duplicate script file '''

cf = open('sample_d.csv')
cr = csv.reader(cf,delimiter=',')

data = []
for i in cr:
    try:
        int(i[2])
    except:
        data.append([
            'Society ID',
            'Order Value',
            'Order Count',
            'Delivery Time',
            'latitude',
            'longitude'
        ])
    else:
        if int(i[2]) <= 350:
            data.append(i)
        else:
            temp = int(i[2])
            while temp>350:
                temp -= 350;
                data.append([i[0],i[1],350,i[3],i[4],i[5]])
            data.append([i[0],i[1],temp,i[3],i[4],i[5]])


with open('temp.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(data)

csvFile.close()



''' Now we'll use temp.csv file which we just created '''

cf = open('temp.csv')
cr = csv.reader(cf,delimiter=',')

data = []
for i in cr:
    try:
        int(i[2])
    except:
        data.append([
            'Society ID',
            'Order Value',
            'Order Count',
            'Delivery Time',
            'latitude',
            'longitude'
        ])
    else:
        if int(i[2]) <= 350:
            data.append(i)
        else:
            temp = int(i[2])
            while temp>350:
                temp -= 350;
                data.append([i[0],i[1],350,i[3],i[4],i[5]])
            data.append([i[0],i[1],temp,i[3],i[4],i[5]])


with open('temp.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(data)

csvFile.close()



cf = open('temp.csv')
cr = csv.reader(cf, delimiter = ',')


count = [0]          		 # Stores Order Count
long  = [76.985951]          # Stores longitude of N orders
latt  = [28.387842]          # Stores lattitude of N orders
sid = []
bigTruck = 0
for i in cr:
  try:
    int(i[2])
  except:
      pass
  else:
    sid.append(int(i[0]))
    count.append(int(i[2]))
    latt.append(float(i[4]))
    long.append(float(i[5]))


# This array will store distances between every societies and warehouse a.k.a Adjacency matrix
dist = [[9999999 for i in range(len(count))] for j in range(len(count))]

dict = {}
for i in range(len(sid)):
	dict[i+1] = sid[i]

for i in range(len(count)):
  for j in range(i+1, len(count)):
    dist[i][j] = distance(latt[i],long[i], latt[j],long[j])
    dist[j][i] = dist[i][j]



truck = 0
path = defaultdict(list)
stack = 0
distances = defaultdict(int)

visited = [False for i in range(len(count))]
visited[0] = True


while True:
  next = min(dist[0])
  if next == 9999999: break
  indx = dist[0].index(next)
  if visited[indx]:
    dist[0][indx] = 9999999
    dist[indx][0] = 9999999
    continue
  stack = 0
  fromm = 0
  to = indx
  while stack<=350 and count[indx]<=350:
    stack += count[indx]
    if stack<=350:
      if not visited[indx]:
        path[truck].append(indx)
        visited[indx] = True
        distances[truck] += dist[fromm][to]
        dist[fromm][to] = 9999999
        dist[0][fromm]  = 9999999
        dist[fromm][0]  = 9999999
        dist[0][to]     = 9999999
        dist[to][0]     = 9999999
        dist[to][fromm] = 9999999
      else:
          stack -= count[indx]

      next = min(dist[to])
      if next == 9999999: break
      fromm = indx
      indx = dist[fromm].index(next)
      to = indx
      while visited[indx]:
        dist[fromm][to] = 9999999
        dist[0][fromm]  = 9999999
        dist[fromm][0]  = 9999999
        dist[0][to]     = 9999999
        dist[to][0]     = 9999999
        dist[to][fromm] = 9999999
        next = min(dist[fromm])
        indx = dist[fromm].index(next)
        to = indx
        if next == 9999999:
          break

    else:
        truck += 1
        break


for i in range(len(count)):
  for j in range(i+1, len(count)):
    dist[i][j] = distance(latt[i],long[i], latt[j],long[j])
    dist[j][i] = dist[i][j]


for i in range(len(distances)):
  distances[i] += dist[path[i][-1]][0]

''' O U T P U T '''


print('Total Numbers of trucks required: ', len(path))
print('Total Distance to be covered: ', sum(distances.values()))

for i in range(len(path)):
  print(str(i).rjust(3), 'truck will goto societies: ')
  print(' ',end = ' ')
  for j in path[i]:
    print(dict[j], end = ' ')
  print()
  print()

for i in range(len(path)):
  print('Truck number ', str(i).rjust(3), 'will cover a total distance of: ',distances[i])
