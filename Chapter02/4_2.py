import argparse
import os
import urllib.request as req
from urllib.parse import urlparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Downloads a file and saves it on your local filesystem")
    parser.add_argument("URL",help="URL where file is stored")
    parser.add_argument("-d","--destination",help="destination to save on local filesystem")

    args = parser.parse_args()

    url = args.URL
    destination = args.destination

    print("this is the URL: ",url)

    if(destination):
        print("this is the destination: ",destination)
        final_location = destination
    else:
        filename = os.path.basename(urlparse(url).path)
        if len(filename) == 0:
            filename = "default_file"
        final_location = "./"+filename


    request = req.Request(url)
    response = req.urlopen(request)

    file_extension = response.info().get_content_subtype()

    final_location += "."+file_extension

    print(final_location)

    with open(final_location, "b+w") as f:
        f.write(response.read())

