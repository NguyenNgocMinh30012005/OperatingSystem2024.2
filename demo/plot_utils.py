# demo/plot_utils.py

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_timeline(history):
    tasks = history["completed"]
    fig, ax = plt.subplots(figsize=(10, 2))
    for task in tasks:
        start, end = task["start"], task["end"]
        ax.broken_barh([(start, end - start)], (10, 9),
                       facecolors='tab:blue')
        ax.text((start + end) / 2, 15, f"PID {task['pid']}", 
                ha='center', va='bottom', fontsize=8, rotation=45)
    ax.set_ylim(5, 35)
    ax.set_xlim(0, max(t["end"] for t in tasks) + 5)
    ax.set_xlabel("Time")
    ax.set_yticks([])
    ax.set_title("CPU Scheduling Timeline")
    plt.tight_layout()
    plt.show()
