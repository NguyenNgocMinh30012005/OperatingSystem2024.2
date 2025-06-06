# demo/app.py
import gradio as gr
from run_simulation import main as run

def launch(policy, workload):
    import os
    os.system(f"python demo/run_simulation.py --policy {policy} --workload {workload} --render")

gr.Interface(fn=launch,
             inputs=[
                gr.Dropdown(["fifo", "rr", "sjf", "xgb", "ppo"], label="Chính sách"),
                gr.Dropdown(["cpu", "io", "mixed"], label="Workload"),
             ],
             outputs="text").launch()
