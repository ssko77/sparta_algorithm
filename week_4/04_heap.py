class MaxHeap:
    def __init__(self):
        self.items = [None]

    # 새노드를 맨 끝에 추가한다
    # 지금 넣은 새노드를 부모와 비교한다. 만약 부모보다 크다면 부모아 교체한다
    # 이과정을 꼭대기까지 반복한다.

    def insert(self, value):
        # 구현해보세요!
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:
            parent_index = cur_index // 2
            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                cur_index = parent_index
            else:
                break
        return

    def delete(self):
        # 구현해보세요!
        self.items[1], self.items[len(self.items) - 1] = self.items[len(self.items) - 1], self.items[1]
        prev_max = self.items.pop()

        cur_index = 1
        while cur_index * 2 < len(self.items) - 1 :
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            if self.items[cur_index] < self.items[left_child_index]:
                self.items[cur_index], self.items[left_child_index] = self.items[left_child_index], self.items[cur_index]
                cur_index = left_child_index
            elif self.items[cur_index] < self.items[right_child_index]:
                self.items[cur_index], self.items[right_child_index] = self.items[right_child_index], self.items[cur_index]
                cur_index = right_child_index
            else:
                break
        return prev_max

max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 7, 6, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 5, 6, 2, 4]