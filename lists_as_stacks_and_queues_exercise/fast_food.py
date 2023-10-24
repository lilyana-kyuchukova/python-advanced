from collections import deque

quantity_of_food = int(input())
quantity_order = deque([int(item) for item in input().split()])
# is_complete = True

print(max(quantity_order))

while quantity_order and quantity_order[0] <= 0:
    quantity_of_food -= quantity_order[0]
    quantity_order.popleft()


if quantity_order:
    # to_print = " ".join([str(order) for order in quantity_order])
    # print(f"Orders left: {to_print}
    print("Orders left:", end="")
    print(f" {quantity_order.popleft()}", end="")
else:
    print("Orders complete")

# while quantity_order:
#     order = quantity_order.popleft()
#
#     if order <= quantity_of_food:
#         quantity_of_food -= order
#     else:
#         quantity_order.appendleft(order)
#         is_complete = False
#         break
#
#
# if is_complete:
#     print("Orders complete")
# else:
#     to_print = " ".join([str(order) for order in quantity_order])
#     print(f"Orders left: {to_print}")
