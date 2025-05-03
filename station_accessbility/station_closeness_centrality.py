import metro_map
import networkx as nx
from matplotlib import pyplot as plt

map = metro_map.get_metro_map()
closeness_centrality = nx.closeness_centrality(map)

closeness_centrality = sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True)
print(closeness_centrality)

average_distance = [(x[0], 1 / x[1]) for x in closeness_centrality]
print(average_distance)

fig = plt.figure(figsize=(16, 6))
bars = plt.bar([x[0] for x in closeness_centrality[:40]], [x[1] for x in closeness_centrality[:40]], color='white', edgecolor='black')
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height + 0.0005,
             f'{height:.4f}', fontsize=6, ha='center', va='bottom')

plt.title('Closeness Centrality of Stations')
plt.ylabel('Closeness Centrality')
plt.xlabel('Station Name')
plt.xticks(rotation=45, ha='right')
plt.savefig('../images/closeness_centrality.png', dpi=400, bbox_inches='tight')

fig = plt.figure(figsize=(16, 6))
bars = plt.bar([x[0] for x in average_distance[:40]], [x[1] for x in average_distance[:40]], color='white', edgecolor='black')
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height + 0.1,
             f'{height:.2f}', fontsize=6, ha='center', va='bottom')

plt.title('Average Distance Between Stations')
plt.ylabel('Average Distance (station)')
plt.xlabel('Station Name')
plt.xticks(rotation=45, ha='right')
plt.savefig('../images/average_distance.png', dpi=400, bbox_inches='tight')
