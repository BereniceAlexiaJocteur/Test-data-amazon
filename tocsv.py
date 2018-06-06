import re

INPUT_FILE_NAME = "amazon-meta.txt"
OUTPUT_FILE_NAME = "Output.csv"

header = [
    "ASIN",
    "title",
    "groupe",
    "categories"]

f = open(INPUT_FILE_NAME, errors='ignore')
outfile = open(OUTPUT_FILE_NAME, "w")

# Write header
outfile.write(",".join(header) + "\n")

currentLine = []
a_categorie_exists = False
compteur = 0
for line in f:
    line = line.strip()
    if line == "":
        if not a_categorie_exists:
            currentLine.append("No categorie")
        outfile.write(",".join(currentLine))
        outfile.write("\n")
        currentLine = []
        compteur = 0
        a_categorie_exists = False
        continue
    parts = line.split(":", 2)
    if parts[0] == "ASIN" or parts[0] == "title" or parts[0] == "group":
        currentLine.append(re.sub(',', ' ', parts[1]))     # if for example the title contains a comma remove the comma to not creat a new collumn in the csv file
    if parts[0][0] == "|" and compteur == 0:
        list_categories = parts[0].split('|')
        try:
            categorie = re.sub(r'\[[0-9]*\]', '', list_categories[3])
            currentLine.append(categorie)
            compteur += 1
            a_categorie_exists = True
        except IndexError:
            categorie = re.sub(r'\[[0-9]*\]', '', list_categories[2])
            currentLine.append(categorie)
            compteur += 1
            a_categorie_exists = True


if currentLine != []:
    outfile.write(",".join(currentLine))


f.close()
outfile.close()