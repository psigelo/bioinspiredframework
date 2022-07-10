from organism.layers.NeuronLayer import NeuronLayer


class Dense(NeuronLayer):
    def __init__(self, input_shape, output_sape):
        super().__init__(input_shape, output_sape)

    # Override Method from NeuronLayer
    def spread(self, inputs):
        pass

