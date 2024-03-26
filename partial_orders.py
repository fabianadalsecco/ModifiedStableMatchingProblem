import numpy as np

def construct_partial_order_matrices(receivers_preferences_1, receivers_preferences_2 = None):
    # If there is no modification on the receivers preferences lists
    if receivers_preferences_2 == None:
        receivers_preferences_2 = receivers_preferences_1

    # Unique values for the receivers and proposers sets
    all_receivers = receivers_preferences_1.keys()
    first_receiver = list(receivers_preferences_1.keys())[0]
    all_proposers = np.sort(receivers_preferences_1[first_receiver])  # Condition: each receiver has a list with all the proposers

    # Dictionary of the partial orders matrices for each receiver
    partial_order_matrices_dict = {}

    for i, receiver in enumerate(all_receivers):
        # Preferences list of the receiver i in both instances
        if receivers_preferences_1.get(receiver) and receivers_preferences_2.get(receiver):
            pref_1 = receivers_preferences_1[receiver]
            pref_2 = receivers_preferences_2[receiver]

        # Partial order matrix filling
        partial_order_matrix = np.zeros((len(all_proposers), len(all_proposers)))
        for j, proposer_1 in enumerate(all_proposers):
            for k, proposer_2 in enumerate(all_proposers):
                if proposer_1 != proposer_2:
                    if pref_1.index(proposer_1) < pref_1.index(proposer_2) and pref_2.index(proposer_1) < pref_2.index(proposer_2):
                        partial_order_matrix[j, k] = 1

        partial_order_matrices_dict[receiver] = partial_order_matrix

    return partial_order_matrices_dict


def count_positive_matrix(matrix):
    # Define the relevance level of each receiver for a proposer
    count = 0
    positive_matrix = np.zeros(matrix.shape[0])
    # For each receiver (row), count the number of positive values
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j] == -1:
                break
            elif matrix[i][j] == 1:
                count += 1
        positive_matrix[i] = count
        count = 0
    return positive_matrix


def choose_receiver(positive_matrix):
    # Choose the receiver with the greatest relevance level
    max_value = max(positive_matrix)
    max_index = np.where(positive_matrix == max_value)[0][0]
    return max_index