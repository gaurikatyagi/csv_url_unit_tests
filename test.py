import unittest
from requester import url_to_csv, batch_url_to_csv, url_to_df
import os
import pandas as pd
from pandas.util.testing import assert_frame_equal
import warnings

class test_url_to_csv(unittest.TestCase):

    def test_no_url(self):
        """
        url_to_csv( ) should raise a ValueError when the user does not pass in a valid URL that can be accessed.
        """
        url = "  "
        fname = "http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.datx"
        with self.assertRaises(ValueError):
            url_to_csv(url, fname)

    def test_correct_url(self):
        """
        url_to_csv( ) should raise a ValueError when the user does not pass in a valid URL that can be accessed.
        """
        url = "webhp?sourceid=chrome-instant&rlz=1C5CHFA_enUS698US699&ion=1&espv=2&ie=UTF-8"
        fname = "try.csv"
        with self.assertRaises(ValueError):
            url_to_csv(url, fname)

    def test_correct_url_csv(self):
        """
        Checks that the file has been saved and path returned
        """
        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer/breast-cancer-data"
        fname = "breast.csv"
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", fname)
        print file_path
        self.assertEquals(url_to_csv(url, fname), file_path)

    def test_wrong_url_csv(self):
        """
        url_to_csv( ) should raise a TypeError if a URL cannot be parsed as CSV.
        """
        with self.assertRaises(TypeError):
            url = "http://code.activestate.com/recipes/286225-httpexists-find-out-whether-an-http-reference-is-v/"
            fname = "wrongname.csv"
            url_to_csv(url, fname)

    def test_url_no_csv(self):
        """
        url_to_csv( ) should raise a TypeError if a URL cannot be parsed as CSV.
        """
        with self.assertRaises(TypeError):
            url = "http://stackoverflow.com/questions/1393324/in-python-given-a-url-to-a-text-file-what-is-the-simplest-way-to-read-the-cont"
            fname = "don't_save.csv"
            url_to_csv(url, fname)

class test_url_to_df(unittest.TestCase):

    def test_DataFrame(self):
        """
        Ensure url_to_df() returns a Pandas DataFrame object
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
        url1 = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
        url2 = "hellooooo"
        urlx6 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00240/UCI%20HAR%20Dataset.names"
        urls = [url2, urlx6, url1]
        fnames = ["url2.csv", "urlx6.csv", "url1.csv"]

        with warnings.catch_warnings(record=True) as warning_created:
            # Causes all warnings to always be triggered
            warnings.simplefilter("always")
            batch_url_to_csv(urls, fnames)
            assert len(warning_created) == 1
            assert issubclass(warning_created[-1].category, RuntimeWarning)
            assert "UserGeneratedWarning!" in str(warning_created[-1].message)

    def test_url_file_number(self):
        """
        Ensure that batch_url_to_csv() generates the same number of files as valid CSV URLs (taking into account URLs
        that might have been skipped due to being invalid or not CSVs).
        """
        url1 = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
        url2 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00244/fertility_Diagnosis.txt"
        urlx3 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00252/pop_failures.dat"
        urlx4 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00250/example-data.dat"
        url5 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00246/3D_spatial_network.txt"
        urlx6 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00240/UCI%20HAR%20Dataset.names"
        self.assertEquals(
            len(batch_url_to_csv([url2, urlx3, urlx4, url5, urlx6, url1],
                                 ["url2.csv", "urlx3.csv", "urlx4.csv", "url5.csv", "urlx6.csv", "url1.csv"]))
                          , 5)

    def test_url_file_number_2(self):
        """
        Ensure that batch_url_to_csv() generates the same number of files as valid CSV URLs (taking into account URLs
        that might have been skipped due to being invalid or not CSVs).
        """
        url1 = "hello"
        url2 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00244/fertility_Diagnosis.txt"
        urlx3 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00252/pop_failures.dat"
        urlx4 = "http://code.activestate.com/recipes/286225-httpexists-find-out-whether-an-http-reference-is-v/"
        url5 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00246/3D_spatial_network.txt"
        urlx6 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00240/UCI%20HAR%20Dataset.names"
        self.assertEquals(
            len(batch_url_to_csv([url2, urlx3, urlx4, url5, urlx6, url1],
                                 ["url2.csv", "urlx3.csv", "urlx4.csv", "url5.csv", "urlx6.csv", "url1.csv"])
                ), 3)

    def test_url_file_name(self):
        """
        Ensure that batch_url_to_csv( ) returns the correct filenames (i.e. when invalid CSV URLs are passed in).
        """
        url1 = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
        urlx3 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00252/pop_failures.dat"
        urlx6 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00240/UCI%20HAR%20Dataset.names"
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
        self.assertEquals(
            (batch_url_to_csv([urlx3, urlx6, url1],
                                 ["urlx3.csv", "urlx6.csv", "url1.csv"]))
            , [os.path.join(file_path, "urlx3.csv"), os.path.join(file_path, "url1.csv")])

    def test_url_file_name_2(self):
        """
        Ensure that batch_url_to_csv( ) returns the correct filenames (i.e. when valid CSV URLs are passed in).
        """
        url2 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00244/fertility_Diagnosis.txt"
        urlx3 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00252/pop_failures.dat"
        urlx4 = "http://code.activestate.com/recipes/286225-httpexists-find-out-whether-an-http-reference-is-v/"
        url5 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00246/3D_spatial_network.txt"
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

        self.assertEquals(
            (batch_url_to_csv([url2, urlx3, urlx4, url5],["url2.csv", "urlx3.csv", "urlx4.csv", "url5.csv"])
            ), [os.path.join(file_path, "url2.csv"), os.path.join(file_path, "urlx3.csv"), os.path.join(file_path, "url5.csv")])

    def test_unique_csv(self): ##NOT
        """
        Ensure that the contents of each file generated by batch_url_to_csv() is different if different URLs are passed.
        """
        url2 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00244/fertility_Diagnosis.txt"
        urlx3 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00252/pop_failures.dat"
        urlx4 = "http://code.activestate.com/recipes/286225-httpexists-find-out-whether-an-http-reference-is-v/"
        url5 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00246/3D_spatial_network.txt"
        saved = batch_url_to_csv([url2, urlx3, urlx4, url5], ["url2.csv", "urlx3.csv", "urlx4.csv", "url5.csv"])
        # saved = batch_url_to_csv([url2, urlx3, urlx4, url5], ["url2.csv", "urlx3.csv", "urlx4.csv", "url5.csv"])
        length_files = len(saved)-1
        for index in range(length_files):
            for item in saved[index+1:]:
                self.assertRaises(assert_frame_equal(pd.read_csv(saved[index]), pd.read_csv(item)), AssertionError)

    def test_duplicate_url(self):
        """
        If a user passes in duplicate URLs to batch_url_to_csv( ) then an AssertionError should be raised that says
        "Duplicate URLs cannot be present in the parameter 'urls'."
        """
        url2 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00244/fertility_Diagnosis.txt"
        urlx3 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00252/pop_failures.dat"
        urlx4 = "http://code.activestate.com/recipes/286225-httpexists-find-out-whether-an-http-reference-is-v/"
        with self.assertRaises(AssertionError):
            saved = batch_url_to_csv([url2, urlx3, url2, urlx4],
                                     ["url2.csv", "urlx3.csv", "url2.csv", "urlx4.csv"])