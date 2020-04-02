import re

re.match(r'[a-z]+\d{2}', 'item01')

re.match(r'[a-zA-Z]+\s\w+', 'Pierre Dupont')

re.match(r'\s+', 'pierre dupont')

re.match(r'\w+', 'pierre dupont')

re.match(r'\w+([-+=]?)', 'pierre-dupont')

re.match(r'\w+([-+=]?)', 'pierre/dupont')

re.match(r'\w+([-+=]+)', 'pierre/dupont')
