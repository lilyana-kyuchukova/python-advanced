clothes_stack = [int(item) for item in input().split()]
capacity = int(input())
# rack = []
# counter = 1
counter = 0

while clothes_stack:
    counter += 1
    current_rack = capacity

    while clothes_stack and clothes_stack[-1] <= current_rack:
        current_rack -= clothes_stack.pop()

    # temp = clothes_stack.pop()
    # if (sum(rack) + temp) <= capacity:
    #     rack.append(temp)
    # else:
    #     counter += 1
    #     rack.clear()
    #     rack.append(temp)

print(counter)
