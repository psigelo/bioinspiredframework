from abc import ABC, abstractmethod

from organism.layers.InputLayer import InputLayer


class Organism(ABC):
    def __init__(self, input_shape, output_shape):
        self.input_layer = None
        self.feature_layers = []
        self.neuron_decision_layers = []
        self.output_layer = None
        self.synaptic_connections = []

    @abstractmethod
    def spread(self, inputs):
        pass

    def set_input_layer(self, input_layer:  InputLayer):
        self.input_layer = input_layer.copy()

    def set_output_layer(self, input_layer:  OutLayer):
        self.input_layer = input_layer.copy()






