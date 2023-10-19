from calculator import euclidean_distance

points: list[tuple[float, float]] = [(1, 5), (4, 7), (2, 2)]
my_point: tuple[float, float] = (2, 3)
distance: float = 3

close_points = [x for x in points if euclidean_distance(x[0], x[1], my_point[0], my_point[1]) < distance]

print(f"Punkty, które znajdują się w odległości mniejszej od {distance} od {my_point}, to {close_points}")
