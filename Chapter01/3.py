print("----- Exercise1 -----")

odd_numbers01 = [number for number in (range(1,21)) if number % 2 != 0]
odds_numbers02 = [number for number in (range(1,21,2))];
print(odd_numbers01)
print(odd_numbers01)




print("----- END -----")


print("----- Exercise2 -----")
even_numbers_to_one_million = [number for number in range(1,1000001) if number % 2 == 0]
print(min(even_numbers_to_one_million))
print(max(even_numbers_to_one_million))
print(sum(even_numbers_to_one_million))
print("----- END -----")


print("----- Exercise3 -----")
multiples_by_3 = [number for number in range(3,301) if number%3 == 0]
print(multiples_by_3)

print("----- END -----")

print("----- Exercise4 -----")
cubes_1_to_10 = [number**3 for number in range(1,11)]
print(cubes_1_to_10)
print("----- END -----")


print("----- TimeIT -----")
import timeit;

cmd = "-".join(str(n) for n in range(100))
print(timeit.timeit(cmd,number=10))
print(cmd)

print("----- END -----")


image_0 = {'color': 'greyscale', 'size': 289983, 'type': 'jpg',
         'address': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Moby_Dick_p510_illustration.jpg'}
image_1 = {'color': 'greyscale', 'size': 492872, 'type': 'jpg',
         'address': 'https://upload.wikimedia.org/wikipedia/commons/f/f7/Queequeg.JPG'}
image_2 = {'color': 'greyscale', 'size': 497121, 'type': 'jpg',
         'address': 'https://upload.wikimedia.org/wikipedia/commons/8/8b/Moby_Dick_final_chase.jpg'}

article_images = [image_0, image_1, image_2]

print(article_images[0]['color'])
print(article_images[0].get('color'))
print(article_images[0].items())


image = {'color': 'greyscale', 'size': 289983, 'type': 'jpg',
         'address': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Moby_Dick_p510_illustration.jpg'}

print(image.get('not_in_list', "the item was not in the list")) #Returns second argument if item is not found
print(image['color'])

image['color'] = "new color"

print(image)

