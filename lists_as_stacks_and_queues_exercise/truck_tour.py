from collections import deque

n = int(input())
truck_tour = deque()
start_position = 0
pumps = 0

for _ in range(n):
    current_fuel, distance = input().split()
    truck_tour.append([int(current_fuel), int(distance)])

while pumps < n:
    fuel = 0
    for i in range(len(truck_tour)):
        fuel += truck_tour[i][0]
        destination = truck_tour[i][1]
        if fuel < destination:
            truck_tour.rotate(-1)
            start_position += 1
            pumps = 0
            break
        fuel -= destination
        pumps += 1

print(start_position)

