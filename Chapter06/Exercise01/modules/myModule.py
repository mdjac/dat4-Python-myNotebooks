import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
import os
from concurrent.futures import ProcessPoolExecutor
import multiprocessing


class TextComparer:
    def __init__(self, url_list):
        self.url_list = url_list
        self.filenames = []

    def download(self,url):
        #Gets filename
        path = urlparse(url).path
        filename = os.path.basename(path)

        #Downloads
        response = requests.get(url, stream = True)
        if(response.status_code == 404):
            raise NotFoundException(url)
        else:
            savedPath = f"./downloads/{filename}"
            with open(savedPath,"wb") as text_file:
                for chunk in tqdm(response.iter_content(chunk_size=1024)):
                    text_file.write(chunk)

            #Adds filenames to property        
            self.filenames.append(savedPath)
    
    def multi_download(self):
        with ThreadPoolExecutor(len(self.url_list)) as ex:
            for url in self.url_list:
                ex.submit(self.download,url)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        while self.index < len(self.filenames):
            x = self.filenames[self.index]
            self.index += 1
            return x
        raise StopIteration

    def urllist_generator(self):
        for element in self.filenames:
            yield element
    
    def avg_vowels(self,text):
        vowels = "AaEeIiOoUu"
        lines = text.split()
        number_of_words = len(lines)

        
        total_vowels = 0;
        
        for line in lines:
            vowels_in_line = [char for char in line if char in vowels]
            total_vowels += len(vowels_in_line)

        average_vowels = total_vowels / number_of_words
        return average_vowels

    #Runs with all processors
    def hardest_read_multiprocessing(self, return_all=None):
        files = []
        with ProcessPoolExecutor(multiprocessing.cpu_count()) as ex:
            res = ex.map(self.open_file_and_count_vowels, self.filenames)
        files = sorted(list(res), key=lambda x:x[1], reverse=True)
        if(return_all == None):
            return files[0]
        else:
            return files

    #Runs with Single
    def hardest_read(self, return_all=None):
        files = []
        for file in self.filenames:
            result = self.open_file_and_count_vowels(file)
            files.append(result)
        files = sorted(files, key=lambda x:x[1], reverse=True)
        if(return_all == None):
            return files[0]
        else:
            return files

    def open_file_and_count_vowels(self,filename):
        with open(filename,'r') as file:
                data = file.read()
                average_vowels = self.avg_vowels(data)
                return (filename,average_vowels)










        

        






class NotFoundException(Exception): 
    def __init__(self,url):
        self.url = url
        super().__init__(f"ERROR - URL : {self.url} - responded with 404")