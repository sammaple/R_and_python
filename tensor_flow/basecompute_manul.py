import tensorflow as tf
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
sess = tf.Session();
add_node = a + b  # 等同于tf.add(a, b)

#当真正运行的时候才传入指定的数据进行计算
print(sess.run(add_node, {a:3, b:4}))
print(sess.run(add_node, {a:[1,3], b:[2,4]}))

add_and_triple = add_node * 3
print(sess.run(add_and_triple, {a:3, b:4.5}))   # (3+4.5)*3