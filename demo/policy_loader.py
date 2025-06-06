# demo/policy_loader.py
import onnxruntime as ort
import numpy as np
from stable_baselines3 import PPO

def load_policy(policy_name):
    if policy_name == "ppo":
        return PPO.load("Step4/best_model.zip")


    elif policy_name == "xgb":
        sess = ort.InferenceSession("Step2/xgb_os_sched.onnx")
        input_name = sess.get_inputs()[0].name

        def predict(obs):
            # Giả sử chọn tiến trình đầu tiên hoặc lấy tiến trình có remaining_time nhỏ nhất
            obs_matrix = obs.reshape(-1, 7)  # shape: (5, 7)
            # Ví dụ chọn tiến trình có thời gian còn lại thấp nhất
            idx = np.argmin(obs_matrix[:, 6])
            feature_vector = obs_matrix[idx]  # → shape: (7,)
            
            # Nếu model yêu cầu 12 features: bạn cần mở rộng thêm ở đây!
            if len(feature_vector) < 12:
                padded = np.pad(feature_vector, (0, 12 - len(feature_vector)), mode='constant')
            else:
                padded = feature_vector[:12]  # cắt bớt nếu dài quá

            result = sess.run(None, {input_name: padded.reshape(1, -1)})
            return result[0][0].argmax()

        return type("XGBPolicy", (), {"predict": lambda self, obs, deterministic=True: [predict(obs)]})()
