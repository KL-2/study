import tensorflow as tf
# 👇️ disable tensorflow warnings
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'



#定义模型
#顺序模型
model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(256,activation='relu'))
model.add(tf.keras.layers.Dense(128,activation='relu'))
model.add(tf.keras.layers.Dense(10,activation='softmax'))
#功能模型
# input=layers.Input(shape=(2,))
# layer1=layers.Dense(10,activation='relu')(input)
# layer2=layers.Dense(10,activation='relu')(layer1)
# output=layers.Dense(1,activation='sigmoid')(layer2)
# model=models.Model(input=input,output=output)

#编译模型
model.compile(loss='sparse_categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])

#加载数据集
mnist = tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test)=mnist.load_data()
#训练和测试集规范化
x_train,x_test=tf.cast(x_train/255.,tf.float32),tf.cast(x_test/255.,tf.float32)
y_train,y_test=tf.cast(y_train,tf.int64),tf.cast(y_test,tf.int64)
#训练模型
model.fit(x=x_train,y=y_train,epochs=10,batch_size=32)

#评估模型
model.evaluate(x=x_test,y=y_test)
