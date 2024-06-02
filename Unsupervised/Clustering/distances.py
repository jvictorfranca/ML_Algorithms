def calculate_euclidian_square(item1: list[float], item2: list[float]):
    distance_array = [(item1[i] - item2[i])**2 for i in range(len(item1))]
    distance = sum(distance_array)
    return distance



def calculate_euclidian(item1: list[float], item2: list[float]):
    square_distance = calculate_euclidian_square(item1, item2)
    distance = square_distance**0.5
    return distance


