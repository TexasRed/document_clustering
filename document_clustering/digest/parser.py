import json
import random
import os
import numpy as np


class Parser:
    input_dir = ''
    suffix = ''
    sample_size = 0

    def __init__(self, input_dir, suffix='json', sample_size=100):
        self.input_dir = input_dir
        self.suffix = suffix
        self.sample_size = sample_size

    def parse(self, topics):
        input_files = []
        for topic in topics:
            file_name = os.path.join(self.input_dir, topic + "." + self.suffix)
            input_files.append(file_name)
        return self.parse_files(input_files)

    def parse_files(self, file_names, shuffle=True):
        pages = []
        urls = []
        names = []
        descriptions = []
        categories = []

        for filename in file_names:
            with open(filename) as data_file:
                file_base_name = os.path.basename(filename)
                category = '[' + os.path.splitext(file_base_name)[0] + '] '
                data = json.load(data_file)
                documents = data[:self.sample_size]
                # documents = np.random.choice(data, size=self.sample_size, replace=False, p=None)
                for document in documents:
                    pages.append((document['url'][0],  category + document['name'][0],
                                  document['description'][0], category))

        if shuffle is True:
            for i in range(10):
                random.shuffle(pages)

        for page in pages:
            urls.append(page[0])
            names.append(page[1])
            descriptions.append(page[2])
            categories.append(page[3])

        return urls, names, descriptions, categories


