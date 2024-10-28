class bankers_algorithm:
    def __init__(self, available, max, allocation, need): # intial function. Defintions are from slide L5 from pg.30
        self.available = available # vector of length m. If available [j] = k, there are k instances of resource type Rj available
        self.max = max # n x m matrix. If Max [i,j] = k, then process Pi may request at most k instances of resource type Rj
        self.allocation = allocation # n x m matrix. If Allocation[i,j] = k then Pi is currently allocated k instances of R
        self.need = need # need [i,j] = Max[i,j] – Allocation [i,j]

    def safety(self): # followed slides for L5
        n = len(self.allocation)
        work = self.available.copy()
        finish = [False] * n
        safe_path = []

        while len(safe_path) < n:
            found = False
            for i in range(n):
                if not finish[i]:
                    safe = True
                    for j in range(len(self.need[i])):
                        if self.need[i][j] > work[j]:
                            safe = False
                            break
                    if safe:
                        for j in range(len(work)):
                            work[j] += self.allocation[i][j]
                        finish[i] = True
                        safe_path.append(f'P{i}')
                        found = True
                        break
            if not found:
                return False, []
        return True, safe_path


n = ['P0', 'P1', 'P2', 'P3', 'P4']
A, B, C = 10, 5, 7
m = [A, B, C]

allocation = [[0, 1, 0],  # P0
              [2, 0, 0],  # P1
              [3, 0, 2],  # P2
              [2, 1, 1],  # P3
              [0, 0, 2]]  # P4

max = [[7, 5, 3],  # P0
       [3, 2, 2],  # P1
       [9, 0, 2],  # P2
       [2, 2, 2],  # P3
       [4, 3, 3]]  # P4

available = [3, 3, 2]

need = []
for i in range(len(max)):
    temporary = []
    for j in range(len(max[0])):
        temporary.append(max[i][j] - allocation[i][j])
    need.append(temporary)

banker = bankers_algorithm(available, max, allocation, need)
safe, safe_path = banker.safety()

if safe:
    print("Safe Path:", safe_path)
else:
    print("Detected Deadlock111")