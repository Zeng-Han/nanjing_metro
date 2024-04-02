import pandas as pd
from matplotlib import pyplot as plt

lines = ['1', '2', '3', '4', '5', '7', '10', 'S1', 'S3', 'S6', 'S7', 'S8', 'S9']
line_distances = []
for line in lines:
    df = pd.read_csv(f'../data/distances_{line}.csv')
    distances = df['平均间距（米）'].tolist()
    distances = [d / 1000 for d in distances]
    line_distances.append(distances)

fig = plt.figure(figsize=(8, 6))
plt.boxplot(line_distances, labels=lines, medianprops={'color': 'black'}, sym='.k')
plt.title('Distribution of Distances Between Stations on Different Lines')
plt.ylabel('Distance (km)')
plt.xlabel('Line')
plt.savefig('../images/distance_distribution.png', dpi=200)
