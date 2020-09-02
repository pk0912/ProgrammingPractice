def tour(lis, n):
    # Code here
    petrol = [l[0] for l in lis]
    distance = [l[1] for l in lis]
    curr_diff = 0
    start = 0
    if sum(petrol) - sum(distance) < 0:
        return -1
    for i in range(len(petrol)):
        curr_diff += petrol[i] - distance[i]
        if curr_diff < 0:
            start = i + 1
            curr_diff = 0
    return start


lst = [87, 27, 40, 95, 71, 96, 79, 35, 2, 68, 3, 98, 93, 18, 57, 53, 81, 2, 42, 87, 90, 66, 20, 45, 30, 41]
lst1 = [lst[i] for i in range(len(lst)) if i % 2 == 0]
lst2 = [lst[i] for i in range(len(lst)) if i % 2 != 0]
print(tour(list(zip(lst1, lst2)), len(lst1)))
