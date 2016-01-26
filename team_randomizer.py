"""Module for shuffling teams when no one wants to present"""

import random
import math
import sys

def random_teams(team_dictionary, number_members='max'):
    """
    Runs shuffler and prints both teams and selected people (or max if number_members > members)

    Inputs:
        team_dictionary (dictionary of string arrays):
            dictionary of teams as keys and team members in string arrays
        number_members (int): number of members to be selected. Use 0 if only team shuffle desired
    """
    # shuffle teams
    shuffled_teams = random.sample(team_dictionary.keys(), len(team_dictionary.keys()))

    # check if members are to be shuffled. if so, shuffle and print teams + members; else teams only
    if number_members == 0:
        print_team_list(shuffled_teams)
    else:
        # shuffle members in team
        shuffled_team_dictionary = {}
        for i in team_dictionary:
            current_team_size = len(team_dictionary[i])
            if number_members == 'max':
                shuffled_team_dictionary[i] = random.sample(team_dictionary[i], current_team_size)
            else:
                if number_members > current_team_size:
                    shuffled_team_dictionary[i] = random.sample(team_dictionary[i],
                                                                current_team_size)
                else:
                    shuffled_team_dictionary[i] = random.sample(team_dictionary[i], number_members)

        # print pretty
        print_team_member_list(shuffled_team_dictionary, shuffled_teams)

def print_team_list(team_ordering):
    """
    Pretty prints list of strings as item stack

    Inputs:
        team_ordering (list of strings): list of team names as strings to print
    """
    # get max length of team name
    team_name_lengths = {key: len(key) for key in team_ordering}
    max_team_name_length = max(team_name_lengths.values()) + 2 # add 2 for | on either side

    # first line of - (add 2 for one additional space before/after content)
    print '-' * (max_team_name_length + 2)

    # content
    for i in team_ordering:
        current_team_length = team_name_lengths[i]
        padding = (max_team_name_length - current_team_length) / 2.0

        # create front padding
        pad_front = '|' + (' ' * int(math.floor(padding)))

        # create back padding
        pad_back = (' ' * int(math.ceil(padding))) + '|'

        # print content
        print pad_front + i + pad_back

        # print separating - (add 2 for one additional space before/after content)
        print '-' * (max_team_name_length + 2)

def print_team_member_list(team_dictionary, ordering):
    """
    Pretty prints list of strings as item stack

    Inputs:
        team_dictionary (dict of strings): dict of team names with shuffled team members
        ordering (list of strings): list of team names as strings to print in order
    """
    # create team strings
    team_strings = []
    for i in ordering:
        team_strings.append(i + ": " + ' --> '.join(team_dictionary[i]))

    # get max length of team string
    team_string_lengths = {key: len(key) for key in team_strings}
    max_team_string_length = max(team_string_lengths.values())

    # create total line length (take max length and add 2 for | on either side)
    total_line_length = max_team_string_length + 2

    # first line of - (add 2 for one additional space before/after content)
    print '-' * (total_line_length + 2)

    # print content
    for i in team_strings:
        padding = (total_line_length - team_string_lengths[i]) / 2.0

        # create front padding
        pad_front = '|' + (' ' * int(math.floor(padding)))

        # create back padding
        pad_back = (' ' * int(math.ceil(padding))) + '|'

        # print content
        print pad_front + i + pad_back

        # print separating - (add 2 for one additional space before/after content)
        print '-' * (total_line_length + 2)

if __name__ == '__main__':
    teams = {
        'BAIY Watch': ['Allison', 'Bodhisattva', 'Isabel', 'Yoko'],
        'Body + Soul': ['Armaan', 'Eduardo', 'Nadia', 'Philip'],
        'HCI Xiaozu': ['Jiawen', 'Jingming', 'Yang', 'Yuling'],
        'Saturn': ['Fei', 'Qian', 'Shiqi', 'Xiaofei'],
        'The Ballers': ['Joseph', 'Pawel', 'Xu', 'Yimin']
    }
    try:
        random_teams(teams, int(sys.argv[1]))
    except IndexError:
        random_teams(teams)
    except ValueError:
        print "Error: argument must be an integer"
