import csv
import os
from collections import Counter

from matplotlib import pyplot as plt


def top_5_test_commits_author_plot():
    result = {}
    reader = csv.DictReader(open('Files/author_commits.csv'))
    for row in reader:
        result[row['Author']] = int(row['Number of Commits'])
    k = Counter(result)
    top_authors = k.most_common(5)
    author_names = [x[0] for x in top_authors]
    total_commits = [x[1] for x in top_authors]
    plt.bar(range(len(top_authors)), total_commits, tick_label=author_names)

    plt.xlabel("Author Names")
    plt.ylabel("Number of commits")
    plt.title("Top 5 Authors with Highest Number of Commits")

    # plt.show()

    plt.savefig(f'Plots{os.path.sep}top_5_test_authors.png')
