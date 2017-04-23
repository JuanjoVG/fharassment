import tensorflow as tf
from numpy.ma import array

from TrainDataset import TrainDataset


class HarassmentDetector:
    y = None
    x = tf.placeholder(tf.float32, [None, 10])
    W = tf.Variable(tf.zeros([10, 3]))
    b = tf.Variable(tf.zeros([3]))

    def init(self):
        self.y = tf.nn.softmax(tf.matmul(self.x, self.W) + self.b)

        y_ = tf.placeholder(tf.float32, [None, 3])
        cross_entropy = tf.reduce_mean(
            -tf.reduce_sum(y_ * tf.log(self.y), reduction_indices=[1]))  ## tf.nn.softmax_cross_entropy_with_logits
        train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

        self.sess = tf.InteractiveSession()
        tf.global_variables_initializer().run()

        ts = TrainDataset()
        ds = ts.get_dataset()

        for _ in range(1000):
            batch_xs, batch_ys = ds.next_batch(5)
            self.sess.run(train_step, feed_dict={self.x: batch_xs, y_: batch_ys})
        pass

    def detect(self, tone_scores):
        if self.y is None:
            print('The model it isn\'t trained')
            return
        x_test = array(tone_scores).reshape(1, 10)
        answer = self.sess.run(self.y, feed_dict={self.x: x_test})
        return answer
