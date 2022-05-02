import os

import config
from authors_py_drill import authors_commits_driller
from csv_writers import assert_writer, assert_debug_writer, author_commit_writer
from utils import file_name_with_path_returner, \
    generic_count_returner_with_line_numbers, merge_dict, file_name_with_path_returner_, unit_test_files_returner, \
    regression_test_files_returner
from productionfile_script import production_assert_debug_dict


def tests_dict_returner():

    unitTestFiles = unit_test_files_returner()
    regressionTestFiles = regression_test_files_returner()
    assert_statements = [config.ASSERT_STATEMENT_REGEX]

    unit_test_asserts_dict = \
        generic_count_returner_with_line_numbers(unitTestFiles, assert_statements, 'assert')
    regression_test_asserts_dict = \
        generic_count_returner_with_line_numbers(regressionTestFiles, assert_statements,
                                                 'assert')

    return unit_test_asserts_dict, regression_test_asserts_dict


def merged_dict_returner(tests_dict_returner):
    merge_dict(tests_dict_returner[0], tests_dict_returner[1])
    return tests_dict_returner[1]


def assert_count_test_returner():
    tupled_data = tests_dict_returner()
    return merged_dict_returner(tupled_data)
