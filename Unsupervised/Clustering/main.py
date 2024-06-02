import json
from distances import calculate_euclidian
from hierarchy import complete_hierarchy, single_hierarchy, average_hierarchy
from Classes.clusterTrainer import ClusterTrainer


file = open("./data.json")

data = json.load(file)
data_ids = ["Gabriela", "Luiz Felipe","Patrícia", "Ovídio", "Leonor"]

distance_calculator = calculate_euclidian
hierarchy_method = average_hierarchy #complete_hierarchy

clusterTrainer = ClusterTrainer(data=data, labels=data_ids, distance_calculator=distance_calculator, hierarchy_method=hierarchy_method)

clusterTrainer.print_report()
clusterTrainer.run_next_stage()
clusterTrainer.print_report()
clusterTrainer.run_next_stage()
clusterTrainer.print_report()
clusterTrainer.run_next_stage()
clusterTrainer.print_report()
clusterTrainer.run_next_stage()
clusterTrainer.print_report()
clusterTrainer.run_next_stage()






