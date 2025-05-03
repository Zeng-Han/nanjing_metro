import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import random

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False


def get_metro_map():
    lines = ['1', '2', '3', '4', '5', '7', '10', 'S1', 'S3', 'S6', 'S7', 'S8', 'S9']
    metro_map = nx.Graph()
    for line in lines:
        df = pd.read_csv(f'../data/stations_{line}.csv')
        stations = df['站点']
        line_map = nx.path_graph(stations)
        metro_map = nx.compose(metro_map, line_map)
    return metro_map


def get_metro_map_with_distance():
    lines = ['1', '2', '3', '4', '5', '7', '10', 'S1', 'S3', 'S6', 'S7', 'S8', 'S9']
    metro_map = nx.Graph()
    for line in lines:
        df = pd.read_csv(f'../data/stations_{line}.csv')
        stations = df['站点']
        distance = pd.read_csv(f'../data/distances_{line}.csv')
        line_map = nx.path_graph(stations)
        for i in distance.index:
            line_map[distance.loc[i, '起点']][distance.loc[i, '终点']]['weight'] = distance.loc[i, '平均间距（米）']
        metro_map = nx.compose(metro_map, line_map)
    return metro_map


if __name__ == "__main__":
    metro_map = get_metro_map_with_distance()

    # show some random stations and their distances
    nodes = list(metro_map.nodes())
    for i in range(5):
        station = nodes[random.randint(0, len(nodes) - 1)]
        neighbor = random.choice(list(metro_map.neighbors(station)))
        distance = metro_map[station][neighbor]
        distance = distance['weight'] if 'weight' in distance else 0
        print(f"Station: {station}, Neighbor: {neighbor}, Distances: {distance}")

    plt.figure(figsize=(8, 8))
    layout = nx.kamada_kawai_layout(metro_map, weight='weight')
    nx.draw(metro_map, pos=layout, with_labels=True, node_size=30, font_size=8)
    plt.show()
