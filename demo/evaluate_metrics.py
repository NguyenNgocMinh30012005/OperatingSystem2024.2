# demo/evaluate_metrics.py
import numpy as np

def evaluate_performance(history):
    total_tasks = len(history["completed"])
    avg_latency = np.mean([t["end"] - t["arrival"] for t in history["completed"]])
    avg_energy = np.mean([t["energy"] for t in history["completed"]])
    print(f"\n📊 Tổng tiến trình: {total_tasks}")
    print(f"⏱️  Latency TB: {avg_latency:.2f}")
    print(f"🔋 Năng lượng TB: {avg_energy:.2f}")
