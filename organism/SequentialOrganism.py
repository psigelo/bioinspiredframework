from organism.Organism import Organism


class SequentialOrganism(Organism):
    def __init__(self, input_shape, output_shape):
        super().__init__(input_shape, output_shape)

    def spread(self, inputs):
        last_spread = self.input_layer.spread(inputs)
        last_spread = self.synaptic_connections[self.input_layer.hash_code].spread(last_spread)
        for feature_layer_it in self.feature_layers:
            last_spread = feature_layer_it.spread(last_spread)
            last_spread = self.synaptic_connections[feature_layer_it.hash_code].spread(last_spread)
        for feature_layer_it in self.neuron_decision_layers:
            last_spread = feature_layer_it.spread(last_spread)
            last_spread = self.synaptic_connections[feature_layer_it.hash_code].spread(last_spread)
        output = self.output_layer.spread(last_spread)
        return output

