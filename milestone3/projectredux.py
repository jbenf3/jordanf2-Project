import numpy as np

def main():
    print_welcome()
    match_type = choose_match_type()
    player_1 = input("Enter player 1 name: ")
    player_2 = input("Enter player 2 name: ")
    if (match_type == 1):
        match_type_1()
    if (match_type == 2):
        match_type_2()
    if (match_type == 3):
        match_type_3()
    if (match_type == 4):
        match_type_4()
    if (match_type == 5):
        match_type_5()

def print_welcome():
    print "Tennis Match"


def choose_match_type():
    print "Match type options:"
    print "  1) 2 out of 3 sets"
    print "  2) 3 out of 5 sets"
    print "  3) 10 game pro set"
    print "  4) 8 game pro set"
    print "  5) 6 game pro set"
    match_type = input("Please choose a match type: ")
    return match_type

def choose_scoring():
    print "Scoring options:"
    print "1) ad"
    print "2) no-ad"
    score_type = input("Please choose a scoring style: ")
    return score_type

def match_type_1():
    scoring = choose_scoring()
    if (scoring == 1):
        # play two out of three set match with ad scoring
    else:
        # play two out of three set match with no-ad scoring

def match_type_2():
    scoring = choose_scoring()
    if (scoring == 1):
        # play three out of five set match with ad scoring
    else:
        # play three out of five set match  with no ad scoring

def match_type_3():
    scoring = choose_scoring()
    if (scoring == 1):
        # play ten game pro set with ad scoring
    else:
        # play ten game pro set with no-ad scoring

def match_type_4():
    scoring = choose_scoring()
    if (scoring == 1):
        # play eight game pro set with ad scoring
    else:
        # play eight game pro set with no-ad scoring

def match_type_5():
    scoring = choose_scoring()
    if (scoring == 1);
        # play six game pro set with ad scoring
    else:
        # play six game pro set with no-ad scoring

# throughout the program, keep track of statistics in the following
# variables:
# 1) first_serve_percentage
# 2) second_serve_percentage
# 3) unforced_errors
# 4) winners
# 5) points_won (each player)


# at the end of the program, the user will be asked if he or she wants a
# visual display of the data that has been collected throughout the
# duration of the program

# the visual information will be shown in the form of graphs of various
# types made with numpy and scipy
