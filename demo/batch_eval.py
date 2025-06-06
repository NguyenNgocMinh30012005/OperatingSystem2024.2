# demo/batch_eval.py
from run_simulation import main as run
import os

for policy in ["xgb", "ppo"]:
    print(f"\n--- Đánh giá policy: {policy} ---")
    os.system(f"python demo/run_simulation.py --policy {policy} --workload mixed")
