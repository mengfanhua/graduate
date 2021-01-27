import math


def ox_to_dx(x, y, k, alpha, dx, dy):
    off_x = k * math.cos(math.radians(alpha)) * x - k * math.sin(math.radians(alpha)) * y + dx
    off_y = k * math.sin(math.radians(alpha)) * x + k * math.cos(math.radians(alpha)) * y + dy
    return off_x, off_y


def dx_to_ox(x, y, k, alpha, dx, dy):
    m = math.cos(math.radians(alpha))
    n = math.sin(math.radians(alpha))
    off_x = (m * x + n * y - m * dx - n * dy) / k
    off_y = (m * y - n * x + n * dx - m * dy) / k
    return off_x, off_y


if __name__ == '__main__':
    s, d = ox_to_dx(5, 6, 0.5, 30, 4, 6)
    print(s, d)
    a, z = dx_to_ox(s, d, 0.5, 30, 4, 6)
    print(a, z)