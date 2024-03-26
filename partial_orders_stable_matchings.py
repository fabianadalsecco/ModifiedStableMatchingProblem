import numpy as np
import adaptation_gale_shapley
import partial_orders
import create_dic
from matching.games import StableMarriage

# File containing preferences lists
filename = "Instance_n4.txt"

# Read preferences lists from the file
all_dicts = create_dic.read_prefs_from_file(filename)

# Separate the preferences lists
proposers_preferences_1 = all_dicts["proposers_preferences_1"]
proposers_preferences_2 = all_dicts["proposers_preferences_2"]
receivers_preferences_1 = all_dicts["receivers_preferences_1"]
receivers_preferences_2 = all_dicts["receivers_preferences_2"]

# Original instance: proposers_preferences and receivers_preferences_1 (with matching.games library)
proposers_matching = StableMarriage.create_from_dictionaries(proposers_preferences_1, receivers_preferences_1)
proposers_opt_matching = proposers_matching.solve()
print(f"For the proposers in instance (0,0) by matching.games library in Python: \n {proposers_opt_matching}\n")

receivers_matching = StableMarriage.create_from_dictionaries(receivers_preferences_1, proposers_preferences_1)
receivers_opt_matching = receivers_matching.solve()
print(f"For the receivers in instance (0,0) by matching.games library in Python: \n {receivers_opt_matching}\n")

# Original instance: proposers_preferences and receivers_preferences_1
partial_order_matrices_receivers_1 = partial_orders.construct_partial_order_matrices(receivers_preferences_1)
partial_order_matrices_proposers_1 = partial_orders.construct_partial_order_matrices(proposers_preferences_1)

print(f"For the proposers in instance (0,0):")
stable_matching_all_partial_1 = adaptation_gale_shapley.adaptation_gale_shapley_all_partial(partial_order_matrices_proposers_1, partial_order_matrices_receivers_1)

print(f"For the receivers in instance (0,0): ")
stable_matching_all_partial_1_receivers = adaptation_gale_shapley.adaptation_gale_shapley_all_partial(partial_order_matrices_receivers_1, partial_order_matrices_proposers_1)

# Compound instance: proposers_preferences and (receivers_preferences_1 + receivers_preferences_2)
print(f"For the proposers in compound instance (0,n):")
partial_order_matrices_receivers_12 = partial_orders.construct_partial_order_matrices(receivers_preferences_1,
                                                                                      receivers_preferences_2)

stable_matching_all_partial_12 = adaptation_gale_shapley.adaptation_gale_shapley_all_partial(partial_order_matrices_proposers_1, partial_order_matrices_receivers_12)

print(f"For the receivers in compound instance (0,n):")
stable_matching_all_partial_12_receivers = adaptation_gale_shapley.adaptation_gale_shapley_all_partial(partial_order_matrices_receivers_12, partial_order_matrices_proposers_1)


# Compound instance: (proposers_preferences_1 + proposers_preferences_2) and (receivers_preferences_1 + receivers_preferences_2)
partial_order_matrices_proposers_12 = partial_orders.construct_partial_order_matrices(proposers_preferences_1, proposers_preferences_2)
print(f"For the proposers in compound instance (1,n):")
stable_matching_all_partial_122 = adaptation_gale_shapley.adaptation_gale_shapley_all_partial(partial_order_matrices_proposers_12, partial_order_matrices_receivers_12)

print(f"For the receivers in compound instance (1,n):")
stable_matching_all_partial_122_receivers = adaptation_gale_shapley.adaptation_gale_shapley_all_partial(partial_order_matrices_receivers_12, partial_order_matrices_proposers_12)
