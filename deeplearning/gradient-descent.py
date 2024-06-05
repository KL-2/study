'''梯度下降，一阶优化算法(只计算一阶导数)
凸函数（只有一个最小值）
非凸函数（有多个最小值）：多个局部最小值+全局最小值
'''

import warnings
warnings.filterwarnings('ignore')
import random
import math
import numpy as np
from matplotlib import pyplot as plt

data=np.random.randn(500,2)
#初始化两个参数m和b
theta=np.zeros(2)

def loss_function(data,theta):
    m=theta[0]
    b=theta[1]
    loss=0
    for i in range(len(data)):
        x=data[i,0]
        y=data[i,1]
        y_hat=(m*x+b)
        loss=loss+((y-y_hat)**2)
        mse=loss/float(len(data))
        return mse

def compute_gradients(data,theta):
    gradients=np.zeros(2)
    N=float(len(data))
    m=theta[0]
    b=theta[1]
    for i in range(len(data)):
        x=data[i,0]
        y=data[i,1]
        #m损失的梯度
        gradients[0]+=-(2/N)*x*(y-((m*x)+b))
        #b损失的梯度
        gradients[1]+=-(2/N)*(y-((theta[0]*x)+b))
    #添加epsilon以避免被零除
    epsilon=1e-6
    gradients=np.divide(gradients,N+epsilon)
    return gradients


num_iterations=5000
#学习率
lr=1e-2

loss=[]
theta=np.zeros(2)
for t in range(num_iterations):
    # compute gradients
    gradients=compute_gradients(data,theta)
    #update parameter
    theta=theta-(lr*gradients)
    #store the loss
    loss.append(loss_function(data,theta))
plt.plot(loss)
plt.grid()
plt.show()

'''
梯度下降:                                       迭代数据集中所有数据点后,更新模型参数
随机梯度下降(SGD,Stochastic Gradient Descent):  迭代数据集中每个数据点后,更新模型参数
小批量梯度下降(Mini-Batch Gradient Descent):    迭代数据集中n个数据点后, 更新模型参数
对于大型数据集,小批量梯度下降更优
'''
def minibatch(data,theta,lr=1e-2,minibatch_ratio=0.01,num_iterations=1000):
    minibatch_size=int(math.ceil(len(data)*minibatch_ratio))
    for i in range(num_iterations):
        sample_size=random.sample(range(len(data)),minibatch_size)
        np.random.shuffle(data)
        sample_data=data[0:sample_size[0],:]
        grad=compute_gradients(sample_data,theta)
        theta=theta-(lr*grad)
        loss.append(loss_function(data,theta))        

#动量梯度下降momentum

def momentum(data,theta,lr=1e-2,gamma=0.9,num_iterations=1000):
    vt=np.zeros(theta.shape[0])
    for i in range (num_iterations):
        gradients=compute_gradients(data,theta)
        vt=gamma*vt+lr*gradients
        theta=theta-vt
        loss.append(loss_function(data,theta))
    return loss

#内斯特罗夫加速梯度算法NAG(Nesterov Accelerated Gradient)
def NAG(data,theta,lr=1e-2,gamma=0.9,num_iterations=1000):
    vt=np.zeros(theta.shape[0])
    for i in range(num_iterations):
        gradients=compute_gradients(data,theta-gamma*vt)
        vt=gamma*vt+lr*gradients
        theta=theta-vt
        loss.append(loss_function(data,theta))
    return loss


def AdaGrad(data,theta,lr=1e-2,epsilon=1e-8,num_iterations=10000):
    gradients_sum=np.zeros(theta.shape[0])
    for t in range(num_iterations):
        gradients=compute_gradients(data,theta)
        gradients_sum+=gradients**2
        gradient_update=gradients/(np.sqrt(gradients_sum+epsilon))
        theta=theta-(lr*gradient_update)
        loss.append(loss_function(data,theta))
    return loss

def AdaDelta(data,theta,gamma=0.9,epsilon=1e-5,num_iterations=1000):
    #running average of gradients
    E_grad2=np.zeros(theta.shape[0])

    #running average of parameter update
    E_delta_theta2=np.zeros(theta.shape[0])
    for t in range(num_iterations):
        gradients=compute_gradients(data,theta)
        E_grad2=(gamma*E_grad2)+((1.-gamma)*(gradients**2))
        delta_theta=-(np.sqrt(E_delta_theta2+epsilon))/(np.sqrt(E_grad2+epsilon))*gradients
        E_delta_theta2=(gamma*E_delta_theta2)+((1.-gamma)*(delta_theta**2))
        theta=theta+delta_theta
        loss.append(loss_function(data,theta))
    return loss


def RMSProp(data, theta, lr = 1e-2, gamma = 0.9, epsilon = 1e-6, num_iterations = 100): 
    
    loss= []
    
    #initialize running average of gradients
    E_grad2 = np.zeros(theta.shape[0])
    
    for t in range(num_iterations):
        
        #compute gradients with respect to theta
        gradients = compute_gradients(data, theta)
        
        #compute running average of gradients as given in equation (17)
        E_grad2 = (gamma * E_grad2) + ((1. - gamma) * (gradients ** 2))
        
        #update model parameter as given in equation (18)
        theta = theta - (lr / (np.sqrt(E_grad2 + epsilon)) * gradients)
        
        #store the loss
        loss.append(loss_function(data,theta))

    return loss

def Adam(data, theta, lr = 1e-2, beta1 = 0.9, beta2 = 0.9, epsilon = 1e-6, num_iterations = 1000):
   
    loss = []
    
    #initialize first moment mt
    mt = np.zeros(theta.shape[0])
    
    #initialize second moment vt
    vt = np.zeros(theta.shape[0])
    
    for t in range(num_iterations):
        
        #compute gradients with respect to theta
        gradients = compute_gradients(data, theta)
        
        #update first moment mt as given in equation (19)
        mt = beta1 * mt + (1. - beta1) * gradients
        
        #update second moment vt as given in equation (20)
        vt = beta2 * vt + (1. - beta2) * gradients ** 2
        
        #compute bias-corected estimate of mt (21)
        mt_hat = mt / (1. - beta1 ** (t+1))
        
        #compute bias-corrected estimate of vt (22)
        vt_hat = vt / (1. - beta2 ** (t+1))
        
        #update the model parameter as given in (23)
        theta = theta - (lr / (np.sqrt(vt_hat) + epsilon)) * mt_hat
      
        loss.append(loss_function(data,theta))

    return loss

def Adamax(data, theta, lr = 1e-2, beta1 = 0.9, beta2 = 0.999, epsilon = 1e-6, num_iterations = 500):
    
    loss = []
    
    #initialize first moment mt
    mt = np.zeros(theta.shape[0])
    
    #initialize second moment vt
    vt = np.zeros(theta.shape[0])
    
    for t in range(num_iterations):
        
        #compute gradients with respect to theta
        gradients = compute_gradients(data, theta)
        
        #compute first moment mt as given in equation (24)
        mt = beta1 * mt + (1. - beta1) * gradients
        
        #compute second moment vt as given in equation (25)
        vt = np.maximum(beta2 * vt, np.abs(gradients))
        
        #compute bias-corrected estimate of mt as given in equation (26)
        mt_hat = mt / (1. - beta1 ** (t+1))
        
        #update theta as give in equation (27)
        theta = theta - ((lr / (vt + epsilon)) * mt_hat)
        
        #store the loss
        loss.append(loss_function(data,theta))

    return loss

def AMSGrad(data, theta, lr = 1e-2, beta1 = 0.9, beta2 = 0.9, epsilon = 1e-6, num_iterations = 50):
    
    loss = []
    
    #initialize first moment mt
    mt = np.zeros(theta.shape[0])
    
    #initialize second moment vt
    vt = np.zeros(theta.shape[0])
    
    #initialize vt_hat
    vt_hat = np.zeros(theta.shape[0])
    
    for t in range(num_iterations):
        
        #compute gradients with respect to theta
        gradients = compute_gradients(data, theta)
        
        #compute first moment as given in equation (28)
        mt = beta1 * mt + (1. - beta1) * gradients
        
        #compute second moment as given in equation (29)
        vt = beta2 * vt + (1. - beta2) * gradients ** 2
        
        #compute vt_hat as given in equation (30)
        vt_hat = np.maximum(vt_hat,vt)
        
        #compute bias-corrected estimate of mt as shown in equation (31)
        mt_hat = mt / (1. - beta1 ** (t+1))
        
        #update model parameter theta as given in (32)
        theta = theta - (lr / (np.sqrt(vt_hat) + epsilon)) * mt_hat

        #store loss
        loss.append(loss_function(data,theta))

    return loss


def Nadam(data, theta, lr = 1e-2, beta1 = 0.9, beta2 = 0.999, epsilon = 1e-6, num_iterations = 50):
   
    loss = []
    
    #initialize first moment mt
    mt = np.zeros(theta.shape[0])
    
    #initialize second moment vt
    vt = np.zeros(theta.shape[0])
    beta_prod = 1
    
    for t in range(num_iterations):
        
        #compute gradients with respect to theta
        gradients = compute_gradients(data, theta)
        
        #compute first moment as given in equation (33)
        mt = beta1 * mt + (1. - beta1) * gradients
        
        #compute second moment as given in equation (34)
        vt = beta2 * vt + (1. - beta2) * gradients ** 2
        beta_prod = beta_prod * (beta1)
        
        #compute bias-corrected estimates of mt as shown in (35)
        mt_hat = mt / (1. - beta_prod)
        
        #compute bias-corrected estimate of gt as shown in (36)
        g_hat = gradients / (1. - beta_prod)
        
        #compute bias-corrected estimate of vt as shown in (37)
        vt_hat = vt / (1. - beta2 ** (t))
        
        #compute mt tilde as shown in (38)
        mt_tilde = (1-beta1**t+1) * mt_hat + ((beta1**t)* g_hat)
        
        #update theta as given in (39)
        theta = theta - (lr / (np.sqrt(vt_hat) + epsilon)) * mt_hat
        
        #store the loss
        loss.append(loss_function(data,theta))

    return loss





























