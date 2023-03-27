"""Define a dict that represents the children and grandchildren in a family.
(See figure 7.1 for a graphic representation.) Each key will be a child’s
name, and each value will be a list of strings representing their children
(i.e., the family’s grandchildren). Thus the dict {'A':['B', 'C', 'D'],
'E':['F', 'G']} means that A and E are siblings; A’s children are B, C, and D;
and E’s children are F and G. Use a list comprehension to create a list of the
grandchildren’s names."""


def gchildren_name(children):
    return [one_child for child in children.values() for one_child in child]


"""Solution to chapter 7, exercise 29, beyond 2: grandchildren_names"""


def grandchildren_names(d):
    return [one_grandchild
            for grandchild_list in d.values()
            for one_grandchild in grandchild_list]


children_gchildren = {
        'alex': ['rafael'],
        'eli': ['felipe'],
        'rick': ['lucas', 'daniel']}

print(gchildren_name(children_gchildren))
print(grandchildren_names(children_gchildren))
