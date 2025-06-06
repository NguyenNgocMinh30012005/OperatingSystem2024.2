# demo/workload_utils.py

import numpy as np

def generate_workload(workload_type="mixed", num_tasks=20):
    workload = []
    for i in range(num_tasks):
        if workload_type == "cpu":
            burst = np.random.randint(20, 40)
        elif workload_type == "io":
            burst = np.random.randint(5, 15)
        else:  # mixed
            burst = np.random.randint(5, 40)
        task = {
            "pid": i,
            "arrival_time": np.random.randint(0, 50),
            "burst_time": burst,
            "priority": np.random.randint(1, 5)
        }
        workload.append(task)
    return workload
