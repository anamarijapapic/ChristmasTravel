##### [Graph Algorithms]: Seminar

# TopCoder: ChristmasTravel

## Problem Statement for ChristmasTravel

Problem statement available at: https://community.topcoder.com/stat?c=problem_statement&pm=15865

> This problem statement is the exclusive and proprietary property of TopCoder, Inc.  
> &copy;2023, TopCoder, Inc. All rights reserved.

### Problem Statement

It is a truth universally acknowledged that Die Hard is the best Christmas movie of all time. And just like John McClane at the beginning of the movie, millions upon millions of people fly home for Christmas each year. This problem is about air travel. Yippie-ki-yay!

There are N airports in Absurdistan. Up until now, there has only been a single airline (owned by the Grand Vizier) that has supplied flights between all the airports. However, the Grand Vizier noticed that the airlines sometimes have trouble filling the planes, and this costs the Grand Vizier money. The Grand Vizier has hired a group of analysts, and after a few months they traced the problem to its root: the possibility to fly an odd number of segments. Ordinary flight tickets in Absurdistan are sometimes called hobbit tickets (as they go "there and back again"). E.g., if a person flies from A via B to C, we can expect that they will later return from C via B to A, traveling a total of four segments. If they were to take a direct flight from C to A instead, the total number of segments flown by our customers would now be odd, and that's the reason why all planes (each with an even number of seats) cannot be filled exactly. Or, at least, that's what the analysts told the Grand Vizier, before collecting their pay and leaving the country in a hurry.

Be it as it may, the Grand Vizier has decided to eliminate this issue completely. His decision was as follows:

- From this moment on, there will be A separate airline companies in Absurdistan. (Each of them owned by the Grand Vizier, of course.)
- For each pair of airports, exactly one of these airlines must fly the direct flights between them, in both directions.
- Each airline must actually fly some flights.
- Each ticket must be purchased with one specific airline. The ticket must contain a sequence of flights offered by that airline. The flights must be consecutive (each starting where the previous ended), and the last flight must return the traveller to the airport where the ticket started.
- It must not be possible to buy a ticket with an odd number of flights.

Find out whether the Grand Vizier's plan can be carried out. If it cannot, return an empty String[]. If it can, return a String[] with N elements, each containing N characters: '-' on the main diagonal, and one of the first A uppercase letters of the English alphabet everywhere else. For each distinct i and j, the characters at [i][j] and [j][i] in the return value must be equal, and they represent the airline that flies between the airports i and j. Any valid answer will be accepted.

### Definition

```
Class:            ChristmasTravel
Method:           plan
Parameters:       int, int
Returns:          String[]
Method signature: String[] plan(int N, int A)
(be sure your method is public)
```

### Constraints
-	N will be between 1 and 100, inclusive.
-	A will be between 1 and 26, inclusive.

### Examples

#### 0)
3  
1  
Returns: { }  
There is no solution. If we had three airports and a single airline, people could buy a ticket with an odd number of flights. An example of such a ticket is a ticket with the flights 2 -> 0 -> 1 -> 2.

#### 1)
3  
3  
Returns: {"-AC", "A-B", "CB-" }  
Remember that each airline must fly some segments, so each of the letters 'A', 'B' and 'C' must appear in the output for this test case (exactly twice). All correct answers for this test case can be obtained from the one shown in the example by permuting 'A', 'B', and 'C'.

#### 2)    	
5  
3  
Returns: {"-ABAB", "A-ACC", "BA-AC", "ACA-B", "BCCB-" }  
The example output describes the following situation:  
Airline 'A' executes the flights between the following pairs of airports: 0-1, 1-2, 2-3, 3-0.  
Airline 'B' executes the flights between the following pairs of airports: 2-0, 0-4, 4-3.  
Airline 'C' executes the flights between the following pairs of airports: 3-1, 1-4, 4-2.  
We can easily verify that none of these airlines can sell a valid ticket with an odd number of flights.

#### 3)	
1  
1  
Returns: { }  
If there is just one airport, no flights are possible, so the only airline in this country does not fly anywhere. This contradicts the requirement that each airline must actually fly some flights.

#### 4)		
6  
5  
Returns: {"-ACEDB", "A-BDCE", "CB-AED", "EDA-BC", "DCEB-A", "BEDCA-" }  
In the example output, each airline has exactly one flight out of each airport. Thus, obviously, each valid ticket people can buy just goes back and forth between two airports one or more times, and therefore there are no valid tickets with an odd number of flights. Of course, this is just one of very many valid solutions.

This problem was used for:  
- Single Round Match 773 Round 1 - Division I, Level Two  
- Single Round Match 773 Round 1 - Division II, Level Three

## Test Report

The following is a screenshot of the test report from the TopCoder Practice Arena:

![Test Report](https://github.com/anamarijapapic/ChristmasTravel/assets/92815435/3d7f6b53-d108-4d51-b530-0683de91521c)
