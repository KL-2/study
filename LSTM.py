import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

import numpy as np
from sklearn.datasets import make_blobs

# 创建一个简单的特征点数据和标签数据
n_samples = 300
n_features = 10
n_clusters = 3

# 创建特征点数据
X, _ = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, random_state=42)

# 创建随机的标签数据，用于测试
y = np.random.choice(['action1', 'action2', 'action3'], size=n_samples)

print("特征点数据 X 的形状：", X.shape)
print("标签数据 y 的形状：", y.shape)


# # 假设我们已经有特征点数据和对应的标签
# X = keypoints
# y = labels  # 替换为实际标签

# 数据预处理
lb = LabelBinarizer()
y = lb.fit_transform(y)

# 分割数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 构建LSTM模型
model = Sequential()
model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(LSTM(128, return_sequences=False, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(y.shape[1], activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 训练模型
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

# 保存模型
model.save('action_model.h5')
