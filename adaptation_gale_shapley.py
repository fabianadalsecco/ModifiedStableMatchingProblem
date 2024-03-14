import partial_orders

# Only receivers have partial orders
def adaptation_gale_shapley_loop(proposers_prefs, receivers_partial_prefs, opt_matching, set_proposers):
    not_found = 0
    for proposer, receivers in proposers_prefs.items():
        proposer_index = set_proposers.index(proposer)

        # If the proposer is not yet matched
        if opt_matching[proposer] == "None":
            for receiver in receivers:
                # If the receiver is already matched with another agent
                if (any(receiver in receivers_matching for receivers_matching in opt_matching.values())):
                    receiver_prefs_matrix = receivers_partial_prefs[receiver]
                    for proposer_matching, receiver_matching in opt_matching.items():
                        if receiver_matching == receiver:
                            proposer_matching = proposer_matching
                            proposer_matching_index = set_proposers.index(proposer_matching)
                            break

                    # Comparison of the proposer with the matched agent w.r.t the receiver's preferences
                    if receiver_prefs_matrix[proposer_index, proposer_matching_index] == 1:
                        opt_matching[proposer] = receiver
                        opt_matching[proposer_matching] = "None"
                        break

                # If the receiver is not yet matched
                else:
                    opt_matching[proposer] = receiver
                    break

        # If after the iterations, there is still no stable matching found
        if opt_matching[proposer] == "None":
            not_found = 1

    return opt_matching, not_found

def adaptation_gale_shapley_partial(proposers_prefs, receivers_partial_prefs):
    # Definition of the optimal stable matching
    proposer_opt = {proposer : "None" for proposer in proposers_prefs}
    all_proposers = list(proposers_prefs.keys())

    # While there is a proposer with no acceptance of receivers
    while any("None" in prefs_list for prefs_list in proposer_opt.values()):
        proposer_opt, not_found = adaptation_gale_shapley_loop(proposers_prefs,
                                         receivers_partial_prefs,
                                         proposer_opt,
                                         all_proposers)
        # If a proposer is rejected by all the receivers, quit the loop
        if not_found == 1:
            print("A stable matching could not be found")
            break

    return proposer_opt


# Both proposers and receivers have partial orders
def adaptation_gale_shapley_all_partial_loop(proposers_partial_prefs, receivers_partial_prefs, set_proposers, set_receivers, positive_dic, opt_matching):
    not_found = 0
    for proposer, receivers_matrix in proposers_partial_prefs.items():
        proposer_index = set_proposers.index(proposer)
        positive_dic[proposer] = partial_orders.count_positive_matrix(receivers_matrix)

        # If the proposer is not yet matched
        if opt_matching[proposer] == "None":
            for i in set_receivers:
                # We find the most relevant receiver in the partial order preferences list of the proposer
                receiver_index = partial_orders.choose_receiver(positive_dic[proposer])
                positive_dic[proposer][receiver_index] = -1
                receiver = set_receivers[receiver_index]

                # If the receiver is already matched with another agent
                if (any(receiver in receivers_matching for receivers_matching in opt_matching.values())):
                    receiver_prefs_matrix = receivers_partial_prefs[receiver]
                    for proposer_matching, receiver_matching in opt_matching.items():
                        if receiver_matching == receiver:
                            proposer_matching = proposer_matching
                            proposer_matching_index = set_proposers.index(proposer_matching)
                            break

                    # Comparison of the proposer with the matched agent w.r.t the receiver's preferences
                    if receiver_prefs_matrix[proposer_index, proposer_matching_index] == 1:
                        opt_matching[proposer] = receiver
                        opt_matching[proposer_matching] = "None"
                        break

                # If the receiver is not yet matched
                else:
                    opt_matching[proposer] = receiver
                    break

        # If after the iterations, there is still no stable matching found
        if opt_matching[proposer] == "None":
            not_found = 1

    return opt_matching, not_found


def adaptation_gale_shapley_all_partial(proposers_partial_prefs, receivers_partial_prefs):
    # Definition of the optimal stable matching
    all_proposers = list(proposers_partial_prefs.keys())
    all_receivers = list(receivers_partial_prefs.keys())
    proposer_opt = {proposer : "None" for proposer in all_proposers}
    positive_dic = {proposer: "None" for proposer in all_proposers}

    # While there is a proposer with no acceptance of receivers
    while any("None" in prefs_list for prefs_list in proposer_opt.values()):
        proposer_opt, not_found = adaptation_gale_shapley_all_partial_loop(proposers_partial_prefs,
                                                     receivers_partial_prefs,
                                                     all_proposers,
                                                     all_receivers,
                                                     positive_dic,
                                                     proposer_opt)

        # If a proposer is rejected by all the receivers, quit the loop
        if not_found == 1:
            print("A matching could not be found")
            break

    # Stability check
    stability = check_stability(proposer_opt,all_proposers,all_receivers,proposers_partial_prefs,receivers_partial_prefs)
    if stability == 0:
        print(f" Optimal stable matching found: {proposer_opt}")
        print(f" This matching is stable.\n")
    else:
        print(f" Stable matching found: {proposer_opt}")
        print(f" This matching is NOT stable.\n")
    return proposer_opt

def check_stability(matching, all_proposers, all_receivers, proposers_prefs, receivers_prefs):
    stability = 0
    for i, proposer in enumerate(all_proposers):
        proposer_prefs = proposers_prefs[proposer]
        matching_receiver_index = all_receivers.index(matching[proposer])
        for j, receiver in enumerate(all_receivers):
            if j != matching_receiver_index:
                if proposer_prefs[j, matching_receiver_index] == 1:
                    receiver_prefs = receivers_prefs[receiver]
                    matching_proposer_index = all_proposers.index(get_key_from_value(matching,receiver))
                    if receiver_prefs[i, matching_proposer_index] == 1:
                        stability = 1
    return stability

def get_key_from_value(dic, value):
    for key, val in dic.items():
        if val == value:
            return key
    return "None"

