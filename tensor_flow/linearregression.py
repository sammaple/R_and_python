# 3个例子来源
# http://blog.csdn.net/sinat_33761963/article/details/56286408?locationNum=9&fps=1

import numpy as np
import tensorflow as tf

# Model parameters
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
# Model input and output
x = tf.placeholder(tf.float32)
linear_model = W * x + b
y = tf.placeholder(tf.float32)
# loss
loss = tf.reduce_sum(tf.square(linear_model - y)) # sum of the squares
# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)
# training data
x_train = [1,2,3,4]
y_train = [0,-1,-2,-3]
# training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init) # reset values to wrong
for i in range(1000):
  sess.run(train, {x:x_train, y:y_train})

# evaluate training accuracy
#print(sess.run([W, b]))#需要评估 loss结果的话需要重新执行

# Add ops to save and restore all the variables.
saver = tf.train.Saver()
print(sess.run([W, b, loss], {x:x_train, y:y_train}))

save_path = saver.save(sess, "model.ckpt")
print("Model saved in file: %s" % save_path)
#curr_W, curr_b, curr_loss = sess.run([W, b, loss])
#curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x:x_train, y:y_train})
#print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))