# from Classes.cluster import Cluster

def calculate_distance_matrix(data: list[list], distance_calculator):
    distance_matrix = []

    for index in range(len(data)):
        item_distances = []

        for index2 in range(len(data)):
            current_distance =  None
            if index2 < index:
                current_distance = distance_matrix[index2][index]
            
            elif index2 > index:
                current_distance = distance_calculator(data[index], data[index2])

            else:
                current_distance = 0
        
            item_distances.append(current_distance)
        
        distance_matrix.append(item_distances)
    return distance_matrix

def calculate_clusters_distance(cluster_from, cluster_to, distance_matrix, hierarchy_calculator):
    distances = []
    for from_item in cluster_from.items:
        for to_item in cluster_to.items:
            distance = distance_matrix[from_item.index][to_item.index]
            distances.append(distance)
    return hierarchy_calculator(distances)
