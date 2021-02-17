from .base_tf_model import BaseTFModel
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.applications import ResNet50

class ResNet50Model(BaseTFModel):
    """A wrapper class for ResNet50 classification model.

    Use tf.keras.applications to obtain the core network.
    """

    def __init__(self) -> None:
        """Create ResNet50 classification model.

        tf.keras.applications provides a preprocessing method for its ResNet50
        model, please use it here.
        """
        super().__init__()
        # TODO (DariaShel): implement model
        self.model = Sequential()
        self.model.add(ResNet50())

        
        


    @property
    def keras_model(self):
        raise NotImplementedError
