import numpy as np
import tensorflow as tf
from numpy.ma import array

from Dataset import DataSet


class HarassmentDetector:
    y = None
    x = tf.placeholder(tf.float32, [None, 10])
    W = tf.Variable(tf.zeros([10, 2]))
    b = tf.Variable(tf.zeros([2]))

    def init(self):
        self.y = tf.nn.softmax(tf.matmul(self.x, self.W) + self.b)

        y_ = tf.placeholder(tf.float32, [None, 2])
        cross_entropy = tf.reduce_mean(
            -tf.reduce_sum(y_ * tf.log(self.y), reduction_indices=[1]))  ## tf.nn.softmax_cross_entropy_with_logits
        train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

        self.sess = tf.InteractiveSession()
        tf.global_variables_initializer().run()

        xs = np.array([[0.9, 0., 0., 0., 0., 0., 0.87, 0., 0., 0.],
                       [1., 0., 0., 0., 0., 0., 0.95, 0., 0., 0.],
                       [0.89, 0., 0., 0., 0., 0., 0.89, 0., 0., 0.],
                       [0., 0.9, 0., 0., 0., 0.87, 0., 0., 0., 0.],
                       [0., 1., 0., 0., 0., 0.95, 0., 0., 0., 0.],
                       [0., 0.89, 0., 0., 0., 0.89, 0., 0., 0., 0.],
                       [0.9, 0., 0., 0., 0., 0., 0.87, 0., 0., 0.],
                       [1., 0., 0., 0., 0., 0., 0.95, 0., 0., 0.],
                       [0.89, 0., 0., 0., 0., 0., 0.89, 0., 0., 0.],
                       [0., 0.9, 0., 0., 0., 0.87, 0., 0., 0., 0.],
                       [0., 1., 0., 0., 0., 0.95, 0., 0., 0., 0.],
                       [0., 0.89, 0., 0., 0., 0.89, 0., 0., 0., 0.],
                       [0.9, 0., 0., 0., 0., 0., 0.87, 0., 0., 0.],
                       [1., 0., 0., 0., 0., 0., 0.95, 0., 0., 0.],
                       [0.89, 0., 0., 0., 0., 0., 0.89, 0., 0., 0.],
                       [0., 0.9, 0., 0., 0., 0.87, 0., 0., 0., 0.],
                       [0., 1., 0., 0., 0., 0.95, 0., 0., 0., 0.],
                       [0., 0.89, 0., 0., 0., 0.89, 0., 0., 0., 0.]
                       ], np.float32)
        ys = np.array(
            [[1., 0.], [1., 0.], [1., 0.], [0., 1.], [0., 1.], [0., 1.], [1., 0.], [1., 0.], [1., 0.], [0., 1.],
             [0., 1.], [0., 1.], [1., 0.], [1., 0.], [1., 0.], [0., 1.], [0., 1.], [0., 1.]], np.float32)

        ds = DataSet(xs, ys)

        for _ in range(1000):
            batch_xs, batch_ys = ds.next_batch(5)
            self.sess.run(train_step, feed_dict={self.x: batch_xs, y_: batch_ys})

        return

    def detect(self, tone_scores):
        if self.y is None:
            print('The model it isn\'t trained')
            return
        x_test = array(tone_scores).reshape(1, 10)
        answer = self.sess.run(self.y, feed_dict={self.x: x_test})
        return answer
