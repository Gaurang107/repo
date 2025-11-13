# CPU Scheduling Algorithm: FCFS

n = int(input("Enter number of processes: "))
processes = []
bt = []   # Burst Time

for i in range(n):
    processes.append(i+1)
    bt.append(int(input(f"Enter Burst Time for Process {i+1}: ")))

wt = [0]*n   # Waiting Time
tat = [0]*n  # Turnaround Time

# Calculate Waiting Time
for i in range(1, n):
    wt[i] = wt[i-1] + bt[i-1]

# Calculate Turnaround Time
for i in range(n):
    tat[i] = wt[i] + bt[i]

# Display results
print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"P{i+1}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")

avg_wt = sum(wt)/n
avg_tat = sum(tat)/n

print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")

