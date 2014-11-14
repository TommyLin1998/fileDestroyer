#! /usr/bin/env python3

fileName = input('What file should I destroy? ')
times = int(input('How many times should I overwrite it? '))

f = open(fileName, "r+")
fileContents = f.read()
letters = len(fileContents)

print('WARNING: This will destroy all data in {}'.format(fileName))
response = input('Are you sure you want to continue? ')

if response.lower() == 'yes':
    for i in range(times):
        f.seek(0)
        print('Pass {}: Writing file with all {}\'s'.format(i + 1, chr(65 + i)))
        f.write('{}'.format(chr(65 + i) * letters))

f.close()
