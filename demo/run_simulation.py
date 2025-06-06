# demo/run_simulation.py
import argparse
from policy_loader import load_policy
from baselines import baseline_policy
from CPUSchedulerEnv import CPUSchedulerEnv  # import đúng từ Step3 nếu cần

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--policy", choices=["xgb", "ppo"], required=True)
    parser.add_argument("--workload", default="mixed", choices=["cpu", "io", "mixed"])
    parser.add_argument("--render", action="store_true", help="Print scheduling timeline")
    args = parser.parse_args()

    # Sửa đoạn này ✅
    env = CPUSchedulerEnv(num_processes=5, max_steps=50)

    if args.policy in ["fifo", "rr", "sjf"]:
        policy_fn = lambda obs: baseline_policy(obs, mode=args.policy)
    else:
        model = load_policy(args.policy)
        policy_fn = lambda obs: model.predict(obs, deterministic=True)[0]

    obs = env.reset()
    done, rewards, steps = False, [], 0

    while not done:
        action = policy_fn(obs)
        obs, reward, done, info = env.step(action)
        rewards.append(reward)
        steps += 1
        if args.render:
            env.render()

    print(f"\n✅ Done in {steps} steps.")


if __name__ == "__main__":
    main()
