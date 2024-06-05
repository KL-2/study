#使用LSTM预测比特币价格
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
plt.style.use('ggplot')

import tensorflow as tf
tf.logging.set_verbosity(tf.logging.ERROR)

import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv("data/btc.csv")
# print(df.head())
data=df['Close'].values
scaler=StandardScaler()
data=scaler.fit_transform(data.reshape(-1,1))
#绘制并观察比特币价格波动
# plt.plot(data)
# plt.xlabel('Days')
# plt.ylabel('Price')
# plt.grid()
# plt.show()
def get_data(data, window_size):
    X = []
    y = []
    
    i = 0
    
    while (i + window_size) <= len(data) - 1:
        X.append(data[i:i+window_size])
        y.append(data[i+window_size])
        
        i += 1
    assert len(X) ==  len(y)
    return X, y


X, y = get_data(data, window_size = 7)
#train set
X_train  = np.array(X[:1000])
y_train = np.array(y[:1000])

#test set
X_test = np.array(X[1000:])
y_test = np.array(y[1000:])
# print(X_train.shape)#(1000, 7, 1)
batch_size=7
window_size=7
hidden_layer=256
learning_rate=0.001


input = tf.placeholder(tf.float32, [batch_size, window_size, 1])
target = tf.placeholder(tf.float32, [batch_size, 1])
#输入门
U_i = tf.Variable(tf.truncated_normal([1, hidden_layer], stddev=0.05))
W_i = tf.Variable(tf.truncated_normal([hidden_layer, hidden_layer], stddev=0.05))
b_i = tf.Variable(tf.zeros([hidden_layer]))
#遗忘门

U_f = tf.Variable(tf.truncated_normal([1, hidden_layer], stddev=0.05))
W_f = tf.Variable(tf.truncated_normal([hidden_layer, hidden_layer], stddev=0.05))
b_f = tf.Variable(tf.zeros([hidden_layer]))
#输出门

U_o = tf.Variable(tf.truncated_normal([1, hidden_layer], stddev=0.05))
W_o = tf.Variable(tf.truncated_normal([hidden_layer, hidden_layer], stddev=0.05))
b_o = tf.Variable(tf.zeros([hidden_layer]))
#候选状态
U_g = tf.Variable(tf.truncated_normal([1, hidden_layer], stddev=0.05))
W_g = tf.Variable(tf.truncated_normal([hidden_layer, hidden_layer], stddev=0.05))
b_g = tf.Variable(tf.zeros([hidden_layer]))
#输出层

V = tf.Variable(tf.truncated_normal([hidden_layer, 1], stddev=0.05))
b_v = tf.Variable(tf.zeros([1]))

def LSTM_cell(input, prev_hidden_state, prev_cell_state):


    it = tf.sigmoid(tf.matmul(input, U_i) + tf.matmul(prev_hidden_state, W_i) + b_i)

    ft = tf.sigmoid(tf.matmul(input, U_f) + tf.matmul(prev_hidden_state, W_f) + b_f)

    ot = tf.sigmoid(tf.matmul(input, U_o) + tf.matmul(prev_hidden_state, W_o) + b_o)

    gt = tf.tanh(tf.matmul(input, U_g) + tf.matmul(prev_hidden_state, W_g) + b_g)

    ct = (prev_cell_state * ft) + (it * gt)

    ht = ot * tf.tanh(ct)

    return ct, ht
#前向传播
y_hat=[]
#for each batch we compute the output and store it in the y_hat list
for i in range(batch_size): 
  
    #initialize hidden state and cell state for each batch
    hidden_state = np.zeros([1, hidden_layer], dtype=np.float32) 
    cell_state = np.zeros([1, hidden_layer], dtype=np.float32)
    
    
    #compute the hidden state and cell state of the LSTM cell for each time step
    for t in range(window_size):
        cell_state, hidden_state = LSTM_cell(tf.reshape(input[i][t], (-1, 1)), hidden_state, cell_state)
        
    #compute y_hat and append it to y_hat list
    y_hat.append(tf.matmul(hidden_state, V) + b_v)
#反向传播
losses=[]
for i in range(len(y_hat)):
    losses.append(tf.losses.mean_squared_error(tf.reshape(target[i],(-1,1)),y_hat[i]))
    loss=tf.reduce_mean(losses)

#梯度剪辑
gradients=tf.gradients(loss,tf.trainable_variables())
clipped,_=tf.clip_by_global_norm(gradients,4.)
optimizer=tf.train.AdamOptimizer(learning_rate).apply_gradients(zip(gradients,tf.trainable_variables()))
#train LSTM
session=tf.Session()
session.run(tf.global_variables_initializer())
epochs=10

for i in range(epochs):
    train_predictions=[]
    index=0
    epoch_loss=[]
    while(index+batch_size)<=len(X_train):
        X_batch=X_train[index:index+batch_size]
        Y_batch=y_train[index:index+batch_size]

        #predict the price and compute the loss
        predicted,loss_val,_=session.run([y_hat,loss,optimizer],
        feed_dict={input:X_batch,target:Y_batch})

        #store the loss in the epoch_loss list
        epoch_loss.append(loss_val)

        #store the predictions in the train_predictions list
        train_predictions.append(predicted)
        index+=batch_size
    if (i%10):
        print('Epoch {},Loss {}'.format(i,np.mean(epoch_loss)))

predicted_output=[]
i=0
while i+batch_size<=len(X_test):
    output=session.run([y_hat],feed_dict={input:X_test[i:i+batch_size]})
    i+=batch_size
    predicted_output.append(output)
predicted_values_test=[]
for i in range(len(predicted_output)):
    for j in range(len(predicted_output[i][0])):
        predicted_values_test.append(predicted_output[i][0][j])
predictions=[]
for i in range(1280):
    if i >=1000:
        predictions.append(predicted_values_test[i-1019])
    else:
        predictions.append(None)

plt.figure(figsize=(16,7))
plt.plot(data,label='Actual')
plt.plot(predictions,label='Predicted')
plt.legend()
plt.xlabel('Days')
plt.ylabel('Price')
plt.grid()
plt.show()

















































































































