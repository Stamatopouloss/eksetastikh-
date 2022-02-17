#3.Σας δίνεται ένα αρχείο κειμένου το οποίο έχει μόνο ASCII χαρακτήρες. Αρχικά, κάντε την κατάλληλη επεξεργασία ώστε να σας μείνει κείμενο με μόνο γράμματα και τον κενό χαρακτήρα (space). Χωρείστε αυτό το κείμενο σε λέξεις σύμφωνα με το κενό και ξεκινείστε να αφαιρείτε ζευγάρια λέξεων αν το άθροισμα των γραμμάτων τους είναι 20. Βγάλτε τα στατιστικά για το μήκος των λέξεων που έμειναν, πχ. 10 λέξεις του ενός γράμματος, 12 λέξεις των 2 γραμμάτων, 3 λέξεις των 3 γραμμάτων κτλ.

import re

file = input()
f = open(file, "r")
contents = f.read()
contents = contents.lower()
contents = re.sub("[^a-zA-Z ]+", "", contents)
contents = contents.split(" ")
contents = [word for word in contents if len(word) < 20 ]

wordlist = [0 for i in range(19)]
for word in contents:
    wordlist[len(word)] += 1

for i in range(len(wordlist)):
    if wordlist[i] > 0:
        print("There are", wordlist[i], "words with", i+1, "characters")
