# tensorboard --logdir="log/" --host=10.27.0.193 --port=6001
import tensorflow as tf
from tensorflow.python.platform import gfile
model = 'best_model_cnn_lstm.pb'
graph = tf.get_default_graph()
graph_def = graph.as_graph_def()
graph_def.ParseFromString(gfile.FastGFile(model, 'rb').read())
tf.import_graph_def(graph_def, name='graph')
summaryWriter = tf.summary.FileWriter('log/', graph)