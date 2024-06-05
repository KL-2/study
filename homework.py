import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 数据定义
data = {
    'outlook': ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy', 'overcast', 'sunny', 'sunny', 'rainy', 'sunny', 'overcast', 'overcast', 'rainy'],
    'temperature': ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'cool', 'mild', 'cool', 'mild', 'mild', 'mild', 'hot', 'mild'],
    'humidity': ['high', 'high', 'high', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'high'],
    'windy': [False, True, False, False, False, True, True, False, False, False, True, True, False, True],
    'play': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']
}
df = pd.DataFrame(data)

# 数据预处理
label_encoder = LabelEncoder()
for col in df.columns:
    df[col] = label_encoder.fit_transform(df[col])

X = df.drop('play', axis=1)
y = df['play']

# 初始化模型
tree_model = DecisionTreeClassifier()
nb_model = GaussianNB()

# 弱分类器数量为20
n_estimators = 20
bagging_tree = BaggingClassifier(base_estimator=tree_model, n_estimators=n_estimators, random_state=0)
adaboost_tree = AdaBoostClassifier(base_estimator=tree_model, n_estimators=n_estimators, random_state=0)
bagging_nb = BaggingClassifier(base_estimator=nb_model, n_estimators=n_estimators, random_state=0)
adaboost_nb = AdaBoostClassifier(base_estimator=nb_model, n_estimators=n_estimators, random_state=0)

# 训练模型并计算准确率
bagging_tree.fit(X, y)
accuracy_bagging_tree = accuracy_score(y, bagging_tree.predict(X))

adaboost_tree.fit(X, y)
accuracy_adaboost_tree = accuracy_score(y, adaboost_tree.predict(X))

bagging_nb.fit(X, y)
accuracy_bagging_nb = accuracy_score(y, bagging_nb.predict(X))

adaboost_nb.fit(X, y)
accuracy_adaboost_nb = accuracy_score(y, adaboost_nb.predict(X))

# 绘制结果
plt.rcParams['font.family'] = 'SimHei'  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号
plt.bar(['Bagging Tree', 'AdaBoost Tree', 'Bagging NB', 'AdaBoost NB'],
        [accuracy_bagging_tree, accuracy_adaboost_tree, accuracy_bagging_nb, accuracy_adaboost_nb])
plt.xlabel('模型')
plt.ylabel('准确率')
plt.title('模型准确率（弱分类器数量为20）')
plt.ylim([0, 1])
plt.show()
