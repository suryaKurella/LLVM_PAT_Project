from datetime import datetime
from pydriller import Repository
import matplotlib.pyplot as plt


def authors_commits_driller():
    author_dict = {}
    for commit in Repository('https://github.com/llvm-mirror/llvm.git',
                             since=datetime(2019, 6, 8, 17, 0, 0)).traverse_commits():
        if commit.author.name not in author_dict.keys():
            author_dict[commit.author.name] = 1
        else:
            author_dict[commit.author.name] += 1
    print(author_dict)
    names = list(author_dict.keys())
    values = list(author_dict.values())
    plt.bar(range(len(author_dict)), values, tick_label=names)
    plt.show()
    return author_dict
