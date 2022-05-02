import os
import pathlib
import re

from matplotlib import pyplot as plt

import config


def file_name_with_path_returner(root_dir, extension):
    filelist = []

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_extension = pathlib.Path(file).suffix
            if file_extension in extension:
                filelist.append(os.path.join(root, file))
    return filelist


def file_name_with_path_returner_(root_dir):
    filelist = []
    for root, dirs, files in os.walk(root_dir):
        if not re.search(config.IGNORE_FOLDERS, root):
            for file in files:
                file_extension = pathlib.Path(file).suffix
                if file_extension not in config.IGNORE_EXTENSIONS:
                    filelist.append(os.path.join(root, file))
    return filelist


def generic_count_returner(file, line, line_number, reg, filename_with_expect_and_assert_count):
    # print("reg is ", reg)
    count = len(reg.findall(line))
    # print(line)
    # print(f'count is {count}')
    if count > 0:
        if filename_with_expect_and_assert_count.__contains__(file):
            filename_with_expect_and_assert_count[file][0] += 1
            filename_with_expect_and_assert_count[file][1].append(line_number + 1)
        else:
            filename_with_expect_and_assert_count[file] = [1, [line_number + 1]]

    return filename_with_expect_and_assert_count


def generic_count_returner_with_line_numbers(files, testStatements, param=''):
    print(f"param is {param}")
    filename_with_expect_and_assert_count = {}
    reg = re.compile(r' | '.join(testStatements), flags=re.I | re.X)
    for file in files:
        print(file)
        current_file = open(file, 'r', encoding='utf8', errors="ignore")
        for line_number, line in enumerate(current_file):
            if not (re.search(config.COMMENTS_REGEX, line)):
                if param == 'assert':
                    if not re.search(config.ASSERT_STATEMENTS_COMMENTS_REGEX, line, flags=re.I | re.X):
                        filename_with_expect_and_assert_count = generic_count_returner(file, line, line_number, reg,
                                                                                       filename_with_expect_and_assert_count)

                elif param == 'debug':
                    if not re.search(
                            config.DEBUG_STATEMENTS_COMMENTS_REGEX, line, flags=re.I | re.X):
                        filename_with_expect_and_assert_count = generic_count_returner(file, line, line_number, reg,
                                                                                       filename_with_expect_and_assert_count)

        if param == 'assert':
            if file not in filename_with_expect_and_assert_count:
                filename_with_expect_and_assert_count[file] = [0, [0]]
        elif param == 'debug':
            if file not in filename_with_expect_and_assert_count:
                filename_with_expect_and_assert_count[file] = [0, [0]]

        current_file.close()

    return filename_with_expect_and_assert_count


def folder_files_count(folder_path):
    return len(file_name_with_path_returner_(folder_path))


# Python code to merge dict using update() method
def merge_dict(dict1, dict2):
    return dict2.update(dict1)


def unit_test_files_returner():
    unittests_path = f"{os.path.normpath(os.getcwd() + os.sep + os.pardir)}{os.path.sep}unittests"
    return file_name_with_path_returner(unittests_path, '.cpp')


def regression_test_files_returner():
    regression_tests_path = f"{os.path.normpath(os.getcwd() + os.sep + os.pardir)}{os.path.sep}test"
    return file_name_with_path_returner(regression_tests_path, ['.cpp', '.ll', '.test', '.py'])


def unit_case_results():
    return [47479, 161, 503, 7]


def regression_case_results():
    return [6689, 0, 0, 7]


def subfolder_name_returner(path, type=''):
    if type == 'test':
        os.chdir(path)
    folder_names_with_path = [os.path.abspath(name) for name in os.listdir(".") if os.path.isdir(name)]
    print(folder_names_with_path)
    os.chdir("../PAT") if type == 'test' else None
    return folder_names_with_path


def folder_wise_file_returner(root, type='', extensions=['.cpp']):
    folder_file_dict = {}
    for folder in subfolder_name_returner(root, type):
        folder_file_dict[folder] = file_name_with_path_returner(folder, extensions)
    return folder_file_dict

    # unit_test_asserts_dict = \
    #     generic_count_returner_with_line_numbers(i, assert_statements, 'assert')


def test_files_folderwise_file_returner():
    return folder_wise_file_returner('../unittests', 'test', ['.cpp']), folder_wise_file_returner('../test', 'test',
                                                                                                  config.REGRESSION_INCLUDE_EXTENSIONS)


def dict_summer(input_dict):
    summer = 0
    for key, value in input_dict.items():
        summer = summer + value[0]
    return summer


def generic_folder_wise_assert_doer(folderwise_assert_dict):
    test_folderwise_assert_dict = {}
    for key, value in folderwise_assert_dict.items():
        print("the key is ", key)
        test_folderwise_assert_dict[key] = dict_summer(
            generic_count_returner_with_line_numbers(value, [config.ASSERT_STATEMENT_REGEX], 'assert'))
    return test_folderwise_assert_dict


def assert_count_returner_folder_wise():
    unit_test_files_folderwise, reg_test_files_folderwise = test_files_folderwise_file_returner()

    return generic_folder_wise_assert_doer(unit_test_files_folderwise), generic_folder_wise_assert_doer(
        reg_test_files_folderwise)


def subfolder_name_non_abs(path, type=''):
    if type == 'test':
        os.chdir(path)
    folder_names = [name for name in os.listdir(".") if os.path.isdir(name)]
    print(folder_names)
    os.chdir("../PAT") if type == 'test' else None
    return folder_names


def common_pie(test_dict, labels, title, explode):
    lister = []

    for key, value in test_dict.items():
        lister.append(value)

    fig1, ax1 = plt.subplots()
    ax1.pie(lister,
            shadow=True, startangle=90, explode=explode)
    plt.title(f'Folder level Assertion Distribution for {title}')
    plt.legend(labels, loc='upper left', prop={'size': 6})
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig(f'Plots{os.path.sep}{title}pieplot.png')
    return lister
