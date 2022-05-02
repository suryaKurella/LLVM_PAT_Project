import csv

from PAT.midrunner import tests_dict_returner
from PAT.pdriller_plots import top_5_test_commits_author_plot
from utils import unit_test_files_returner, \
    regression_test_files_returner, unit_case_results, regression_case_results, \
    assert_count_returner_folder_wise, subfolder_name_non_abs, common_pie

import os
import matplotlib.pyplot as plt


def unit_regression_file_paths_returner():
    return unit_test_files_returner(), regression_test_files_returner()


def unit_regression_tests_file_count_plot():
    unit_cases_files, regression_cases_files = unit_regression_file_paths_returner()

    labels = ['Unit Test Files', 'Regression Test Files']

    plt.bar(range(len(labels)), [len(unit_cases_files), len(regression_cases_files)], tick_label=labels)
    plt.xlabel("Test case Files")
    plt.ylabel("Number of Test case Files")
    plt.title("Unit vs Regression Test File Count")
    plt.savefig(f'Plots{os.path.sep}test_files_unit_regression.png')

    # print('regression test', len(regression_cases_files))


def plot_bar_graphs(target_data):
    plt.bar(range(len(target_data)), target_data.values(), tick_label=target_data.keys())
    plt.show()


def dict_summer(dict_):
    dict_sum = 0
    for key, value in dict_.items():
        dict_sum = dict_sum + value[0]
    return dict_sum


def unit_regression_asserts_plot():
    unittest_assert_dict, regression_assert_dict = tests_dict_returner()
    labels = ['Unit Test Asserts', 'Regression Test Asserts']

    unittest_assert_sum = dict_summer(unittest_assert_dict)
    regression_assert_sum = dict_summer(regression_assert_dict)

    plt.bar(range(len(labels)), [unittest_assert_sum, regression_assert_sum], tick_label=labels)
    plt.xlabel("Unit and Regression Folders")
    plt.ylabel("Number of Assert statements")
    plt.title("Unit vs Regression Assert Statement Count")
    plt.savefig(f'Plots{os.path.sep}assert_count_unit_regression.png')


def pass_fail_common_func(cases, type):
    labels = ['Passed', 'Failed', 'Unsupported', 'Skipped']
    fig, ax = plt.subplots()
    ax.barh(range(len(cases)), cases, tick_label=labels)

    plt.ylabel("Test case Status")
    plt.title(f"{type} Test cases Pass Fail Counts ")
    for i, v in enumerate(cases):
        ax.text(v + 1, i + .15, str(v),
                color='black', fontweight='bold')

    plt.savefig(f'Plots{os.path.sep}{type}_test_pass_fail.png')


def pass_fail_unitest_plot():
    cases = unit_case_results()
    pass_fail_common_func(cases, 'Unit')


def pass_fail_regressiontest_plot():
    cases = regression_case_results()
    pass_fail_common_func(cases, 'Regression')


def pie_plot_unit():
    unit_tests_for_pie, reg_tests_for_pie = assert_count_returner_folder_wise()

    unit_labels = subfolder_name_non_abs("../unittests", 'test')
    regression_labels = subfolder_name_non_abs("../test", 'test')

    bb = 0
    kk = 0
    for i in range(len(regression_labels)):
        if regression_labels[i] in 'CodeGen':
            bb = i
    for i in range(len(unit_labels)):
        if regression_labels[i] in 'ADT':
            bb = i

    unit_explode_list = len(unit_labels) * [0]
    regression_explode_list = len(regression_labels) * [0]
    unit_explode_list[kk] = 0.2
    regression_explode_list[bb] = 0.2
    print(unit_explode_list)

    #
    common_pie(unit_tests_for_pie, unit_labels, 'unittests', unit_explode_list)
    common_pie(reg_tests_for_pie, regression_labels, 'regression', regression_explode_list)


def yearly_files_plot():
    intermediate = {}

    with open('Files/yearly_files_added.csv', mode='r') as inp:
        reader = csv.reader(inp)
        dict_from_csv = {rows[0]: rows[1] for rows in reader}

    for key, value in dict_from_csv.items():
        if 'Year' not in key:
            intermediate[key] = int(value)
    print(intermediate)

    plt.plot(intermediate.keys(), intermediate.values())
    plt.title('Year Wise Test files generation')
    plt.xlabel('Years')
    plt.xticks(rotation=90)
    plt.ylabel('Number Of Files Added')
    plt.savefig(f'Plots{os.path.sep}_yearly_file_add.png')


def local_runner():
    unit_regression_tests_file_count_plot()
    unit_regression_asserts_plot()
    pass_fail_unitest_plot()
    pass_fail_regressiontest_plot()
    pie_plot_unit()
    top_5_test_commits_author_plot()
    yearly_files_plot()


local_runner()
