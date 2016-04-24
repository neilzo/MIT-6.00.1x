# Counting Vowels
# Passes with output 'Number of vowels: 5'
count = 0
s = 'azcbobobegghakl'

for i in s:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        count += 1

print 'Number of vowels: %d' % count
