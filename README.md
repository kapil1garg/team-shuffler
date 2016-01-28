# Team Shuffler
A simple team/member shuffler for when no one wants to volunteer...

## Usage
1. In, `team_randomizer.py`, edit the `teams` dictionary at the end of the script to hold your teams and the members. Format should be:

   ```
   teams = {
      'team_a': ['member_a1', 'member_a2'],
      'team_b': ['member_b1'],
      'team_c': ['member_c1', 'member_c2', 'member_c3']
    }
   ```
2. From command line, run `python team_randomizer.py number_of_members` where `number_of_members` is the number (as integer) of members to be randomly selected for each team. 
