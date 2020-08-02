# Read a web text file, extracts integers, sum and print with a single line

import re, requests

print(sum([int(i) for i in re.findall('[0-9]+',requests.get("http://py4e-data.dr-chuck.net/regex_sum_42.txt").text)]))
