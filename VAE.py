import tensorflow as tf

(train_images, _), (test_images, _) = tf.keras.datasets.mnist.load_data()

print(train_images.shape())

def process_images(images):
    images = images.reshape()