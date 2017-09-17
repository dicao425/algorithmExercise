#!/usr/bin/python
from __future__ import print_function
import os
import sys
import math

FILE_PATH = "/home/root/t/tf_idf"

class TF_IDF(object):
    def __init__(self):
        self.docs = []
        self.docs_name = []
        self.tf = []
        self.idf = {}
        self.tf_idf = []

    def store_term_count(self, content):
        # Remove punctuation
        new_c = ""
        for i in content:
            if not i.isalpha() and i != " ":
                continue
            new_c += i
        c_list = [i.lower() for i in new_c.split(" ") if i]
        c_dict = {}
        for i in c_list:
            if i not in c_dict:
                c_dict[i] = 1
            else:
                c_dict[i] += 1
        self.docs.append(c_dict)

    def read_files(self, path = FILE_PATH):
        for file_item in os.listdir(path):
            if not file_item.endswith(".txt"):
                continue
            with open(os.path.join(FILE_PATH, file_item), "r") as f_obj:
                file_content = f_obj.read()
            self.docs_name.append(file_item)
            self.store_term_count(file_content)

    def cal_term_frequency(self):
        for tc in self.docs:
            tf_dict = {}
            sum_tc = sum(tc.values())
            for key in tc:
                tf_dict[key] = tc[key] / float(sum_tc)
            self.tf.append(tf_dict)

    def cal_idf(self):
        sum_docs = len(self.docs)
        for doc in self.docs:
            for word in doc:
                if word not in self.idf:
                    num_contain = sum(1 for ff in self.docs if word in ff)
                    self.idf[word] = math.log(sum_docs / float(1+num_contain)) if sum_docs != num_contain else 0.0

    def cal_tfidf(self):
        for item in self.tf:
            tfidf_dict = {}
            for w in item:
                tfidf_dict[w] = item[w] * self.idf[w]
            self.tf_idf.append(tfidf_dict)

    def search_words(self, str_input, sort=False):
        result = []
        for idx, doc in enumerate(self.tf_idf):
            tfidf = 0.0
            for w in str_input.split(" "):
                if w in doc:
                    tfidf += doc[w]
            result.append({str(tfidf): self.docs_name[idx]})
        return result if not sort else sorted(result, reverse=True)

def main():
    aa = TF_IDF()
    aa.read_files()
    aa.cal_term_frequency()
    aa.cal_idf()
    aa.cal_tfidf()
    
    import pdb
    pdb.set_trace()
    return 0

if __name__ == "__main__":
    sys.exit(main())
