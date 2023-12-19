# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Seminar - ChristmasTravel

Visualisation helper for examples (using NetworkX package).

https://community.topcoder.com/stat?c=problem_statement&pm=15865

This problem was used for:
       Single Round Match 773 Round 1 - Division I, Level Two
       Single Round Match 773 Round 1 - Division II, Level Three

@author: Anamarija Papic
"""

import networkx as nx
import matplotlib.pyplot as plt

def visualize_flights(N, A):
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes representing airports
    for i in range(N):
        G.add_node(i, label=str(i))

    # Add edges representing flights
    airline_counter = 0
    for i in range(N):
        for j in range(i + 1, N):
            airline_label = chr(ord('A') + airline_counter % A)
            G.add_edge(i, j, label=airline_label)
            G.add_edge(j, i, label=airline_label)
            airline_counter += 1

    # Draw the graph
    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'label')
    
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightgray', font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.8, font_color='red')
    
    plt.title(f'Airline Flights\n{N} airports and {A} airlines')
    plt.legend(['airports', 'flights'], borderpad=1.5, labelspacing=2)
    plt.show()

def main():
    # Note, each example is just one of very many valid solutions.
    
    # Example 0)
    # []
    visualize_flights(3, 1)
    
    # Example 1)
    # ["-AC", "A-B", "CB-"]
    visualize_flights(3, 3)
    
    # Example 2)
    # ["-ABAB", "A-ACC", "BA-AC", "ACA-B", "BCCB-"]
    visualize_flights(5, 3)
    
    # Example 3)
    # []
    visualize_flights(1, 1)
    
    # Example 4)
    # ["-ACEDB", "A-BDCE", "CB-AED", "EDA-BC", "DCEB-A", "BEDCA-"]
    visualize_flights(6, 5)
    
    # visualize_flights(N, A)
    
if __name__ == '__main__':
    main()
