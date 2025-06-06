# demo/baselines.py
def baseline_policy(observation, mode="fifo"):
    queue = observation["ready_queue"]
    if mode == "fifo":
        return queue[0]
    elif mode == "rr":
        return queue[0]  # placeholder: use round-robin state
    elif mode == "sjf":
        return min(queue, key=lambda pid: observation["estimated_burst"][pid])
