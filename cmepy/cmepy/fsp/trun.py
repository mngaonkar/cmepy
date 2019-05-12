import numpy as np
import operator
import cmepy.recorder
import cmepy.fsp.solver
import cmepy.fsp.simple_expander
import cmepy.domain
import cmepy.statistics

# From this function I am finding and returning the maximum element/value present inside propensities set.
def maxpropval(propensities):
    maxVal = propensities[0]
    for i in range(0, len(propensities), 1):
        if maxVal < propensities[i]:
            maxVal = propensities[i]
    return maxVal

# From this function I am multiplying the maximum element/value present inside propensities set with the value percent_prop (can be of type 32.5 or 30.00).
def maxproppercent(propensities, percent_prop):
    max_val = maxpropval(propensities)
    max_propen = operator.mul(max_val, percent_prop)
    max_propensity = (max_propen / 100)  # dividing value by 100
    return max_propensity

# From this function I am removing all the values from propensities set which is less than max_propensity and then calculating (k) the how many elements/values
# are removed from propensities and then remove same number of elements from last from newarray and then returning the newarray from this function
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
def maxpropval2(propensities,percent_prop):
    maxVal = propensities[0]
    for i in range(0, len(propensities), 1):
        if maxVal < propensities[i]:
            maxVal = propensities[i]
    max_val = float(maxVal)
    percent_propen = float(percent_prop)
    max_propensity = operator.mul(max_val, percent_propen)
    return max_propensity

def ignorereactionnew(propensities, newarrayy, percent_prop):
    Oldlength = len(propensities)
    maxVal = propensities[0]
    for i in range(0, len(propensities), 1):
        if maxVal < propensities[i]:
            maxVal = propensities[i]
    max_val = maxVal
    max_val = max_val
    percent_propen = percent_prop
    max_propensity = np.multiply(max_val, percent_propen)
    for i in propensities:
        if i < (max_propensity / 100):
            propensities.remove(i)
    Newlength = len(propensities)
    k = Oldlength - Newlength
    truncated_new_transitions = newarrayy[: len(newarrayy) - k]
    return truncated_new_transitions

def ignorereactionnew2(propensities, newarrayy, percent_prop):
    propensities_list = list(propensities)
    Oldlength = len(propensities_list)
    max_val = float(max(propensities_list))
    percent_propen = float(percent_prop)
    max_propensity = operator.mul(max_val, percent_propen)
    for i in propensities:
        if i < (max_propensity / 100):
            propensities_list.remove(i)
    Newlength = len(propensities_list)
    k = Oldlength - Newlength
    truncated_new_transitions = newarrayy[: len(newarrayy) - k]
    return truncated_new_transitions


def ignorereactionnew3(propensities, newarray, percent_prop):
    Oldlength = len(propensities)
    max_val = sorted(propensities, reverse=True)[:1]
    max_vall = float(max_val)
    percent_propen = float(percent_prop)
    max_propensity = operator.mul(max_vall, percent_propen)
    for i in propensities:
        if i < (max_propensity / 100):
            propensities.remove(i)
    Newlength = len(propensities)
    k = Oldlength - Newlength
    truncated_new_transitions = newarray[: len(newarray) - k]
    return truncated_new_transitions
"""