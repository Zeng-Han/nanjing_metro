import metro_map
import networkx as nx
from matplotlib import pyplot as plt

map = metro_map.get_metro_map()
betweenness_centrality = nx.betweenness_centrality(map)

betweenness_centrality = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)
print(betweenness_centrality)

fig = plt.figure(figsize=(16, 6))
bars = plt.bar([x[0] for x in betweenness_centrality[:40]], [x[1] for x in betweenness_centrality[:40]], color='white', edgecolor='black')
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height + 0.002,
             f'{height:.4f}', fontsize=6, ha='center', va='bottom')

plt.title('Betweenness Centrality of Stations')
plt.ylabel('Betweenness Centrality')
plt.xlabel('Station Name')
plt.xticks(rotation=45, ha='right')
plt.savefig('../images/betweenness_centrality.png', dpi=400, bbox_inches='tight')
