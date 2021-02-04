from abc import ABC, abstractmethod

import tensorflow as tf


class BaseTFModel(ABC):
    @abstractmethod
    def get_keras_model() -> tf.keras.Model:
        pass

    def compute_grad_input(x):
        raise NotImplementedError
