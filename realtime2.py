import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
import time

# 初始化MediaPipe Holistic模型
mp_holistic = mp.solutions.holistic
holistic = mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# 加载预训练的模型
model = tf.keras.models.load_model('weizmann_action_model_dense.h5')

# 定义关键点提取函数
def extract_keypoints(results):
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(132)
    face = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(1404)
    left_hand = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(63)
    right_hand = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(63)
    return np.concatenate([pose, face, left_hand, right_hand])

# 打开摄像头
cap = cv2.VideoCapture(0)

fps_time = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # 将帧转换为RGB格式
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # 使用MediaPipe Holistic处理图像并提取关键点
    results = holistic.process(image)
    keypoints = extract_keypoints(results)
    keypoints = keypoints.reshape((1, -1))  # 重新塑造形状以适应模型输入
    
    # 使用模型进行预测
    prediction = model.predict(keypoints)
    
    # 获取最可能的动作标签
    action_label = np.argmax(prediction)
    actions = ['run', 'walk', 'jump','wave'] 

    action = actions[action_label]
    
    # 在帧上绘制预测结果
    cv2.putText(frame, f'Action: {action}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    # 计算FPS
    curr_time = time.time()
    fps = 1.0 / (curr_time - fps_time)
    fps_time = curr_time
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    # 显示帧
    cv2.imshow('Webcam', frame)
    
    # 按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
