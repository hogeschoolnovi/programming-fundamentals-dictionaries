zin = "dit is een testzin om te testen of dit programma werkt"
aantal_woorden = {}

woorden = zin.split()
for woord in woorden:
    if woord in aantal_woorden:
        aantal_woorden[woord] += 1
    else:
        aantal_woorden[woord] = 1

print(aantal_woorden)
