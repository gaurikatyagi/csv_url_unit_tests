import pandas as pd
import warnings
import os
import urllib2
import validators
import urlparse

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
        if validators.url(url) != True:# or urlparse.urlparse(url) != True:
            raise ValueError
        else:
            data = pd.read_csv(url)
            data.to_csv(file_path)
    except (urllib2.HTTPError):
        raise ValueError
    except (IOError):
        raise TypeError
    except (pd.io.common.CParserError):
        raise TypeError
    except Exception as e:
        raise ValueError
    return file_path

def batch_url_to_csv(url,fname):
    """
        Takes a list of URLs to CSV files, downloads them, and saves them to files given by the list of names in fnames.
        Returns a list of the filenames saved.
        :param urls:
        :param fnames:
        :return: data_names
    """
    list_of_files=[]
    for i in range(len(url)):
        print "Reading the file: ",url[i]
        try:
          list_of_files.append(url_to_csv(url[i],fname[i]))
        except ValueError:
           warnings.warn('RuntimeWarning,%s has been skipped' % (url[i]))
        except TypeError:
          warnings.warn('%s has been skipped'%(url[i]))
    return list_of_files

def url_to_df(url):
    """
    Takes a URL to a CSV file and returns the contents of the URL as a Pandas DataFrame
    :param url: string variable which is used to pass a url
    :return: pandas DataFrame which contains the data on the url
    """
    data = pd.read_csv(url, header = None)
    return data


# print batch_url_to_csv(url=['https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data',
#                             'http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data',
#                             'www.google.com'],
#                        fname=['adult', 'abalone', 'google'])

if __name__ == "__main__":
    print url_to_csv("code.activestate.com/recipes/286225-httpexists-find-out-whether-an-http-reference-is-v/",
               "abalone.csv")
    # print url_to_csv("http://code.activestate.com/recipes/286225-httpexists-find-out-whether-an-http-reference-is-v/", "abc.csv")
    # print url_to_csv("google.com", "abc.csv")
    # print url_to_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.datx','abalone.csv')
    # print url_to_csv("webhp?sourceid=chrome-instant&rlz=1C5CHFA_enUS698US699&ion=1&espv=2&ie=UTF-8", "hello.csv")
    # print url_to_csv("webhp?sourceid=chrome-instant&rlz=1C5CHFA_enUS698US699&ion=1&espv=2&ie=UTF-8", "hello.csv")
    # data = url_to_df("https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data")