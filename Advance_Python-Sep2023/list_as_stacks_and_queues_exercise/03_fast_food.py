from collections import deque
food_quantity = int(input())
orders_queue = deque([int(x) for x in input().split()])
print(max(orders_queue))

while orders_queue and orders_queue[0] <= food_quantity:
    food_quantity -= orders_queue[0]
    orders_queue.popleft()

if orders_queue:
    print("Orders left:", end="")
    while orders_queue:
        print(f" {orders_queue.popleft()}", end = "")
else:
    print("Orders complete")