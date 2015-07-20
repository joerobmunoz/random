class ann:
    def __init__(self, training_set):

        self.p_layer_1_1 = simple_perceptron(None, training_set)
        self.p_layer_1_2 = simple_perceptron(None, training_set)
        self.p_layer_1_3 = simple_perceptron(None, training_set)

        self.p_layer_2_1 = simple_perceptron([self.p_layer_1_1, self.p_layer_1_2, self.p_layer_1_3])
        self.p_layer_2_2 = simple_perceptron([self.p_layer_1_1, self.p_layer_1_2, self.p_layer_1_3])
        self.p_layer_2_3 = simple_perceptron([self.p_layer_1_1, self.p_layer_1_2, self.p_layer_1_3])

        self.p_layer_3_1 = simple_perceptron([self.p_layer_2_1, self.p_layer_2_2, self.p_layer_2_3])

        self.training_set = training_set

    def train(self):
        c = len(self.training_set)
        while c > 0:
            self.p_layer_3_1.feed_fordward()
            c -= 1

        print 'Finished Training.\n'
        # print self.p_layer_3_1.coefficients

    def evaluate(self, record):
        return self.p_layer_3_1.evaluate(record)

class simple_perceptron:
    def __init__(self, parent_perceptrons=None, training_set=None, coefficients=None):
        self.parent_perceptrons = parent_perceptrons
        self.training_set = training_set
        self.coefficients = None
        self.current_record = 0

    def feed_fordward(self):
        # if no parent, train a record off the set
        if self.parent_perceptrons == None and len(self.training_set) > 0:
            return self.train(self.training_set.pop())
        # if parent, train parent
        elif self.parent_perceptrons == None:
            return None
        else:
            layer_outputs = []
            for p in self.parent_perceptrons:
                parent_output = p.feed_fordward()
                if parent_output == None:
                    return

                layer_outputs.append(parent_output)

            record = ([ev[0] for ev in layer_outputs], layer_outputs[0][1])
            # print record
            return self.train(record)

    def evaluate(self, record):
        # if no parent, train a record off the set
        if self.parent_perceptrons == None:
            return self.train(record)
        # if parent, train parent
        else:
            layer_outputs = []
            for p in self.parent_perceptrons:
                parent_output = p.evaluate(record)
                layer_outputs.append(parent_output)

            record = ([ev[0] for ev in layer_outputs], layer_outputs[0][1])

            return self.train(record)

    def train(self, record):
        """
        Input record as a tuple ([list of values], binary classifier)

        Returns an (evaluation number, 0/1 classifier) to be passed into another node.
        """
        # Set variable coefficients
        temp_coefficients = []
        if self.coefficients != None:
            temp_coefficients = self.coefficients
        else:
            # Initialize to 0
            temp_coefficients = [1 for x in record[0]]

         # ax+by+cz > 0
        coefficient_size = len(record[0])

        # Train
        evaluation = sum([record[0][i]*temp_coefficients[i] for i in range(len(record[0]))])
        # Binary classification
        classification = 0
        if evaluation > 0: # 0 threshold
            classification = 1
        else:
            classification = 0

        # Predicted incorrectly
        if classification != record[1] and classification == 1:
            # If over, subtract record from coefficients
            temp_coefficients = [temp_coefficients[i] - record[0][i] for i in range(coefficient_size)]
        elif classification != record[1] and classification == 0:
            # If under, add record to coefficients
            temp_coefficients = [temp_coefficients[i] + record[0][i] for i in range(coefficient_size)]

        self.coefficients = temp_coefficients
        return (evaluation, record[1])