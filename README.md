# CreateRoutingTableBaseOnDijsktra
we design the customizable cost function f to extend Dijkstra's algorithm to better address the practical needs of modern network systems. While the traditional Dijkstra algorithm focuses solely on optimizing for the shortest distance or lowest latency, today's networks often require consideration of more factors such as bandwidth, reliability, service priority, or resource costs. The function f is designed to integrate these network parameters and the specific requirements of different service types to optimize the cost of routing. This approach not only enables more flexible route optimization but also ensures that services can operate efficiently, meeting the quality of service and availability criteria demanded by modern applications.
This algorithm extends Dijkstra’s shortest-path approach by incorporating a customizable cost function 𝑓 to optimize routing based on network parameters and the requirements of different service types.

𝑓=β1​⋅Bandwidth^-1​+β2​⋅Delay+β3​⋅PacketLoss+C

β1​,β2​,β3​: Weights determining the importance of each parameter

Bandwidth: Available bandwidth (Mbps).

Delay: Link delay (ms).

PacketLoss: Packet loss ratio (0 to 1).

C: A custom function, defined differently for each service type. Examples:

For interactive apps ( latency-sensitive services), C could depend on real-time constraints.

For file transfer ( reliability-sensitive services),  C could depend on retransmission cost

The goal is to find the optimal path from a source node S to a destination node D, minimizing the total cost 𝑓. The step of this algorithm below: 

Initialization: Set the cost from the source node S to all other nodes as ∞, except cost[S]=0. Use a priority queue to keep track of nodes to visit, initially containing only the source 
node.

Iteration: 
Extract the node 𝑢 with the smallest cost 𝑓 from the priority queue.
If 𝑢 is the destination node 𝐷, terminate the algorithm.
For each neighbor 𝑣 of 𝑢:
Compute the cost 𝑓(𝑢,𝑣) 
Update the cost to reach 𝑣 if the path through 𝑢 has a lower cost than the previously known cost.
Add 𝑣 to the priority queue

Termination: When the priority queue is empty or the destination node is reached, return the path and the minimum total cost.
We utilize the GEANT topology, comprising 23 nodes and 38 links, as depicted in the figures, to simulate the network and assess our algorithm. The experimental environment is established using the Mininet platform. For network management, we employ Ryu as the OpenFlow controller, while Iperf is used to generate flow traffic. The performance evaluation is conducted on the widely recognized GEANT network topology.

 Hello protocol: A protocol used to discover router neighbors and confirm reachability to those neighbors .

 Helper module:

 ConvertToJson: This is a module to convert network status we collect from simulation to Json file to apply our algorithm

 Module Crate_routing: This module is designed for computing routing paths in a network graph using Dijkstra's algorithm. It reads network topology data from a JSON file containing nodes and edges with attributes like bandwidth, delay, and packet loss (from the ConvertToJson module), and calculates a cost for each edge to construct the graph using the NetworkX library. The core functionality includes computing the shortest path and its cost between a source and destination node, converting the resulting path into a readable table format, and exporting the table to a CSV file for further use. Users interact with the module by providing source and destination nodes, after which the system validates the input, calculates the routing path, and displays the results.
