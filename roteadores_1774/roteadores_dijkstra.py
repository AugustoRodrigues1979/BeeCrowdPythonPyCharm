import heapq

router_graph = {}  # Initialize an empty graph


def dijkstra(grafo, origem, destino):
    # Inicialização
    dist = {v: float('inf') for v in grafo}  # Distâncias iniciais são infinitas
    dist[origem] = 0  # Distância da origem para si mesma é 0
    prev = {v: None for v in grafo}  # Vetor para armazenar os predecessores
    pq = [(0, origem)]  # Fila de prioridade com (distância, vértice)

    while pq:
        # Obtém o vértice com a menor distância
        distancia_atual, vertice_atual = heapq.heappop(pq)

        # Se atingiu o destino, podemos parar
        if vertice_atual == destino:
            break

        # Verifica os vizinhos do vértice atual
        for vizinho, custo in grafo[vertice_atual]:
            distancia = distancia_atual + custo

            # Se encontramos um caminho mais curto para o vizinho, atualizamos
            if distancia < dist[vizinho]:
                dist[vizinho] = distancia
                prev[vizinho] = vertice_atual
                heapq.heappush(pq, (distancia, vizinho))

    # Recupera o caminho mais curto
    caminho = []
    atual = destino
    while atual is not None:
        caminho.insert(0, atual)
        atual = prev[atual]

    return dist[destino], caminho


def add_router_with_cable(graph, start_node, end_node, value_weight):
    if not start_node in graph:
        graph[start_node] = []

    if not end_node in graph:
        graph[end_node] = []

    graph[start_node].append([end_node, value_weight])
    graph[end_node].append([start_node, value_weight])


def run_challenge():
    input_data_lst = list(input().split())
    if len(input_data_lst) != 2:
        return

    amount_routers, amount_cables = int(input_data_lst[0]), int(input_data_lst[1])
    if amount_routers < 3 or amount_routers > 60:
        return

    if amount_cables < amount_routers or amount_cables > 200:
        return

    start_id_router = -1
    final_id_router = -1
    for _ in range(amount_cables):
        data_cable_lst = list(map(int, input().split()))
        begin_id_router, end_id_router, price_cable = data_cable_lst[0], data_cable_lst[1], data_cable_lst[2]
        add_router_with_cable(router_graph, begin_id_router, end_id_router, price_cable)

        if start_id_router == -1 or start_id_router > min(begin_id_router, end_id_router):
            start_id_router  = min(begin_id_router, end_id_router)

        if final_id_router == -1 or final_id_router < max(begin_id_router, end_id_router):
            final_id_router = max(begin_id_router, end_id_router)

    smallest_weight, path_between_first_to_final_router = dijkstra(router_graph, start_id_router, final_id_router)

    print(str(smallest_weight))

if __name__ == '__main__':
    run_challenge()
