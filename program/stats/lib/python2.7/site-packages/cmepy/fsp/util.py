"""
Common utility routines for Finite State Projection.
"""
import operator
import numpy
from cmepy.cme_matrix import non_neg_states
from cmepy import lexarrayset




def maxproppercent(propensities, percent_prop):
    maxVal = propensities[0]
    for i in range(0, len(propensities), 1):
        if maxVal < propensities[i]:
            maxVal = propensities[i]
    percent_propen = float(percent_prop)
    max_propensity_val = operator.mul(maxVal, percent_propen)
    return max_propensity_val

def ignorereaction(propensities, newarray):
    Oldlength = len(propensities)
    #max_propensity = maxproppercent(propensities, percent_prop)
    for i in propensities:
        if i < 20.03:
            propensities.remove(i)
    Newlength = len(propensities)
    k = Oldlength - Newlength
    truncated_new_transitions = newarray[: len(newarray) - k]
    return truncated_new_transitions

def grow_domain(domain_states, transitions, depth, validity_test = None):
    """
    Returns domain_states grown by depth along transitions.

    Resulting states are filtered by the validity_test. By default,
    only states without a negative coordinate are valid.
    """
    if numpy.size(domain_states) == 0:
        raise ValueError('there must be at least one state to expand')

    if validity_test is None:
        validity_test = non_neg_states

    expanded_states = domain_states
    for _ in xrange(depth):
        # expand support states by one along each state transition
        for transition in transitions:
            level_states = domain_states
            # expand support states by transition upto bound limit
            for _ in xrange(3):
                new_level_states = lexarrayset.shift(level_states, transition)
                valid = validity_test(new_level_states)
                new_level_states = new_level_states[:, valid]
                expanded_states = lexarrayset.union(
                expanded_states,
                new_level_states
                )
            level_states = expanded_states
        domain_states = level_states
    return expanded_states
"""
def ignorereaction(propensities, newarray, percent):
    max_propensity = max(propensities)
    Oldlength = len(propensities)
    for i in propensities:
        if i < (max_propensity * percent):
            propensities.remove(i)
    Newlength = len(propensities)
    k = Oldlength - Newlength
    truncated_new_transitions = newarray[: len(newarray) - k]
    return truncated_new_transitions
"""
"""
def reorder(propensities, transitions, no_of_reactions):
    mapping = {k: i for i, k in enumerate(sorted(propensities, reverse=True))}
    new_index = ([mapping[i] for i in propensities])
    for i in xrange(0,no_of_reactions):
        while (new_index[i] != i):
            oldTargetI = new_index[new_index[i]]
            oldTargetE = transitions[new_index[i]]
            transitions[new_index[i]] = (transitions[i])
            new_index[new_index[i]] = (new_index[i])
            new_index[i] = oldTargetI
            transitions[i] = oldTargetE
    newarray = []
    for i in xrange(0, no_of_reactions):
        newarray.append(transitions[i])
    #print newarray
    newindex = []
    for i in xrange(0, no_of_reactions):
        newindex.append(new_index[i])
    #print newindex
    return newarray
"""

"""
def maxpropval(propensities):
    maxVal = propensities[0]
    for i in range(0, len(propensities), 1):
        if maxVal < propensities[i]:
            maxVal = propensities[i]
    return maxVal

def maxproppercent(propensities, percent_prop):
    max_val = maxpropval(propensities)
    percent_propen = int(percent_prop)
    max_propensity = operator.__mul__(max_val, percent_propen)
    return max_propensity

def ignorereaction(propensities, newarray, percent_prop):
    Oldlength = len(propensities)
    max_propensity = maxproppercent(propensities, percent_prop)
    for i in propensities:
        if i < (max_propensity):
            propensities.remove(i)
    Newlength = len(propensities)
    k = Oldlength - Newlength
    truncated_new_transitions = newarray[: len(newarray) - k]
    return truncated_new_transitions
"""