from abc import ABC, abstractmethod

import tensorflow as tf


class BaseTFModel(ABC):
    @abstractmethod
    def __init__(self) -> None:
        """Create a Keras classification model to be attacked.

        The model must have an input shape of (224, 224, 3) and uint8 (0..255)
        dtype. Any preprocessing (convert to floats, normalize) should also be
        a part of this model.
        In subclasses, assign the model to some protected attribute (with
        underscore) and make it accessible via keras_model() property.
        """
        pass

    @property
    @abstractmethod
    def keras_model(self) -> tf.keras.Model:
        pass

    def compute_grad_input(x: tf.Tensor, y_true: tf.Tensor) -> tf.Tensor:
        """Compute gradient of loss with respect to inputs.

        Hint: use GradientTape and sparse_categorical_crossentropy().

        Args:
            x: a batch of input images, shape (batch_size, 224, 224, 3)
            y_true: ground truth class indices, shape (batch_size,)

        Returns:
            Gradients tensor, shape (batch_size, 224, 224, 3)
        """
        raise NotImplementedError
