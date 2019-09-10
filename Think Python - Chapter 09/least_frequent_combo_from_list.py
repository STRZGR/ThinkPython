# from http://amjith.blogspot.com/2011/10/picking-items-from-list-of-recursion.html

def combo(w, l):
    lst = []
    for i in range(len(w)):
        if l == 1:
            lst.append(w[i])
        for c in combo(w[i+1:], l-1):
            lst.append(w[i] + c)
    return lst

combo_list = combo(alphabet, 5)

# Tallying and printing words in words.txt without every five letter combination

fin = open('words.txt')

# Tallying number of words in words.txt

tally = 0
for line in fin:
    tally += 1

# initializing the tally and setting the least_freq_combo

least_freq_tally = tally
least_freq_combo = ""

for c in combo_list:
    avoids_tally = tally
    fin = open('words.txt')
    for line in fin:
        if avoids(c, line.strip()):
            avoids_tally -=1

    if avoids_tally < least_freq_tally:
        least_freq_tally = avoids_tally
        least_freq_combo = c
print(least_freq_combo)
print(least_freq_tally)