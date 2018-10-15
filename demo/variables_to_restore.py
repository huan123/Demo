# import tensorflow as tf

# v = tf.Variable(0, dtype= tf.float32, name= "v")
# for variables in tf.global_variables():
#     print(variables.name)
# ema = tf.train.ExponentialMovingAverage(0.99)
# maintain_averages_op = ema.apply(tf.global_variables())
# for variables in tf.global_variables():
#     print()


# v = tf.Variable(0, dtype=tf.float32, name= "v")
# ema = tf.train.ExponentialMovingAverage(0.99)
# print(ema.variables_to_restore())
#
# saver = tf.train.Saver(ema.variables_to_restore())
# with tf.Session() as sess:
#     saver.restore(sess, "/model.ckpt")
#     print(sess.run(v))

import tensorflow as tf
from tensorflow.python.framework  import graph_util

v1 = tf.Variable(tf.constant(1.0, shape = [1]), name= "v1")
v2 = tf.Variable(tf.constant(2.0, shape = [1]), name= "v2")
result = v1 + v2

init_op = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init_op)
    graph_def = tf.get_default_graph().as_graph_def()
    output_graph_def = graph_util.convert_variables_to_constants(
        sess, graph_def, ['add']
    )
    with tf.gfile.GFile("./combined_model.pb", "wb") as f:
        f.write(output_graph_def.SerializeToString())

import tensorflow as tf
from tensorflow.python.platform import  gfile

with tf.Session() as sess:
    model_filename = "./combined_model.pb"
    with gfile.FastGFile(model_filename, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
    result = tf.import_graph_def(graph_def, return_elements=["add:0"])
    print(sess.run(result))
