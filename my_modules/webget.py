import os
import urllib.request as req
from urllib.parse import urlparse


def download(url, to=None):
    """Download a remote file specified by a URL to a 
    local directory.

    :param url: str
        URL pointing to a remote file.

    :param to: str
        Local path, absolute or relative, with a filename 
        to the file storing the contents of the remote file.
    """

    if to:
        final_location = to
    else:
        filename = os.path.basename(urlparse(url).path)
        final_location = "./"+filename

    file_exists = os.path.exists(final_location)
    if file_exists != True:
        req.urlretrieve(url,filename=final_location)
    else:
        print("File already exists!!")



if __name__ == '__main__':
    url = 'https://wfs-kbhkort.kk.dk/k101/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=k101:skolegrunddistrikt&outputFormat=csv&SRSNAME=EPSG:4326'
    download(url)
