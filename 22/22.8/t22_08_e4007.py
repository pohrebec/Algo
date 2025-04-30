from collections import deque

def valid(num_str):
    return '0' not in num_str

def apply(num_str):
    results = []

    if num_str[0] != '9':
        new_num = str(int(num_str[0]) + 1) + num_str[1:]
        if valid(new_num):
            results.append(new_num)

    if num_str[-1] != '1':
        new_num = num_str[:-1] + str(int(num_str[-1]) - 1)
        if valid(new_num):
            results.append(new_num)

    new_num = num_str[-1] + num_str[:-1]
    if valid(new_num):
        results.append(new_num)

    new_num = num_str[1:] + num_str[0]
    if valid(new_num):
        results.append(new_num)

    return results

def shortest_path(start, end):
    queue = deque()
    queue.append(start)
    visited = {start: None}

    while queue:
        current = queue.popleft()
        if current == end:
            break
        for neighbor in apply(current):
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)

    path = []
    node = end
    while node:
        path.append(node)
        node = visited[node]
    path.reverse()
    return path

start = input().strip()
end = input().strip()

path = shortest_path(start, end)
for number in path:
    print(number)
