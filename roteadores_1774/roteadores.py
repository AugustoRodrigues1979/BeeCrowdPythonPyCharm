router_graph = {} # Initialize an empty graph

def add_edge_with_smallest_weight(graph, start_node, end_node, value_weight):
    is_added_edge = False
    if end_node in graph and graph[end_node][0][0] == start_node:  # Check if exist end_node in graph and this node is connected with start_node
        return is_added_edge

    if start_node not in graph:  # Check if start_node is with in graph
        graph[start_node] = [(end_node, value_weight)]  # Create start_node in the graph
        is_added_edge = True
    else:
        current_node, current_weight_node = graph[start_node][0][0], graph[start_node][0][1]  # Get data from start node
        if current_weight_node > value_weight:  # Check if current weight is greater the weight input
            graph[start_node] = [(end_node, value_weight)]  # Update weight between start_node and end_node
            is_added_edge = True

    return is_added_edge

def run_challenge():
    input_data_lst = list(input().split())
    if len(input_data_lst) != 2:
        return

    amount_routers, amount_cables = int(input_data_lst[0]), int(input_data_lst[1])
    if amount_routers < 3 or amount_routers > 60:
        return

    if amount_cables < amount_routers or amount_cables > 200:
        return

    for _ in range(amount_cables):
        data_cable_lst = list(map(int, input().split()))
        begin_id_router, end_id_router, price_cable = data_cable_lst[0], data_cable_lst[1], data_cable_lst[2]
        add_edge_with_smallest_weight(router_graph, begin_id_router, end_id_router, price_cable)

    smallest_weight = 0
    for id_router in router_graph.keys():
        smallest_weight += router_graph[id_router][0][1]

    print(str(smallest_weight))

if __name__ == '__main__':
    run_challenge()
