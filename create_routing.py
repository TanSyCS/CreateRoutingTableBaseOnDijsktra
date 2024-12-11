import networkx as nx
import json
import pandas as pd

# Đọc dữ liệu từ tệp JSON
with open('./topongu.json', 'r') as file:
    data = json.load(file)

# Khởi tạo đồ thị
graph = nx.Graph()

for node in data["nodes"]:
    graph.add_node(str(node["id"]))

for edge in data["edges"]:
    source = str(edge["source"])
    target = str(edge["target"])
    bandwidth = edge["bandwidth"]
    delay = edge["delay"]
    packetloss = edge["packetloss"]
    cost = 0.9 * bandwidth + 0.05 * delay + 0.05 * packetloss
    graph.add_edge(source, target, cost=cost)

def calculate_routing_table(graph, src_node, dst_node):
    try:
        # Tính toán đường đi ngắn nhất bằng thuật toán Dijkstra
        path = nx.shortest_path(graph, source=src_node, target=dst_node, weight='cost')
        cost = nx.shortest_path_length(graph, source=src_node, target=dst_node, weight='cost')
        return {"Node src": src_node, "Node dst": dst_node, "Cost": cost, "Path": path}
    except nx.NetworkXNoPath:
        return {"Node src": src_node, "Node dst": dst_node, "Cost": float('inf'), "Path": []}
    except nx.NodeNotFound:
        return {"Node src": src_node, "Node dst": dst_node, "Cost": float('inf'), "Path": "Node not found in graph"}

def generate_routing_table(graph, src, dst):
    routing_entry = calculate_routing_table(graph, src, dst)
    return routing_entry

def convert_path_to_table(path):
    table = []
    for i in range(len(path) - 1):
        table.append({"src": path[i], "dst": path[i + 1]})
    return pd.DataFrame(table)

def export_routing_table(path_table, filename="routing_table.csv"):
    path_table.to_csv(filename, index=False)
    print(f"Routing table exported to {filename}")

src_node = input("Nhập node nguồn (src): ")
dst_node = input("Nhập node đích (dst): ")

if src_node not in graph.nodes:
    print(f"Node nguồn (src) {src_node} không tồn tại trong đồ thị.")
elif dst_node not in graph.nodes:
    print(f"Node đích (dst) {dst_node} không tồn tại trong đồ thị.")
else:
    routing_entry = generate_routing_table(graph, src_node, dst_node)
    print(routing_entry)
    if routing_entry["Path"]:
        path_table = convert_path_to_table(routing_entry["Path"])
        print(path_table)
        export_routing_table(path_table)
