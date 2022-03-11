from modules.myModule import TextComparer
import pytest
import os
import shutil
from collections.abc import Iterable

urls = []
urls.append("https://www.gutenberg.org/files/84/84-0.txt")
urls.append("https://www.gutenberg.org/files/1342/1342-0.txt")

tc = TextComparer(urls)

@pytest.fixture
def cleanup():
    # Setup: fill with any logic you want
    shutil.rmtree("./downloads")
    os.makedirs("./downloads")
    yield # this is where the testing happens

    # Teardown : fill with any logic you want
    shutil.rmtree("./downloads")
    os.makedirs("./downloads")
   

#Downloads file and test that size is bigger than 10 bytes
def test_download(cleanup):
    tc.download(urls[0])
    empty_files = False
    for file in tc.filenames:
        sz = os.path.getsize(file)
        print(sz)
        if sz < 10:
            empty_files = True
    assert empty_files == False

def test_multi_download(cleanup):
    tc.multi_download()
    empty_files = False
    for file in tc.filenames:
        sz = os.path.getsize(file)
        print(sz)
        if sz < 10:
            empty_files = True
    assert empty_files == False


def test_iter(cleanup):
    my_iterable = tc.__iter__()
    assert isinstance(my_iterable, Iterable) == True


def test_avg_vowels(cleanup):
    #3 words - 6 total vowes = 2 average pr word!
    expected = 2
    actual = tc.avg_vowels("##HI! heello ##THERE")
    assert expected == actual

def test_hardest_read(cleanup):
    _filenames = ['./downloads/file1.txt','./downloads/file2.txt']
    with open(_filenames[0], 'w') as f_2:
        f_2.write("##HI! heello ##THERE")

    with open(_filenames[1], 'w') as f_2:
        f_2.write("##HIi! heelloooooooooooooooooo ##THERE")

    tc.filenames = _filenames

    file_with_highest_average_vowels = tc.hardest_read_multiprocessing()
    assert _filenames[1] == file_with_highest_average_vowels[0]
