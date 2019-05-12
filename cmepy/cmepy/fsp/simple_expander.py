"""
A simple domain expansion routine for the FSP algorithm.
"""
import operator
import cmepy.fsp.util
import cmepy.fsp.trun

class SimpleExpander(object):
    """
    Simple FSP expander that expands the entire domain.

    The domain is expanded along the given transitions, up to the specified
    depth.
    """
    def __init__(self, propensities, transitions, depth):
        """
        Simple FSP expander that expands the entire domain.

        The domain is expanded along the given transitions, up to the specified
        depth.
        """
        self.propensities = propensities
        self.transitions = transitions
        self.depth = depth
        self.no_of_reactions = len(self.propensities)
        self.percent_prop = 30.00

    def expand(self, **kwargs):
        no_of_reactions = self.no_of_reactions
        propensities = self.propensities
        #Oldlength = len(propensities)


        #this converts original transitions tuples to list of array
        transitions_list = list(self.transitions)
        propensities_list = list(self.propensities)

        #this sort the propensities in descending order but doesn't change the order of the propensities,
        #instead gives the index of the propensities from max to min - 0...to...n and gives output of
        #index array in the form [4,2,0,1,3] for 5 propensities
        #start
        mapping = {k: i for i, k in enumerate(sorted(propensities, reverse=True))}
        new_index = ([mapping[i] for i in propensities])
        #end

        #this shuffles the original transitions based on max to min propensities values of the reactions
        #start
        for i in xrange(0,no_of_reactions):
            while (new_index[i] != i):
                oldTargetI = new_index[new_index[i]]
                oldTargetE = transitions_list[new_index[i]]
                transitions_list[new_index[i]] = (transitions_list[i])
                new_index[new_index[i]] = (new_index[i])
                new_index[i] = oldTargetI
                transitions_list[i] = oldTargetE
        newarray = []
        for i in xrange(0, no_of_reactions):
            newarray.append(transitions_list[i])
        #print newarray
        newindex = []
        for i in xrange(0, no_of_reactions):
            newindex.append(new_index[i])
        #print newindex
        #end
        truncated_new_transitions = cmepy.fsp.trun.ignorereaction(
            propensities_list,
            newarray,
            self.percent_prop
        )
        #this sends the truncated new transitions to expander
        #start
        expanded_states = cmepy.fsp.util.grow_domain(
            kwargs['domain_states'],
            truncated_new_transitions,
            self.depth
        )
        #end
        return expanded_states

"""
    def expand(self, **kwargs):

        Returns expanded domain states

        transitions_list = list(self.transitions)
        newarray = cmepy.fsp.util.reorder(
            self.propensities,
            transitions_list,
            self.no_of_reactions
        )
        expanded_states = cmepy.fsp.util.grow_domain(
            kwargs['domain_states'],
            newarray,
            self.depth
        )
        return expanded_states
"""


"""
        #this removes the re-arranged transitions given by above function
        #start
        max_propensity = max(propensities)
        for i in propensities:
            if i < (max_propensity * percent):
                propensities.remove(i)
            Newlength = len(propensities)
        k = Oldlength - Newlength
        truncated_new_transitions = newarray[: len(newarray) - k]
        #end
"""

"""
        newtx = cmepy.fsp.util.ignorereaction(
            propensities,
            newarray,
            percent
        )
"""