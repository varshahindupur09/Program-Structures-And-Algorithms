# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT
# n_tc = int(input())
# size_of_input_array = int(input()) 
# matrix = []
# for i in range(size_of_input_array):
#     matrix.append([int(j) for j in input().split()])

# print(n_tc)
# print(size_of_input_array)
# print(matrix) ## [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.head is None

    def enqueue(self, x):
        new_node = Node(x)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        dequeue_data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        return dequeue_data

def is_path_possible(matrix, N):
    if matrix[0][0] == 0 or matrix[N-1][N-1] == 0:
        return "NOT POSSIBLE"

    directions = [(0, 1), (1, 0)]  # Right and Down movements
    queue = SList()
    queue.enqueue((0, 0))
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[0][0] = True

    while not queue.is_empty():
        x, y = queue.dequeue()
        
        if x == N-1 and y == N-1:
            return "POSSIBLE"
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and matrix[nx][ny] == 1:
                queue.enqueue((nx, ny))
                visited[nx][ny] = True

    return "NOT POSSIBLE"

# Example usage
def main():
    test_cases = int(input())
    for _ in range(test_cases):
        N = int(input())
        matrix = []
        for _ in range(N):
            matrix.append(list(map(int, input().split())))
        print(is_path_possible(matrix, N))

if __name__ == "__main__":
    main()
