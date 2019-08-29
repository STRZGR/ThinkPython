
# Tallying and printing words in words.txt without every five letter combination

fin = open('words.txt')

# Tallying number of words in words.txt

tally = 0
for line in fin:
    tally += 1
    
# initializing the tally and setting the least_freq_combo

least_freq_tally = 0
least_freq_combo = ""

# creating all possible combinations 

n = 0
p1 = n
while p1 < len(alphabet):
    p2 = p1 + 1
    while p2 < len(alphabet):
        p3 = p2 + 1
        while p3 < len(alphabet):
            p4 = p3 + 1
            while p4 < len(alphabet):
                p5 = p4 + 1
                while p5 < len(alphabet):
                    forbidden = (alphabet[p1] + alphabet[p2] + alphabet[p3] +
                                 alphabet[p4] + alphabet[p5])
                    avoids_tally = tally
                    fin = open('words.txt')
                    
                    # testing the new combination
                    
                    for line in fin:
                        if avoids(forbidden, line.strip()):
                            avoids_tally -=1
                    
                    # updating the tally and least_freq_combo
                    
                    if avoids_tally > least_freq_tally:
                        least_freq_tally = avoids_tally
                        least_freq_combo = forbidden
                    
                    p5 += 1
                p4 += 1
            p3 += 1
        p2 += 1
    p1 += 1
    
print(least_freq_combo)
print(least_freq_tally)
