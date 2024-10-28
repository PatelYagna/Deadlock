class BankersAlgorithm:
    def __init__(self, available, max_claim, allocation, need):
        self.available = available  # Vector of length m. Available resources
        self.max_claim = max_claim   # n x m matrix. Maximum resource claim
        self.allocation = allocation   # n x m matrix. Currently allocated resources
        self.need = need               # Need = Max - Allocation
    
    def safety(self):
        n_processes = len(self.allocation)
        work = self.available.copy()  # Work vector
        finish = [False] * n_processes  # Finish status for each process
        safe_path = []  # List to hold the safe sequence

        while len(safe_path) < n_processes:
            found = False
            
            for i in range(n_processes):
                # Check if the process is not finished and its needs can be satisfied
                can_allocate = True
                for j in range(len(work)):
                    if self.need[i][j] > work[j]:  # Check if needs are less than or equal to work
                        can_allocate = False
                        break

                if not finish[i] and can_allocate:
                    # Update work and finish status
                    for j in range(len(work)):
                        work[j] += self.allocation[i][j]
                    finish[i] = True
                    safe_path.append(f'P{i}')  # Append process to safe sequence
                    found = True
                    break
            
            if not found:  # No process can be executed
                return False, []

        return True, safe_path

# Test data
processes = ['P0', 'P1', 'P2', 'P3', 'P4']
A, B, C = 10, 5, 7
available = [3, 3, 2]  # Available resources

allocation = [[0, 1, 0],  # P0
              [2, 0, 0],  # P1
              [3, 0, 2],  # P2
              [2, 1, 1],  # P3
              [0, 0, 2]]  # P4

max_claim = [[7, 5, 3],  # P0
              [3, 2, 2],  # P1
              [9, 0, 2],  # P2
              [2, 2, 2],  # P3
              [4, 3, 3]]  # P4

# Calculate the need matrix
need = []
for i in range(len(max_claim)):
    need_row = []
    for j in range(len(max_claim[0])):
        need_row.append(max_claim[i][j] - allocation[i][j])
    need.append(need_row)

# Instantiate the BankersAlgorithm class
banker = BankersAlgorithm(available, max_claim, allocation, need)

# Check if the system is in a safe state and print the result
is_safe, safe_path = banker.safety()

if is_safe:
    print("Safe Processes Path:", safe_path)
else:
    print("Deadlock!!!")