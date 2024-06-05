import cv2
import mediapipe as mp
import time

# 初始化MediaPipe姿态识别
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# 初始化摄像头
cap = cv2.VideoCapture(0)

prev_time = 0
while True:
    ret, frame = cap.read()
    if not ret:
        continue
    
    # 转换颜色空间从BGR到RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # 进行姿态检测
    results = pose.process(frame_rgb)
    
    # 绘制姿态检测的结果
    mp.solutions.drawing_utils.draw_landmarks(
        frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # 计算帧率
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    cv2.putText(frame, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

    # 显示图像
    cv2.imshow('Motion Detection', frame)
    
    # 按下'q'键退出
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
