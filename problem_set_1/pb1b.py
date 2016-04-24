# Counting 'bob's
# Passes with output 'Number of times bob occurs is: 2'
count = 0
s = 'azcbobobegghakl'
location = -1

while True:
    location = s.find('bob', location + 1)
    if (location == -1):
        break
    count += 1

print 'Number of times bob occurs is: %d' % count
