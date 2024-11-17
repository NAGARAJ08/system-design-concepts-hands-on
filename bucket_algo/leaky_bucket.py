from collections import deque
import time


class LeakyBucket:

    def __init__(self, capacity, leak_rate) -> None:

        self.capacity = capacity
        self.leak_rate = leak_rate
        self.queue = deque()
        self.last_leak_time = time.time()

    def leak(self):

        now = time.time()

        elpapsed = now - self.last_leak_time

        leaks_to_process = int(elpapsed*self.leak_rate)

        for _ in range(min(leaks_to_process, len(self.queue))):
            self.queue.popleft()

        self.last_leak_time = now

    def allow_request(self, request):

        self.leak()

        if len(self.queue) < self.capacity:
            self.queue.append(request)
            return True
        else:
            return False


if __name__ == '__main__':

    leaky_buc = LeakyBucket(capacity=2, leak_rate=1)

    for i in range(10):

        time.sleep(0.6)

        if leaky_buc.allow_request(f"Request-{i+1}"):
            print(f"Request {i+1}: Allowed")
        else:
            print(f"Request {i+1}: Denied")
