def SimplePerception(training_set, recursion_limit, run=None, variable_coefficients=None):
    """
    Input a training_set as a list of tuples (list of record values,
    classification value), a recursion_limit as an integer, variables as
    a list of variable coefficients.

    This function assumes zero starting values and returns a function when a linear
    separator is found.
    """

    # Start with number of variable assumptions
    # QUESTION: How to deal with non-linear separability? Include other complex
    # variables, but how?
    print 'Run: %s, Coefficients: %s' % (run, variable_coefficients)

    # Set variable coefficients
    temp_coefficients = []
    if variable_coefficients != None:
        temp_coefficients = variable_coefficients
    else:
        # Initialize to 0
        temp_coefficients = [0 for x in training_set[0][0]]

    # ax+by+cz > 0
    coefficient_size = len(training_set[0][0])
    classification_errors = 0

    # Train
    for n in training_set:
        # Evaluate
        evaluation = sum([n[0][i]*temp_coefficients[i] for i in range(len(n[0]))])
        # Binary classification
        classification = 0
        if evaluation > 0: # 0 threshold
            classification = 1
        else:
            classification = 0

        # Predicted incorrectly
        if classification != n[1] and classification == 1:
            # If over, subtract record from coefficients
            classification_errors += 1
            temp_coefficients = [temp_coefficients[i] - n[0][i] for i in range(coefficient_size)]
        elif classification != n[1] and classification == 0:
            # If under, add record to coefficients
            classification_errors -= 1
            temp_coefficients = [temp_coefficients[i] + n[0][i] for i in range(coefficient_size)]
    if classification_errors == 0:
        print temp_coefficients
        return temp_coefficients
    elif run < recursion_limit:
        return SimplePerception(training_set, recursion_limit, run+1, temp_coefficients)
    else:
        print 'Not linearly separable data!'
        return None

# Training set example:
# test_set = [([1,2,3],0), ([1,2,3],0), ([1,2,3],0), ([1,2,3],0)]
# test_set = [([1, 2, 3], 0), ([2, 4, 5], 1), ([1, 2, 3], 0), ([3, 5, 6], 1)]
test_set = [([1, 2, 3], 0), ([2, 4, 5], 1), ([1, 2, 3], 0), ([3, 5, 6], 1), ([0, 2, 6], 0)]

SimplePerception(test_set, 3, 0)