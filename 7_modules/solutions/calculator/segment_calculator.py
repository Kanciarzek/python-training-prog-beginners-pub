from math import sqrt


def euclidean_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


if __name__ == '__main__':

    print("Calculate your distance")

    a_x: float = float(input("Give x coordinate of point A: "))
    a_y: float = float(input("Give y coordinate of point A: "))

    b_x: float = float(input("Give x coordinate of point B: "))
    b_y: float = float(input("Give y coordinate of point B: "))

    ab_length = euclidean_distance(a_x, a_y, b_x, b_y)

    print(f"Length of segment AB is {ab_length}")
