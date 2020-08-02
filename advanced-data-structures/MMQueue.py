class MMQueue:
    def __init__(self):
        self.miq = collections.deque()
        self.maq = collections.deque()
        self.len = 0

    def enqueue(self, v):
        self.len += 1

        c = 1
        while self.miq and self.miq[-1][0] > v:
            c += self.miq.pop()[1]
        self.miq.append([v, c])

        c = 1
        while self.maq and self.maq[-1][0] < v:
            c += self.maq.pop()[1]
        self.maq.append([v, c])

    def dequeue(self):
        self.len -= 1

        ami = self.min()
        ama = self.max()

        self.miq[0][1] -= 1
        if self.miq[0][1] <= 0:
            self.miq.popleft()
        self.maq[0][1] -= 1
        if self.maq[0][1] <= 0:
            self.maq.popleft()

    def min(self):
        return self.miq[0][0] if self.miq else 0

    def max(self):
        return self.maq[0][0] if self.maq else 0

    def __len__(self):
        return self.len
