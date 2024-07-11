import tensorflow as tf
from tensorflow.keras import models
import matplotlib.pyplot as plt
import numpy as np

# Load dataset MNIST
(_, _), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# Preprocessing data
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255
test_labels = tf.keras.utils.to_categorical(test_labels)

# Muat model yang telah disimpan
model = models.load_model('mnist_model.h5')

# Evaluasi model yang dimuat
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f"Test accuracy: {test_acc}")

# Memprediksi angka pada data test set
predictions = model.predict(test_images)

# Menampilkan beberapa prediksi
def plot_predictions(images, labels, predictions, num=10):
    plt.figure(figsize=(10, 10))
    indices = np.random.choice(len(images), num, replace=False)
    for i, idx in enumerate(indices):
        plt.subplot(5, 2, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(images[idx].reshape(28, 28), cmap=plt.cm.binary)
        predicted_label = np.argmax(predictions[idx])
        true_label = np.argmax(labels[idx])
        if predicted_label == true_label:
            color = 'blue'
        else:
            color = 'red'
        plt.xlabel(f"Predicted: {predicted_label}, True: {true_label}", color=color)
    plt.tight_layout()
    plt.show()

# Menampilkan prediksi untuk 10 gambar acak dalam test set
plot_predictions(test_images, test_labels, predictions, num=10)
