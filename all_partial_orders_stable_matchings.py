import numpy as np
import adaptation_gale_shapley
import partial_orders
import create_dic
from matching.games import StableMarriage

# File containing preferences lists
filename = "Instance_n4.txt"

# Read dictionaries from the file
all_dicts = create_dic.read_prefs_from_file(filename)

# Separate the dictionaries
proposers_preferences_1 = all_dicts["proposers_preferences_1"]
proposers_preferences_2 = all_dicts["proposers_preferences_2"]
receivers_preferences_1 = all_dicts["receivers_preferences_1"]
receivers_preferences_2 = all_dicts["receivers_preferences_2"]

# Original instance: proposers_preferences and receivers_preferences_1
partial_order_matrices_receivers_1 = partial_orders.construct_partial_order_matrix(receivers_preferences_1)
partial_order_matrices_proposers_1 = partial_orders.construct_partial_order_matrix(proposers_preferences_1)

print(f"Optimal stable matching for the proposers in instance (0,0):")
stable_matching_all_partial_1 = adaptation_gale_shapley.adaptation_gale_shapley_all_partial(partial_order_matrices_proposers_1, partial_order_matrices_receivers_1)

print(f"Optimal stable matching for the receivers in instance (0,0): ")
stable_matching_all_partial_1_receivers = adaptation_gale_shapley.adaptation_gale_shapley_all_partial(partial_order_matrices_receivers_1, partial_order_matrices_proposers_1)

# Combined instance: proposers_preferences and (receivers_preferences_1 + receivers_preferences_2)
print(f"Optimal stable matching for the proposers in combined instance (0,n):")
partial_order_matrices_receivers_12 = partial_orders.construct_partial_order_matrix(receivers_preferences_1, receivers_preferences_2)
print(f"\nPartial order matrices for the women: \n{partial_order_matrices_receivers_12}\n")

stable_matching_all_partial_12 = adaptation_gale_shapley.adaptation_gale_shapley_all_partial(partial_order_matrices_proposers_1, partial_order_matrices_receivers_12)

print(f"Optimal stable matching for the receivers in combined instance (0,n):")
stable_matching_all_partial_12_receivers = adaptation_gale_shapley.adaptation_gale_shapley_all_partial(partial_order_matrices_receivers_12, partial_order_matrices_proposers_1)

# Combined instance: (proposers_preferences_1 + proposers_preferences_2) and (receivers_preferences_1 + receivers_preferences_2)
print(f"Optimal stable matching for the proposers in combined instance (n,n):")
partial_order_matrices_proposers_12 = partial_orders.construct_partial_order_matrix(proposers_preferences_1, proposers_preferences_2)
stable_matching_all_partial_12n = adaptation_gale_shapley.adaptation_gale_shapley_all_partial(partial_order_matrices_proposers_12, partial_order_matrices_receivers_12)
print(f"\nPartial order matrices for the men: \n{partial_order_matrices_proposers_12}\n")

print(f"Optimal stable matching for the receivers in combined instance (n,n):")
stable_matching_all_partial_receivers_12n = adaptation_gale_shapley.adaptation_gale_shapley_all_partial(partial_order_matrices_receivers_12, partial_order_matrices_proposers_12)