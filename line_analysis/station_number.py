import pandas as pd
from matplotlib import pyplot as plt

lines = ['1', '2', '3', '4', '5', '7', '10', 'S1', 'S3', 'S6', 'S7', 'S8', 'S9']

numbers = []
for line in lines:
    df = pd.read_csv(f'../data/stations_{line}.csv')
    station_num = df.shape[0]
    numbers.append(station_num)

fig = plt.figure(figsize=(8, 6))
plt.bar(lines, numbers, color='white', edgecolor='black')
plt.title('Number of Stations on Different Lines')
plt.ylabel('Number of Stations')
plt.xlabel('Line')
plt.savefig('../images/station_number.png', dpi=200)
