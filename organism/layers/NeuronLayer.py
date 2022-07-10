from abc import ABC, abstractmethod

from utils.hash_generator import create_hash


class NeuronLayer(ABC):
    def __init__(self, input_shape, output_shape):
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.hash_code = create_hash(str(type(self)))  # ToDo: check that type(self) use the actual instance name

    @abstractmethod
    def spread(self, inputs):
        pass

    @abstractmethod
    def copy(self):
        pass
