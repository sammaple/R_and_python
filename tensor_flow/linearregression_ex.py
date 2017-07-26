import tensorflow as tf
# Numpy通常用于加载，维护与预处理数据
import numpy as np
# 需求队列(还有很多其他类型的column)
#.声明特征集。在这个案例中我们只有一个特征。
features = [tf.contrib.layers.real_valued_column("x", dimension=1)]
# estimator是一个前端调用用于训练与评估的接口，这里有非常多预定义的类型，如Linear Regression, Logistic Regression, Linear Classification, Logistic Classification 以及各种各样的Neural Network Classifiers 与 Regressors. 这里我们用的是Linear Regression
# 定义一个学习器，此处是线性回归
estimator = tf.contrib.learn.LinearRegressor(feature_columns=features)
# TensorFlow有提供了许多工具方法来读写数据集，这里我们使用`numpy_input_fn`，
# 我们不得不告诉方法一共有多少组(num_epochs)，并且每组有多大(batch_size)
x = np.array([1., 2., 3., 4.])
y = np.array([0., -1., -2., -3.])
#Tensorflow 提供了很多方法来读取与设置数据集。这里使用numpy_input_fn，
# 括号中必须告诉这个函数，要多少批数据（num_epochs), 以及每批数据的大小（batch_size)
input_fn = tf.contrib.learn.io.numpy_input_fn({"x":x}, y, batch_size=4,
                                              num_epochs=1000)
# 我们可以通过传入训练所用的数据集调用1000次`fit`方法来一步步训练
estimator.fit(input_fn=input_fn, steps=1000)
# 评估目前模型训练的怎么样。实际运用中，我们需要一个独立的验证与测试数据集避免训练过渡(overfitting)
print(estimator.evaluate(input_fn=input_fn))

#print(estimator.predict(input_fn=input_fn,outputs="scores"))
#print(estimator.predict_scores(input_fn=input_fn))