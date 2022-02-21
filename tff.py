import os
import numpy as np
import tensorflow as tf
from tensorflow import keras

current_dir = os.getcwd() 

config = tf.ConfigProto
config.gpu_options.allow_growth=True
sess = tf.Session(config=config)

# Append data/mnist.npz to the previous path to get the full path
data_path = os.path.join(current_dir, "data/mnist.npz") 

# Get only training set
(training_images, training_labels), _ = tf.keras.datasets.mnist.load_data(path=data_path) 



def reshape_and_normalize(images):
    
    ### START CODE HERE

    # Reshape the images to add an extra dimension
    images = training_images.reshape(60000, 28, 28, 1)
    
    # Normalize pixel values
    images = training_images / 255.0
    
    ### END CODE HERE

    return images

(training_images, _), _ = tf.keras.datasets.mnist.load_data(path=data_path) 

# Apply your function
training_images = reshape_and_normalize(training_images)

print(f"Maximum pixel value after normalization: {np.max(training_images)}\n")
print(f"Shape of training set after reshaping: {training_images.shape}\n")
print(f"Shape of one image after reshaping: {training_images[0].shape}")


class myCallback(tf.keras.callbacks.Callback):
    # Define the correct function signature for on_epoch_end
    def on_epoch_end(self, epoch, logs={}):
        if logs.get('accuracy') is not None and logs.get('accuracy') > 0.99: # @KEEP
            print("\nReached 99% accuracy so cancelling training!") 
            # Stop training once the above condition is met
            self.model.stop_training = True
### END CODE HERE


# GRADED FUNCTION: convolutional_model
def convolutional_model():
    
    ### START CODE HERE

    # Define the model, it should have 5 layers:
    # - A Conv2D layer with 32 filters, a kernel_size of 3x3, ReLU activation function
    #    and an input shape that matches that of every image in the training set
    # - A MaxPooling2D layer with a pool_size of 2x2
    # - A Flatten layer with no arguments
    # - A Dense layer with 128 units and ReLU activation function
    # - A Dense layer with 10 units and softmax activation function
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(units=128, activation='relu'),
        tf.keras.layers.Dense(units=10, activation='softmax')
        ]) 
    ### END CODE HERE
    # Compile the model
    model.compile(optimizer='adam', 
                  loss='sparse_categorical_crossentropy', 
                  metrics=['accuracy'])     
    return model


# Save your untrained model
model = convolutional_model()

# Instantiate the callback class
callbacks = myCallback()

# Train your model (this can take up to 5 minutes)
histiry = model.fit(training_images, training_labels, epochs=10, callbacks=[callbacks])

print(f"Your model was trained for {len(history.epoch)} epochs")