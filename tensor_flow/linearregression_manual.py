import tensorflow as tf

# 创建线性回归的两个权重变量
w = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)
# 为自变量x创建占位符
x = tf.placeholder(tf.float32)

sess = tf.Session();
#建立一元线性模型
linear_model = w * x + b

#tf.Variable()并不会去初始化变量，要初始化变量，必须调用特定的操作,如下：
init = tf.global_variables_initializer()
sess.run(init)

#print(sess.run(linear_model, {x: [1,2,3,4]}))

#上面我们已经常见了一个一元线性模型，并且给定了初始的参数w,b值，
# 然后输出了一组模型的预测值。但是我们怎么知道参数这样设的时候模型的好坏呢？
# 此时，就需要知道一组真实的y值，来和预测的y值作比较从而建立损失函数。
# 这组y值一般都是外部进来的数据，所以也需要placehoder。
#损失函数是真实值与预测值之间的差距，这里我们用一个标准的损失函数来评估线性模型：平方差和

y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
#print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))
"""
fixW = tf.assign(w, [-1.])
fixB = tf.assign(b, [1.])
sess.run([fixW,fixB] )
print(sess.run(loss,  {x:[1,2,3,4], y:[0,-1,-2,-3]}))
"""
# 比如Tensorflow中提供了一些优化器，通过损失最小化的目标来改变变量。最简单的优化器是梯度下降法，使用如下：
#[array([-0.9999969], dtype=float32), array([ 0.99999082], dtype=float32)]
#以上是在学习率为0.01梯度下降法下训练了1000次的参数，可见几乎等于了我们之前设置的最优的参数了。
optimizer = tf.train.GradientDescentOptimizer(0.01)   ## 括号内的是学习率
train = optimizer.minimize(loss)
sess.run(init)  # 初始化变量
x_train = [1,2,3,4]
y_train = [0,-1,-2,-3]
for i in range(1000):  # 迭代1000次
    #sess.run(train, {x:[1,2,3,4], y:[0,-1,-2,-3]})
    sess.run(train, {x: x_train, y: y_train})
print(sess.run([w,b]))