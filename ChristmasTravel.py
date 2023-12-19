# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Seminar - ChristmasTravel

ChristmasTravel class implementation.

Time complexity of this implementation: O(N^2)

https://community.topcoder.com/stat?c=problem_statement&pm=15865

This problem was used for:
       Single Round Match 773 Round 1 - Division I, Level Two
       Single Round Match 773 Round 1 - Division II, Level Three

@author: Anamarija Papic
"""

import networkx as nx
import matplotlib.pyplot as plt

class ChristmasTravel:
    def plan(self, N, A):
        """
        Determines if the Grand Vizier's plan for air travel can be carried out.
        
        Parameters:
        - N (int): Number of airports in Absurdistan (1 to 100, inclusive).
        - A (int): Number of separate airline companies (1 to 26, inclusive).
        
        Returns:
        - list of str: If the plan can be carried out, returns a list of N strings,
                      each containing N characters. If not, returns an empty list.
        """
        if not (1 <= N <= 100 and 1 <= A <= 26):
            raise ValueError("Input parameters do not meet the constraints.")

        # If there is just one airport, no flights are possible.
        # Also check if number of airlines is sufficent. 
        if N % 2 == 1 and A < N // 2 or A == 1:
            return []

        res = [['-'] * N for _ in range(N)]
        
        airlines = [chr(ord('A') + i) for i in range(A)]

        # Handle even N
        if N % 2 == 0:
            for i in range(N):
                for j in range(i + 1, N):
                    res[i][j] = res[j][i] = airlines[(i + j) % A]
        # Handle odd N
        else:
            for i in range(N - 1):
                for j in range(i + 1, N):
                    res[i][j] = res[j][i] = airlines[(i + j) % A]
            for i in range(N - 1):
                res[i][N - 1] = res[N - 1][i] = airlines[(i + N - 1) % A]

        return [''.join(res[i]) for i in range(N)]
    
    def print_airline_flights(self, N, A):
        """
        Prints the flights executed by each airline.

        Parameters:
        - N (int): Number of airports in Absurdistan (1 to 100, inclusive).
        - A (int): Number of separate airline companies (1 to 26, inclusive).
        """
        flights = self.plan(N, A)
        
        if not flights:
            print('No flights are possible.')
            return
        
        airlines = [chr(ord('A') + i) for i in range(A)]

        for i, airline in enumerate(airlines):
            print(f"Airline '{airline}' executes the flights between the following pairs of airports: ", end='')
            airport_pairs = []
            for j in range(len(flights)):
                for k in range(j + 1, len(flights[j])):
                    if flights[j][k] == airline:
                        airport_pairs.append((j, k))
            print(', '.join([f'{pair[0]}-{pair[1]}' for pair in airport_pairs]))
            
    def visualize_plan(self, N, A):
        """
        Visualizes the Christmas Travel plan using a directed graph.
        Using NetworkX Python package.

        Parameters:
        - N (int): Number of airports in Absurdistan (1 to 100, inclusive).
        - A (int): Number of separate airline companies (1 to 26, inclusive).
        """
        flights = self.plan(N, A)

        if not flights:
            print('No valid flights plan to visualize.')
            return
        else:
            print('Visualizing flights plan, see Plots.')

        # Create a directed graph
        G = nx.DiGraph()

        # Add nodes representing airports
        for i in range(N):
            G.add_node(i, label=str(i))

        # Add edges representing flights
        for i in range(N):
            for j in range(i + 1, N):
                if flights[i][j] != '-':
                    G.add_edge(i, j, airline=flights[i][j])
                    G.add_edge(j, i, airline=flights[j][i])

        # Draw the graph
        pos = nx.spring_layout(G)
        edge_labels = {(i, j): flights[i][j] for i, j in G.edges()}

        nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightgray", font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.8, font_color='red')
        
        plt.title(f'ChristmasTravel: Flights Plan Visualization\n{N} airports and {A} airlines')
        plt.legend(['airports', 'flights'], borderpad=1.5, labelspacing=2)
        plt.show()

def main():
    christmas_travel = ChristmasTravel()
    
    # Note, each example is just one of very many valid solutions.
    
    # Example 0)
    # []
    print('Example 0)\n\tN=3\n\tA=1')
    print('Returns:', christmas_travel.plan(3, 1))
    christmas_travel.print_airline_flights(3, 1)
    christmas_travel.visualize_plan(3, 1)
    
    # Example 1)
    # ["-AC", "A-B", "CB-"]
    print('\nExample 1)\n\tN=3\n\tA=3')
    print('Returns:', christmas_travel.plan(3, 3))
    christmas_travel.print_airline_flights(3, 3)
    christmas_travel.visualize_plan(3, 3)
    
    # Example 2)
    # ["-ABAB", "A-ACC", "BA-AC", "ACA-B", "BCCB-"]
    print('\nExample 2)\n\tN=5\n\tA=3')
    print('Returns:', christmas_travel.plan(5, 3))
    christmas_travel.print_airline_flights(5, 3)
    christmas_travel.visualize_plan(5, 3)
    
    # Example 3)
    # []
    print('\nExample 3)\n\tN=1\n\tA=1')
    print('Returns:', christmas_travel.plan(1, 1))
    christmas_travel.print_airline_flights(1, 1)
    christmas_travel.visualize_plan(1, 1)
    
    # Example 4)
    # ["-ACEDB", "A-BDCE", "CB-AED", "EDA-BC", "DCEB-A", "BEDCA-"]
    print('\nExample 4)\n\tN=6\n\tA=5')
    print('Returns:', christmas_travel.plan(6, 5))
    christmas_travel.print_airline_flights(6, 5)
    christmas_travel.visualize_plan(6, 5)
    
    # print(christmas_travel.plan(N, A))
    # christmas_travel.visualize_plan(N, A)

if __name__ == '__main__':
    main()
