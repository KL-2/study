# import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'#只输出ERROR + FATAL
# x=tf.constant(1,name='x')
# y=tf.constant(1,name='y')
# a=tf.constant(3,name='a')
# b=tf.constant(3,name='b')
# with tf.name_scope("Product"):
#     with tf.name_scope("prob1"):
#         prob1=tf.multiply(x,y,name='prob1')
#     with tf.name_scope("prob2"):
#         prob2=tf.multiply(a,b,name='prob2')
# with tf.name_scope("sum"):
#     sum=tf.add(prob1,prob2,name='sum')

# with tf.Session() as sess:
#     writer=tf.summary.FileWriter(logdir='./graphs',graph=sess.graph)
#     print(sess.run(sum))

import warnings
warnings.filterwarnings('ignore')
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
tf.logging.set_verbosity(tf.logging.ERROR)
import matplotlib.pyplot as plt

mnist=input_data.read_data_sets("data/mnist",one_hot=True)
# print("No of images in training set {}".format(mnist.train.images.shape))

# print("No of labels in training set {}".format(mnist.train.labels.shape))

# print("No of images in test set {}".format(mnist.test.images.shape))

# print("No of labels in test set {}".format(mnist.test.labels.shape))
# No of images in training set (55000, 784)
# No of labels in training set (55000, 10)
# No of images in test set (10000, 784)   
# No of labels in test set (10000, 10)

img1=mnist.train.images[0].reshape(28,28)
plt.imshow(img1,cmap='Greys')
# plt.show()
#number of neurons in input layer
num_input=784

#num of neurons in hidden layer 1
num_hidden1=512

#num of neurons in hidden layer 2
num_hidden2=256

#num of neurons in hidden layer 3
num_hidden3=128

#num of neurons in output layer
num_output=10

with tf.name_scope('input'):
    X=tf.placeholder("float",[None,num_input])
with tf.name_scope('output'):
    Y=tf.placeholder("float",[None,num_output])

with tf.name_scope('weights'):
    weights={
        'w1':tf.Variable(tf.truncated_normal([num_input,num_hidden1],stddev=0.1),name='weight_1'),
        #变量创建
        'w2':tf.Variable(tf.truncated_normal([num_hidden1,num_hidden2],stddev=0.1),name='weight_2'),
        'w3':tf.Variable(tf.truncated_normal([num_hidden2,num_hidden3],stddev=0.1),name='weight_3'),
        'out':tf.Variable(tf.truncated_normal([num_hidden3,num_output],stddev=0.1),name='weight_4')       
    }

with tf.name_scope('biases'):
    biases={
        'b1':tf.Variable(tf.constant(0.1,shape=[num_hidden1]),name='bias_1'),
        #创建常量
        'b2':tf.Variable(tf.constant(0.1,shape=[num_hidden2]),name='bias_2'),
        'b3':tf.Variable(tf.constant(0.1,shape=[num_hidden3]),name='bias_3'),
        'out':tf.Variable(tf.constant(0.1,shape=[num_output]),name='bias_4'),
    }

with tf.name_scope('Model'):
    with tf.name_scope('layer1'):
        layer_1=tf.nn.relu(tf.add(tf.matmul(X,weights['w1']),biases['b1']))
    with tf.name_scope('layer2'):
        layer_2=tf.nn.relu(tf.add(tf.matmul(layer_1,weights['w2']),biases['b2']))
    with tf.name_scope('layer3'):
        layer_3=tf.nn.relu(tf.add(tf.matmul(layer_2,weights['w3']),biases['b3']))
    with tf.name_scope('output_layer'):
        y_hat=tf.nn.sigmoid(tf.add(tf.matmul(layer_3,weights['out']),biases['out']))

with tf.name_scope('Loss'):
    loss=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y_hat,labels=Y))
learning_rate=1e-4
optimizer=tf.train.AdamOptimizer(learning_rate).minimize(loss)

with tf.name_scope('Accuracy'):
    predicted_digit=tf.argmax(y_hat,1)
    actual_digit=tf.argmax(Y,1)
    correct_pred=tf.equal(predicted_digit,actual_digit)
    accuracy=tf.reduce_mean(tf.cast(correct_pred,tf.float32))
tf.summary.scalar("Accuracy",accuracy)
tf.summary.scalar("Loss",loss)
merge_summary=tf.summary.merge_all()


init=tf.global_variables_initializer()
learning_rate=1e-4
num_iterations=1000
batch_size=128
with tf.Session() as sess:
    sess.run(init)
    summary_writer=tf.summary.FileWriter('./graphs',graph=sess.graph)
    for i in range(num_iterations):
        batch_x,batch_y=mnist.train.next_batch(batch_size)
        sess.run(optimizer,feed_dict={X:batch_x,Y:batch_y})
        if i%100==0:
            batch_loss,batch_accuracy,summary=sess.run([loss,accuracy,merge_summary],feed_dict={X:batch_x,Y:batch_y})
            summary_writer.add_summary(summary,i)
            print('Iteration:{},Loss:{},Accuracy:{}'.format(i,batch_loss,batch_accuracy))




