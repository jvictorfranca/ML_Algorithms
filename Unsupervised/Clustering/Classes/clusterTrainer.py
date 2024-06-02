from utils import calculate_distance_matrix, calculate_clusters_distance
from Classes.cluster import Cluster, ClusterItem, ClustersGroup
from types import FunctionType

class ClusterTrainer:
    def __init__(self, data: list[list[float]], labels: list[str], distance_calculator: FunctionType , hierarchy_method: FunctionType):
        self.stage = 0
        self.labels = labels
        self.distance_matrix = calculate_distance_matrix(data, distance_calculator)
        self.hierarchy_method = hierarchy_method
        self.distance_calculator = distance_calculator

        clusters: list[Cluster] = []
        for index, item in enumerate(data):
            cluster_item = ClusterItem(index, item)
            clusters.append(Cluster([cluster_item], index))

        self.clusters_group = ClustersGroup(clusters)

    def print_report(self):
        self.clusters_group.print_report(self.labels)

    def run_next_stage(self):
        if(len(self.clusters_group.clusters) <= 1):
            print("Max Stages reached")
            return 
        distances = []
        for index in range(len(self.clusters_group.clusters)):
            for index2 in range(index + 1, len(self.clusters_group.clusters)):
                cluster_from = self.clusters_group.clusters[index]
                cluster_to = self.clusters_group.clusters[index2]
                distance = calculate_clusters_distance(cluster_from, cluster_to, self.distance_matrix, self.hierarchy_method)
                distance_dict = { "cluster_from": cluster_from, "cluster_from_id": cluster_from.id, "cluster_to": cluster_to, "cluster_to_id": cluster_to.id, "distance": distance}
                distances.append(distance_dict)

        min_distance = min(distances, key = lambda x : x["distance"])
        self.stage += 1
        print(f"Stage {self.stage} started")
        print(f"Smaller distance: Cluster ({min_distance['cluster_from_id']}) : Cluster ({min_distance['cluster_to_id']}) - Distance: {min_distance['distance']} ")
        for item in min_distance["cluster_to"].items:
            min_distance["cluster_from"].items.append(item)
        min_distance["cluster_to"].items.clear()
        self.clusters_group.remove_empty_clusters()