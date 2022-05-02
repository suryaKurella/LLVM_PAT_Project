from authors_py_drill_latest import authors_commits_driller
from csv_writers import assert_writer, assert_debug_writer, author_commit_writer, common_test_folderwise_asserts_writer
from productionfile_script import production_assert_debug_dict
from midrunner import assert_count_test_returner
from subprocess import call

# csvs
assert_writer(assert_count_test_returner())
common_test_folderwise_asserts_writer()
assert_debug_writer(production_assert_debug_dict())
common_test_folderwise_asserts_writer()

# pydriller scripts
author_commit_writer(authors_commits_driller())
call(["python", "gen-figures.py"])
call(["python", "llvm_pydrill.py"])
