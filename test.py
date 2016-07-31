import unittest
from requester import url_to_csv, batch_url_to_csv, url_to_df
import os
import pandas as pd

class test_url_to_csv(unittest.TestCase):

    # def test_no_url(self):
    #     url = "  "
    #     fname = "http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.datx"
    #     self.assertRaises(TypeError, url_to_csv(url, fname))

    def test_correct_url(self):
        url = ""
        fname = "webhp?sourceid=chrome-instant&rlz=1C5CHFA_enUS698US699&ion=1&espv=2&ie=UTF-8"
        with self.assertRaises(ValueError):
            url_to_csv(url, fname)

    def test_correct_url_csv(self):
        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer/breast-cancer-data"
        fname = "breast.csv"
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", fname)
        print file_path
        self.assertEquals(url_to_csv(url, fname), file_path)

    def test_wrong_url_csv(self):
        with self.assertRaises(TypeError):
            url = "http://code.activestate.com/recipes/286225-httpexists-find-out-whether-an-http-reference-is-v/"
            fname = "wrongname.csv"
            url_to_csv(url, fname)

    def test_url_no_csv(self):
        with self.assertRaises(TypeError):
            url = "http://stackoverflow.com/questions/1393324/in-python-given-a-url-to-a-text-file-what-is-the-simplest-way-to-read-the-cont"
            fname = "don't_save.csv"
            url_to_csv(url, fname)

class test_url_to_df(unittest.TestCase):

    def test_DataFrame(self):
        """
        Ensure url_to_df( ) returns a Pandas DataFrame object
        """
        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
        self.assertEquals(type(url_to_df(url)),type(pd.DataFrame([{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}])))

    def test_rows(self):
        """
        Ensure the number of rows in the Pandas DataFrame returned by url_to_df( ) matches the number of rows in the
        CSV when there is no header row in the CSV
        Do you mean the link to csv?
        Do you mean a csv which has been stored? But, this function does not store
        """
        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data","abalone.csv")
        data_rows = pd.read_csv(url, header = None).shape[0]
        self.assertEquals(url_to_df(url).shape[0], data_rows)

class test_batch_url_to_csv(unittest.TestCase):

    def test_url_fail_runtime(self):
        """
        Should NOT raise any errors if a URL fails to be accessed or if the URL cannot be parsed as CSV; instead, it
        should simply emit a RuntimeWarning (Links to an external site.) indicating that the URL was skipped.
        """
        pass