from abc import ABC, abstractmethod


# TODO: it must inherit from NeuronLayer
class OutLayer(ABC):
    def __init__(self, input_shape):
        self.input_shape = input_shape

    @abstractmethod
    def spread(self, inputs):
        pass

    @abstractmethod
    def copy(self):
        pass
