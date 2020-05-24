import random
def init_random_matrix(amount_point, amount_relationship):
    amount_relationship_init = 0
    matrix = []
    check_list=[]
    for i in range(amount_point):
        matrix.append([])
        for j in range(amount_point):
            matrix[i].append(0)
            if i != j:
                check_list.append([i, j])

    while amount_relationship_init != amount_relationship:
        x = random.choice(check_list)
        matrix[x[0]][x[1]] = random.randint(1, 100)
        check_list.remove([x[0], x[1]])
        amount_relationship_init += 1
    return matrix


def init_point_position(amount_point):
    list_point = []
    list_position = []
    list_point.append([0, 0])

    if amount_point >= 3 and amount_point <= 6:
        distance = 350
        epxilon = 2.5
    elif amount_point >= 7 and amount_point <= 10:
        distance = 130
        epxilon = 4
    elif amount_point >= 11 and amount_point <= 14:
        distance = 60
        epxilon = 6
    elif amount_point >= 15 and amount_point <= 18:
        distance = 35
        epxilon = 8
    elif amount_point >= 19 and amount_point <= 22:
        distance = 23
        epxilon = 8.5
    elif amount_point >= 23 and amount_point <= 26:
        distance = 17
        epxilon = 6
    elif amount_point >= 27 and amount_point <= 30:
        distance = 13
        epxilon = 3
    elif amount_point >= 31 and amount_point <= 34:
        distance = 10
        epxilon = 2
    else:
        distance = 5
        epxilon = 2
    distance_min_ratio = int((amount_point+2)/4) if (amount_point-2) % 4 != 0 else int((amount_point+2)/4)-1


    for i in range(distance_min_ratio):
        list_point.append([-(distance_min_ratio-i), i]) if i != 0 else \
            list_point.append([-distance_min_ratio, (1e-1)*epxilon])
    list_point.append([0, distance_min_ratio])

    for i in range(1, distance_min_ratio+1, 1):
        list_point.append([i, (distance_min_ratio-i)]) if i != distance_min_ratio else \
            list_point.append([distance_min_ratio, (1e-1)*epxilon])

    for i in range(distance_min_ratio, 0, -1):
        list_point.append([i, -(distance_min_ratio-i)]) if i != distance_min_ratio else \
            list_point.append([distance_min_ratio, -(1e-1)*epxilon])

    list_point.append([0, -distance_min_ratio])

    for i in range(1, distance_min_ratio, 1):
        list_point.append([-i, -(distance_min_ratio-i)])

    list_position.append([600, 5])
    for i in range(1, len(list_point), 1):
        x = list_position[i-1][0] + distance*list_point[i][0]
        y = list_position[i-1][1] + distance*list_point[i][1]
        list_position.append([x,y])
    if amount_point % 4 == 1:
        list_position.remove(list_position[int(len(list_position)/2)])
    elif amount_point % 4 == 0:
        list_position.remove(list_position[int(len(list_position)/2)])
        list_position.remove(list_position[0])
    elif amount_point % 4 == 3:
        list_position.remove(list_position[int(len(list_position)/2)])
        list_position.remove(list_position[int(len(list_position)/2)])
        list_position.remove(list_position[int(len(list_position)/2)])
    return list_position


def init_line_points(a, b):
    # Top (OK) -> Right (OK) -> Bottom (OK)-> Left (OK)
    a1 = [[a[0]+26, a[1]], [a[0]+50, a[1]+12], [a[0]+26, a[1]+26], [a[0], a[1]+12]]
    b1 = [[b[0]+26, b[1]], [b[0]+50, b[1]+12], [b[0]+26, b[1]+26], [b[0], b[1]+12]]
    if a[1] < b[1]:
        if a[0] < b[0]:
            return [a1[2], b1[3]]
        elif a[0] > b[0]:
            return [a1[2], b1[1]]
        else:
            return [a1[2], b1[0]]
    elif a[1] > b[1]:
        if a[0] < b[0]:
            return [a1[1], b1[2]]
        elif a[0] > b[0]:
            return [a1[3], b1[2]]
        else:
            return [a1[0], b1[2]]

    else:
        if a[0] < b[0]:
            return [a1[1], b1[3]]
        else:
            return [a1[3], b1[1]]

