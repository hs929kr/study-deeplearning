import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
import random

mnist=input_data.read_data_sets("MNIST_data/",one_hot=True)
nb_classes = 10 #0~9
training_epochs=30
batch_size=100
learning_rate=0.01
X=tf.placeholder(tf.float32,[None,784])
Y=tf.placeholder(tf.float32,[None,nb_classes])
W=tf.Variable(tf.random_normal([784,nb_classes])) 
b=tf.Variable(tf.random_normal([nb_classes]))
hypothesis=tf.matmul(X,W)+b

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=hypothesis,labels=Y))
optimizer=tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost) #Adam : review later

sess=tf.Session()
sess.run(tf.global_variables_initializer())

for epoch in range(training_epochs):
	avg_cost=0
	total_batch=int(mnist.train.num_examples/batch_size)
	for i in range(total_batch):
		batch_xs,batch_ys=mnist.train.next_batch(batch_size)
		feed_dict = {X:batch_xs, Y:batch_ys}
		c,_ = sess.run([cost,optimizer],feed_dict=feed_dict)
		avg_cost+=c/total_batch
	print('Epoch:','%04d'%(epoch+1),'cost = ','{:.9f}'.format(avg_cost))
print('Learning Finished!')

correct_prediction = tf.equal(tf.argmax(hypothesis,1),tf.argmax(Y,1))
accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
print('Accuracy:', sess.run(accuracy,feed_dict={X:mnist.test.images,Y:mnist.test.labels}))
