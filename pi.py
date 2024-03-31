text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

text = "How I want a drink alcoholic of course after the heavy chapters involving\
        quantum mechanics All of thy geometry Herr Planck is fairly hard"

text1 = list(map(len,(text.split())))

for i in text1:
    print(str(i), end = "")