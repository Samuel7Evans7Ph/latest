import tensorflow as tf
from tensorflow.keras.layers import Layer
class L1Dist(Layer):

  #init method-inheritance
    def __init__(self,**kwargs):
        super().__init__()

    def call(self,input_embedding,validation_embedding):
    # distance=tf.math.abs(input_embedding-validation_embedding)
        input_embedding = tf.convert_to_tensor(input_embedding)
        validation_embedding = tf.convert_to_tensor(validation_embedding)
        distance = tf.math.abs(input_embedding - validation_embedding)

        return distance
    def get_config(self):
        config = super().get_config()
        return config

    @classmethod
    def from_config(cls, config):
        return cls(**config)
