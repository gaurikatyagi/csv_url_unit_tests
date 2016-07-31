import pandas as pd
import warnings
import os
import urllib2
import validators

def url_to_csv(url,fname):
    """
        This function will go to a url and download the csv file on that location. It will further save it to a folder as
        /data/fname
        This function should raise a TypeError if a URL cannot be parsed as CSV
        It raises a ValueError when the user does not pass in a valid URL that can be accessed

        :param url: string variable which is used to pass a url
        :param fname: filename used to store the csv file in /data folder
        :return: None
    """
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", fname)
    try:
        urllib2.urlopen(url)
        if validators.url(url) != True:
            raise ValueError
        else:
            data = pd.read_csv(url)
            data.to_csv(file_path)
    except (urllib2.HTTPError):
        raise ValueError
    except (IOError):
        raise TypeError
    # except pd.io.common.CParserError:
    except pd.parser.CParserError:
        raise TypeError
    except Exception as e:
        raise ValueError
    return file_path

def batch_url_to_csv(urls,fnames):
    """
        Takes a list of URLs to CSV files, downloads them, and saves them to files given by the list of names in fnames.
        Returns a list of the filenames saved.
        should NOT raise any errors if a URL fails to be accessed or if the URL cannot be parsed as CSV; instead, it
        should simply emit a RuntimeWarning (Links to an external site.) indicating that the URL was skipped.
        :param urls: list of urls to be traversed
        :param fnames: list of file names to be saved
        :return: data_names list of paths to files saved
    """
    files_saved=[]
    for index in range(len(urls)):
        try:
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", fnames[index])
            if urls[index] in urls[0:index]:
                    raise AssertionError
            # if (file_path in files_saved) or (urls[index] in urls[0:index]):
            #     continue
            else:
                files_saved.append(url_to_csv(urls[index],fnames[index]))
        except ValueError:
            warnings.warn('UserGeneratedWarning!',RuntimeWarning)
        except TypeError:
            warnings.warn('UserGeneratedWarning!',RuntimeWarning)
        except AssertionError:
            raise AssertionError("Duplicate URLs cannot be present in the parameter 'urls'.")
    return files_saved

def url_to_df(url):
    """
    Takes a URL to a CSV file and returns the contents of the URL as a Pandas DataFrame
    :param url: string variable which is used to pass a url
    :return: pandas DataFrame which contains the data on the url
    """
    data = pd.read_csv(url, header = None)
    return data

if __name__ == "__main__":
    # print url_to_csv("code.activestate.com/recipes/286225-httpexists-find-out-whether-an-http-reference-is-v/",
    #            "abalone.csv")
    # print url_to_csv("http://code.activestate.com/recipes/286225-httpexists-find-out-whether-an-http-reference-is-v/", "abc.csv")
    # print url_to_csv("google.com", "abc.csv")
    # print url_to_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.datx','abalone.csv')
    # print url_to_csv("webhp?sourceid=chrome-instant&rlz=1C5CHFA_enUS698US699&ion=1&espv=2&ie=UTF-8", "hello.csv")
    # print url_to_csv("webhp?sourceid=chrome-instant&rlz=1C5CHFA_enUS698US699&ion=1&espv=2&ie=UTF-8", "hello.csv")

    # url1 = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
    # url2 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00244/fertility_Diagnosis.txt"
    # urlx3 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00252/pop_failures.dat"
    # urlx4 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00250/example-data.dat"
    # url5 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00246/3D_spatial_network.txt"
    # urlx6 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00240/UCI%20HAR%20Dataset.names"

    # url1 = "hello"
    # url2 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00244/fertility_Diagnosis.txt"
    # urlx3 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00252/pop_failures.dat"
    # urlx4 = "archive.ics.uci.edu/ml/machine-learning-databases"
    # url5 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00246/3D_spatial_network.txt"
    # urlx6 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00240/UCI%20HAR%20Dataset.names"
    # saved = batch_url_to_csv([url2, urlx3, urlx4, url5, urlx6, url1], ["url2.csv", "urlx3.csv", "urlx4.csv",
    #                                                            "url5.csv", "urlx6.csv", "url1.csv"])
    # print saved

    # saved2 = batch_url_to_csv([url2, urlx3, url2, url5, urlx6, url2], ["url2.csv", "urlx3.csv", "urlx4.csv",
    #                                                            "url5.csv", "urlx6.csv", "url1.csv"])
    # print saved2
    # data = url_to_df("https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data")

    url1 = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
    url2 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00244/fertility_Diagnosis.txt"
    urlx3 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00252/pop_failures.dat"
    urlx4 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00250/example-data.dat"
    url5 = "helloollooo"
    urlx6 = "https://archive.ics.uci.edu/ml/machine-learning-databases/00240/UCI%20HAR%20Dataset.names"
    urls = [url2, urlx3, urlx4, url5, urlx6, url1]
    fnames = ["url2.csv", "urlx3.csv", "urlx4.csv", "url5.csv", "urlx6.csv", "url1.csv"]

    saved = batch_url_to_csv(urls, fnames)