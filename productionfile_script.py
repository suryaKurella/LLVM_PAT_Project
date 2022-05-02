import os
import pathlib
import re
import config
from utils import generic_count_returner_with_line_numbers, file_name_with_path_returner_


def production_assert_debug_dict():
    assert_statements = [config.ASSERT_STATEMENT_REGEX]
    debug_statements = [config.DEBUG_STATEMENTS_REGEX]
    filers = file_name_with_path_returner_(f'{os.path.normpath(os.getcwd() + os.sep + os.pardir)}')

    assert_prod_files = generic_count_returner_with_line_numbers(filers, assert_statements, 'assert')
    debug_prod_files = generic_count_returner_with_line_numbers(filers, debug_statements, 'debug')

    print(len(assert_prod_files))
    print(len(debug_prod_files))

    for key, value in assert_prod_files.items():
        print(f'key = {key}')
        if key in debug_prod_files:
            print("So found it ")
            assert_prod_files[key].append(debug_prod_files[key])
        else:
            print("Key not found dude")

    return assert_prod_files
# print(assert_prod_files)

# print(debug_prod_files)
