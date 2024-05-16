# This is a sample Python script.
import json
import os
import numpy as np
from tabulate import tabulate

# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

DIRECTORIES = [
    # "magicCardsDeck",
    "technologyCardsDeck"
]

EST_WPM = 139

# Initialize an empty list to store the data
tech_data = []

for directory in DIRECTORIES:
    # read all the json files in the directory
    for filename in os.listdir(directory):
        if not filename.endswith(".json"):
            continue

        with open(os.path.join(directory, filename), "r") as f:
            data = json.load(f)

        # print(data["num_words_back"])

        time_to_read = (data["num_words_back"] / EST_WPM) * 60

        tech_data.append([data["title"], data["num_words_back"], time_to_read])
        # print(data["title"], data["num_words_back"])

magic_data = []
# read all the json files in the directory
for filename in os.listdir("magicCardsDeck"):
    if not filename.endswith(".json"):
        continue

    with open(os.path.join("magicCardsDeck", filename), "r") as f:
        data = json.load(f)

    # print(data["num_words_back"])

    time_to_read = (data["word_count"] / EST_WPM) * 60

    magic_data.append([data["title"], data["word_count"], time_to_read])
    # print(data["title"], data["num_words_back"])

# Convert the list to a numpy array
# arr = np.array(data_list)


data_list = magic_data + tech_data

print(tabulate(data_list, headers=["Title", "num_words_back", "time_to_read (s)"]))

# Calculate the statistics for each category
all_cards_ttr = np.array([f[2] for f in data_list])
all_cards_stats = ["all cards", all_cards_ttr.mean(), all_cards_ttr.min(), all_cards_ttr.max()]

magic_cards_ttr = np.array([f[2] for f in magic_data])
magic_cards_stats = ["magic card", magic_cards_ttr.mean(), magic_cards_ttr.min(), magic_cards_ttr.max()]

tech_cards_ttr = np.array([f[2] for f in tech_data])
tech_cards_stats = ["tech cards", tech_cards_ttr.mean(), tech_cards_ttr.min(), tech_cards_ttr.max()]

# Combine the statistics into a list of lists
table_data = [
    magic_cards_stats,
    tech_cards_stats,
    all_cards_stats,
]

# Define the headers for the table
headers = ["Category", "Mean TTR", "Minimum TTR", "Maximum TTR"]

# Print the table using tabulate
print(tabulate(table_data, headers=headers, floatfmt=".2f"))

# arr = np.array([f[2] for f in data_list])
# print(f"Mean TTR: {arr.mean()}, Minimum TTR: {arr.min()}, Maximum TTR: {arr.max()}")
