import warnings
warnings.filterwarnings('ignore')

import random
import numpy as np
import pandas as pd
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.ERROR)
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv('./data/songdata.csv')
# print(df.head())
# print(df.shape[0])#57650
# print(len(df['artist'].unique()))#643
# print(df['artist'].value_counts()[:10])
# print(df['artist'].value_counts().values.mean())#89.65785381026438
data=', '.join(df['text'])
# print(data[:369])
#将数据集中的所有唯一字符存储到名为chars变量中，作为词汇表
chars=sorted(list(set(data)))
vocab_size=len(chars)
#神经网络只接收数字的输入，需要将词汇表中所有字符转换成一个数字
char_to_ix={ch:i for i,ch in enumerate(chars)}#将所有字符映射到他们的下标
ix_to_char={i:ch for i,ch in enumerate(chars)}#将所有下标映射成各自字符
# print(char_to_ix)
#{'\n': 0, ' ': 1, '!': 2, '"': 3, "'": 4, '(': 5, ')': 6, ',': 7, '-': 8, '.': 9, '0': 10, '1': 11, '2': 12, '3': 13, '4': 14, '5': 15, '6': 16, '7': 17, '8': 18, '9': 19, ':': 20, '?': 21, 'A': 22, 'B': 23, 'C': 24, 'D': 25, 'E': 26, 'F': 27, 'G': 28, 'H': 29, 'I': 30, 'J': 31, 'K': 32, 'L': 33, 'M': 34, 'N': 35, 'O': 36, 'P': 37, 'Q': 38, 'R': 39, 'S': 40, 'T': 41, 'U': 42, 'V': 43, 'W': 44, 'X': 45, 'Y': 46, 'Z': 47, '[': 48, ']': 49, 'a': 50, 'b': 51, 'c': 52, 'd': 53, 'e': 54, 'f': 55, 'g': 56, 'h': 57, 'i': 58, 'j': 59, 'k': 60, 'l': 61, 'm': 62, 'n': 63, 'o': 64, 'p': 65, 'q': 66, 'r': 67, 's': 68, 't': 69, 'u': 70, 'v': 71, 'w': 72, 'x': 73, 'y': 74, 'z': 75}
# print(char_to_ix['s'])     
# print(ix_to_char[68])#一对一

def one_hot_encoder(index):
    return np.eye(vocab_size)[index]

# print(one_hot_encoder(3))
#[0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
hidden_size=100
seq_length=25
learning_rate=1e-1
seed_value=42
tf.set_random_seed(seed_value)
random.seed(seed_value)
inputs=tf.placeholder(shape=[None,vocab_size],dtype=tf.float32,name="inputs")
targets=tf.placeholder(shape=[None,vocab_size],dtype=tf.float32,name="target")
init_state=tf.placeholder(shape=[1,hidden_size],dtype=tf.float32,name="state")
initializer=tf.random_normal_initializer(stddev=0.1)
#前向传播
with tf.variable_scope("RNN") as scope:
    h_t=init_state
    y_hat=[]
    for t,x_t in enumerate(tf.split(inputs,seq_length,axis=0)):
        if t>0:
            scope.reuse_variables()

        #input to hidden layer weights
        U=tf.get_variable("U",[vocab_size,hidden_size],initializer=initializer)

        #hidden to hidden layer weights
        W=tf.get_variable("W",[hidden_size,hidden_size],initializer=initializer)

        #output to hidden layer weights
        V=tf.get_variable("V",[hidden_size,vocab_size],initializer=initializer)

        #bias for hidden layer
        bh=tf.get_variable("bh",[hidden_size],initializer=initializer)

        #bias for output layer
        by=tf.get_variable("by",[vocab_size],initializer=initializer)

        h_t=tf.tanh(tf.matmul(x_t,U)+tf.matmul(h_t,W)+bh)

        y_hat_t=tf.matmul(h_t,V)+by

        y_hat.append(y_hat_t)

output_softmax=tf.nn.softmax(y_hat[-1])
outputs=tf.concat(y_hat,axis=0)
loss=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=targets,logits=outputs))
#将RNN最终隐藏状态存储在hprev中，使用最终状态进行预测
hprev=h_t
#定义BPTT

minimizer=tf.train.AdamOptimizer()
gradients=minimizer.compute_gradients(loss)
threshold=tf.constant(5.0,name="grad_clipping")
clipped_gradients=[]
for grad,var in gradients:
    clipped_grad=tf.clip_by_value(grad,-threshold,threshold)
    clipped_gradients.append((clipped_grad,var))
update_gradients=minimizer.apply_gradients(clipped_gradients)

#开始生成歌词
sess=tf.Session()
init=tf.global_variables_initializer()
sess.run(init)

pointer=0
iteration=0
while True:
    
    if pointer + seq_length+1 >= len(data) or iteration == 0:
        hprev_val = np.zeros([1, hidden_size])
        pointer = 0  

    input_sentence=data[pointer:pointer+seq_length]
    output_sentence=data[pointer+1:pointer+seq_length+1]
    input_indices=[char_to_ix[ch] for ch in input_sentence]
    target_indices=[char_to_ix[ch] for ch in output_sentence]
    input_vector=one_hot_encoder(input_indices)
    target_vector=one_hot_encoder(target_indices)
    hprev_val,loss_val,_=sess.run([hprev,loss,update_gradients],feed_dict={inputs:input_vector,targets:target_vector,init_state:hprev_val})
        #make predictions on every 500th iteration 
    if iteration % 500 == 0:
        sample_length=500
        random_index=random.randint(0,len(data)-seq_length)
        sample_input_sent=data[random_index:random_index+seq_length]
        sample_input_indices=[char_to_ix[ch] for ch in sample_input_sent]
        sample_prev_state_val=np.copy(hprev_val)
        predicted_indices=[]
        for t in range(sample_length):
            sample_input_vector=one_hot_encoder(sample_input_indices)
                       #compute the probability of all the words in the vocabulary to be the next character
            probs_dist, sample_prev_state_val = sess.run([output_softmax, hprev],feed_dict={inputs: sample_input_vector,init_state: sample_prev_state_val})
            ix=np.random.choice(range(vocab_size),p=probs_dist.ravel())
            sample_input_indices=sample_input_indices[1:]+[ix]
            predicted_indices.append(ix)
        predicted_chars=[ix_to_char[ix] for ix in predicted_indices]
        text=' '.join(predicted_chars)
        #predict the predict text on every 50000th iteration
        if iteration %1000 == 0:           
            print ('\n')
            print (' After %d iterations' %(iteration))
            print('\n %s \n' % (text,))   
            print('-'*115)

            
    #increment the pointer and iteration
    pointer += seq_length
    iteration += 1













