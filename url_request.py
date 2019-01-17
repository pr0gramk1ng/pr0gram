import urllib.request
from http import HTTPStatus
from urllib.error import HTTPError, URLError

def main():
    url = "http://httpbin.org/html"
    
    try:
        result = urllib.request.urlopen(url)
        print("Result code: {0}".format(result.status))
        if(result.getCode() == HTTPStatus.OK):
            print(result.read().decode('utf-8'))
    except HTTPError as err:
        print("Error: {0}".format(err.code))
    except URLError as err:
        print("Yeah that server is bunk. {0}".format(err))
    
    
main()
