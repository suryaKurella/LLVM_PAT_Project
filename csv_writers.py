import csv
import os

from PAT.utils import assert_count_returner_folder_wise


def assert_writer(dict_list):
    with open(f'Files{os.path.sep}assert_count.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["File Name", "Assert Count"])
        for key, value in dict_list.items():
            key = key.split(f"lllvm{os.path.sep}")[1]
            writer.writerow([key, value[0]])


def assert_debug_writer(dict_list):
    with open(f'Files{os.path.sep}production_assert_debug_count.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quoting=csv.QUOTE_MINIMAL)

        writer.writerow(["File Name", "Assert Count", "Assert Location", "Debug Count", "Debug Location"])
        for key, value in dict_list.items():
            key = key.split(f"lllvm{os.path.sep}")[1]
            writer.writerow([key, value[0], value[1], value[2][0], value[2][1]])


def author_commit_writer(dict_list):
    with open(f'Files{os.path.sep}author_commits.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Author", "Number of Commits"])
        for key, value in dict_list.items():
            writer.writerow([key, value])


def tets_folder_wise_writer(folder_name, test_dict):
    with open(f'Files{os.path.sep}{folder_name}folderwise_assert_count.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Folder Name", "Assert Count"])
        for key, value in test_dict.items():
            key = key.split(f"lllvm{os.path.sep}")[1]
            writer.writerow([key, value])


def common_test_folderwise_asserts_writer():
    unit_tests_for_pie, regression_tests_for_pie = assert_count_returner_folder_wise()
    tets_folder_wise_writer('Unit Test', unit_tests_for_pie)
    tets_folder_wise_writer('Regression Test', regression_tests_for_pie)



