"""
This module solves skyscrapers puzzle, checks if
given game board is right and all rules are abided.
"""
from typing import List

def read_input(path: str) -> List[str]:
    """
    Reads game board file from path.
    Returns list of str.
    >>> read_input("skyscrapers_state.txt")
    ['***21**', '4?????*', '4?????*', '*?????5', \
'*?????*', '*?????*', '*2*1***']
    """
    with open(path) as file:
        field = file.readlines()
        list_of_rows = [row[:-1] if '\n' in row
            else row for row in field]
    return list_of_rows
# print(read_input('skyscrapers_state.txt'))

def left_to_right_check(input_line: str, pivot: int) -> bool:
    """
    Checks row-wise visibility from left to right.
    Returns True if number of building from the left-most hint
    is visible looking to the right, False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line. 

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    input_line = input_line[1:-1]
    list_of_numbers = [int(number) for number in input_line]
    visible_buildings_number = 1
    index_control = 1
    while index_control < 5:
        smaller_numbers = 0
        for number in list_of_numbers[0:index_control]:
            if number < list_of_numbers[index_control]:
                smaller_numbers += 1
        if smaller_numbers == len(list_of_numbers[0:index_control]):
            visible_buildings_number += 1
        index_control += 1
    return visible_buildings_number == pivot
 
print(left_to_right_check("132345*", 3))

# print(left_to_right_check("412345*", 5))

def check_not_finished_board(board: list) -> bool:
    """
    Check if skyscraper board is not finished, i.e.,
    '?' present on the game board.
    Returns True if finished, False otherwise.
    >>> check_not_finished_board(['***21**', '4?????*', \
'4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', \
'423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', \
'423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for row in board:
        if row.find('?') != -1:
            return False
        else:
            continue
    return True

# print(check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***']))

def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique
    length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', \
'423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', \
'423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', \
'423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for row in board:
        row = row[1:-1].split('*')
        number_list = []
        for index in range(len(row)):
            if row[index] in number_list:
                return False
            elif row[index] == '':
                continue
            else:
                number_list.append(row[index])
    return True

# print(check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***']))

def check_horizontal_visibility(board: List[str]):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
    i.e., for line 412453* , hint is 4, and 1245 are the
    four buildings that could be observed from the hint
    looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', \
'423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', \
'423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', \
'423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    new_board = []
    for row in board:
        if row[0] != '*':
            new_board.append(row)
    for number in new_board:
        visible_num = int(number[0])
        number_list = []
        visible_buildings_number = 0
        number = number[1:]
        for index in range(len(number)):
            if all(i < number[index] for i in number_list):
                number_list.append(number[index])
                visible_buildings_number += 1
        if visible_buildings_number != visible_num:
            return False
    return True
# print(check_horizontal_visibility((['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])))

def check_columns(board: list):
    """
    Checks column-wise compliance of the board for uniqueness
    (buildings of unique height) and visibility (top-bottom
    and vice versa).
    Same as for horizontal cases, but aggregated in one
    function for vertical case, i.e. columns.
    >>> check_columns(['***21**', '412453*', '423145*', \
'*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', \
'*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', \
'*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    below_nums = board[0]  #works with regular list
    below_list = [number for number in below_nums
                        if number != '*']
    below_index_list = [below_nums.find(number)
                        for number in below_list]
    rows_list = []
    for index in below_index_list:
        new_row = str(below_nums[index])
        for row in board[1:-1]:
            new_row += row[index]
        rows_list.append(new_row)
    down_nums = board[-1]   #works with reversed list
    down_list = [number for number in down_nums
                        if number != '*']
    down_index_list = [down_nums.find(number)
                        for number in down_list]
    rowss_list = []
    for index in down_index_list:
        new_row = str(down_nums[index])
        for row in reversed(board[1:-1]):
            new_row += row[index]
        rowss_list.append(new_row)
    rows_list.extend(rowss_list)
    return check_horizontal_visibility(rows_list)
    # print(rowss_list)

    #need to form numbers strings and then use horisontal check
    #make one more function for not rewriting same things for
    #below and down numbers

# print(check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***']))

def check_skyscrapers(input_path: str) -> bool:
    """
    Main function to check the status of skyscraper game board.
    Returns True if the board status is compliant with the rules,
    False otherwise.
    >>> check_skyscrapers("check.txt")
    True
    """
    board = read_input(input_path)
    if check_not_finished_board(board):
        if check_uniqueness_in_rows(board):
            if check_horizontal_visibility(board) and check_columns(board):
                return True
    return False
    