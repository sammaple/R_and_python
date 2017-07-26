# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Functions for downloading and reading MNIST data."""

"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import gzip
import os
import tempfile

import numpy
from six.moves import urllib
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets

mnist = read_data_sets("MNIST_data/", one_hot=True)

import tensorflow as tf
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x,W) + b)

y_ = tf.placeholder("float", [None,10])
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
"""

import tensorflow as tf

# 导入mnist数据
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# 定义输入图片(tensor)变量x，其结构为任意个数的784个点的图片
x = tf.placeholder(tf.float32, [None, 784])

# 定义训练因素
W = tf.Variable(tf.zeros([784, 10])) # 定义权重W, 10张784个点的图片
b = tf.Variable(tf.zeros([10])) # 定义偏移量，0~9

# 导入公式 softmax(W * x + b)
y = tf.nn.softmax(tf.matmul(x, W) + b)

# 使用cross-entropy(一个常见的loss模型)来定义结果有多差(定义一个标准，这样Tensorflow才能通过不断减少这个差值，来接近最终我们想要的模型)
y_ = tf.placeholder(tf.float32, [None, 10]) # 定义正确的
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1])) # 导入croos-entropy公式
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy) # 使用"梯度减少"算法通过0.5的减少比率来学习

sess = tf.InteractiveSession() # 在InteractiveSession中启动模型
tf.global_variables_initializer().run() # 初始化我们创建的模型

# 每一步我们通过训练的集合生成100个随机的数据，通过train_step喂乳数据到图片x与对应的表示的数字y_
for _ in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# 验证模型训练结果

# tf.argmax(y, 1)是对所有输入模型认为的最有可能的结果，tf.argmax(y_,1)实际上对所有输入最有可能的结果，然后通过tf.equal判断两个是否相等
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
# 由于correct_prediction计算出来的是一个Boolean数组，因此我们要通过tf.cast将其转为float，如[True, False, True, True]应该转为[1, 0, 1, 1]其中1占其中的0.75
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# 最后输出通过模型计算出来的正确率，这个模型的正确率会在92%左右
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))