import partial_orders
import adaptation_gale_shapley
from matching.games import StableMarriage

proposers_preferences_1 = {
    '1': ['D', 'A', 'C', 'B'],
    '2': ['B', 'D', 'A', 'C'],
    '3': ['D', 'B', 'C', 'A'],
    '4': ['D', 'B', 'C', 'A'],
}

receivers_preferences_1 = {
    'A': ['2', '3', '1', '4'],
    'B': ['3', '2', '4', '1'],
    'C': ['4', '1', '3', '2'],
    'D': ['3', '2', '1', '4'],
}

proposers_matching = StableMarriage.create_from_dictionaries(proposers_preferences_1, receivers_preferences_1)
proposers_opt_matching = proposers_matching.solve()
print(f"Optimal stable matching for the proposers in instance (0,0) by matching.games library in Python: \n {proposers_opt_matching}\n")

# ------------------------------------------------------------------------------------------------------------------------------------------
partial_order_matrices_receivers_1 = partial_orders.construct_partial_order_matrix(receivers_preferences_1)
partial_order_matrices_proposers_1 = partial_orders.construct_partial_order_matrix(proposers_preferences_1)

stable_matching_1 = gale_shapley.gale_shapley_partial(proposers_preferences_1, partial_order_matrices_receivers_1)
print(f"Optimal stable matching for the proposers in instance (0,0): \n Partial: {stable_matching_1}")
stable_matching_all_partial_1 = gale_shapley.gale_shapley_all_partial(partial_order_matrices_proposers_1, partial_order_matrices_receivers_1)
print(f" All partial: {stable_matching_all_partial_1}\n")

