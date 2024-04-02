import networkx as nx
import pandas as pd


def get_metro_map():
    lines = ['1', '2', '3', '4', '5', '7', '10', 'S1', 'S3', 'S6', 'S7', 'S8', 'S9']
    metro_map = nx.Graph()
    for line in lines:
        df = pd.read_csv(f'../data/stations_{line}.csv')
        stations = df['站点']
        line_map = nx.path_graph(stations)
        metro_map = nx.compose(metro_map, line_map)
    return metro_map
