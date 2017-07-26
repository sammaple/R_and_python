import tensorflow as tf
co = tf.constant("hi tensorflow")
session = tf.Session()
print(session.run(co))