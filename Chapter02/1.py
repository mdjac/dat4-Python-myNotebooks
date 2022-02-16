import pathlib
print(pathlib.Path().resolve())


print("----- Exercise -----")
with open('../../data/verbs') as verbs_file:
    verbs = verbs_file.read().split('\n')



with open('../../data/nouns') as nouns_file:
    nouns = nouns_file.read().split('\n')


with open('../../data/adjectives') as adjectives_file:
    adjectives = adjectives_file.read().split('\n')


sentences = [""+adjective+" "+noun+" "+verb for adjective in adjectives for noun in nouns for verb in verbs]

from pprint import pprint
print(sentences[10000:10050])

print("----- END -----")