class ClusterItem:
    def __init__(self, index, item:list):
        self.index = index
        self.item = item

class Cluster:
    def __init__(self, cluster_items: list[ClusterItem], id):
        self.items = cluster_items
        self.id = id

class ClustersGroup:
    def __init__(self, clusters: list[Cluster]):
        self.clusters = clusters

    def remove_empty_clusters(self):
        for cluster in self.clusters:
            if(len(cluster.items) == 0):
                self.clusters.remove(cluster)

    def print_report(self, items_ids):
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Report")
        print(f"Clusters number: {len(self.clusters)}")
        for cluster in self.clusters:
            print(f" - Cluster {cluster.id}")
            for item in cluster.items:
                print(f"    - Item {items_ids[item.index]}: {item.item}")