import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

# 加载数据
X = np.load('weizmann_keypoints_flat.npy')
y_encoded = np.load('weizmann_labels_encoded.npy')

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# 构建模型
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(y_train.shape[1], activation='softmax')
])

# 编译模型
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 训练模型
model.fit(X_train, y_train, epochs=30, batch_size=32, validation_split=0.2)

# 保存模型
model.save('weizmann_action_model_dense.h5')
