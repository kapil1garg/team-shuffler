"""Module for shuffling teams when no one wants to present"""

import random
import math

def random_teams(team_dictionary, number_members='max'):
    """
    Runs shuffler and prints both teams and selected people (or max if number_members > members)

    Inputs:
        team_dictionary (dictionary of string arrays):
            dictionary of teams as keys and team members in string arrays
        number_members (int): number of members to be selected. Use 0 if only team shuffle desired
    """
    # count number of members for each team
    number_members_per_team = team_dictionary.copy()
    for i in number_members_per_team:
        number_members_per_team[i] = len(number_members_per_team[i])

    # shuffle members in team
    shuffled_team_dictionary = team_dictionary
    if number_members == 'max':
        for i in shuffled_team_dictionary:
            shuffled_team_dictionary[i] = random.sample(shuffled_team_dictionary[i],
                                                        number_members_per_team[i])
    elif number_members == 0:
        shuffled_teams = random.sample(team_dictionary.keys(), len(team_dictionary.keys()))
        print_team_list(shuffled_teams)
        return
    else:
        for i in shuffled_team_dictionary:
            current_number_members = number_members_per_team[i] if \
                number_members_per_team[i] < number_members else number_members
            shuffled_team_dictionary[i] = random.sample(shuffled_team_dictionary[i],
                                                        current_number_members)

    # shuffle teams
    shuffled_teams = random.sample(team_dictionary.keys(), len(team_dictionary.keys()))

    # print all pretty
    print_team_member_list(shuffled_team_dictionary, shuffled_teams)


def print_team_list(team_ordering):
    """
    Pretty prints list of strings as item stack

    Inputs:
        team_ordering (list of strings): list of team names as strings to print
    """
    # get max length of team name
    max_teamname_length = max([len(i) for i in team_ordering]) + 2

    # first line of -
    print '-' * (max_teamname_length + 2)

    # content
    for i in xrange(len(team_ordering)):
        current_team_length = len(team_ordering[i])
        padding = (max_teamname_length - current_team_length) / 2.0

        # pad front of string
        print '|' + (' ' * int(math.floor(padding) - 1)),

        # print team
        print team_ordering[i],

        # pad end of string
        print (" " * int(math.ceil(padding) - 1)) + '|'

        # print separating -
        print '-' * (max_teamname_length + 2)

def print_team_member_list(team_dictionary, ordering):
    """
    Pretty prints list of strings as item stack

    Inputs:
        team_dictionary (dict of strings): dict of team names with shuffled team members
        ordering (list of strings): list of team names as strings to print in order
    """
    # get max length of team name
    max_teamname_length = max([len(i) for i in ordering]) + 2

    # get max number of members picked
    max_members_picked = max([len(team_dictionary[x]) for x in team_dictionary])

    # get max length of member listing
    max_member_listing_length = 0
    for i in team_dictionary:
        max_member_listing_length = max(max_member_listing_length,
                                        reduce(lambda x, y: x + y,
                                               [len(x) for x in team_dictionary[i]]) +
                                        (len(team_dictionary[i]) - 1) * 5)

    # get total line length
    total_line_length = max_teamname_length + max_member_listing_length

    # first line of -
    print '-' * (total_line_length + 4)

    # content
    for i in ordering:
        current_team_length = len(i)
        current_member_selected_length = len(' --> '.join(team_dictionary[i]))

        padding = (total_line_length - current_team_length - current_member_selected_length) / 2.0

        # pad front of string
        print '|' + (' ' * int(math.floor(padding) - 1)),

        # print team
        print i + ':',

        # print selected members, if any
        print ' --> '.join(team_dictionary[i]),

        # pad end of string
        print (" " * int(math.ceil(padding) - 1)) + '|'

        # print separating -
        print '-' * (total_line_length + 4)

if __name__ == '__main__':
    # teams = {
    #     'BAIY Watch': ['Allison', 'Bodhisattva', 'Isabel', 'Yoko'],
    #     'Body + Soul': ['Armaan', 'Eduardo', 'Nadia', 'Philip'],
    #     'HCI Xiaozu': ['Jiawen', 'Jingming', 'Yang', 'Yuling'],
    #     'Saturn': ['Fei', 'Qian', 'Shiqi', 'Xiaofei'],
    #     'The Ballers': ['Joseph', 'Pawel', 'Xu', 'Yimin']
    # }
    #

    teams = {
        'BAIY Watch': ['Allison', 'Yoko'],
        'Body + Soul': ['Armaan', 'Eduardo', 'Nadia', 'Philip'],
        'HCI Xiaozu': ['Jiawen', 'Yang', 'Yuling'],
        'Saturn': ['Fei', 'Qian', 'Shiqi', 'Xiaofei'],
        'The Ballers': ['Joseph']
    }

    random_teams(teams, 3)
