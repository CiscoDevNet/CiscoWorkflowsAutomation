import sys
import string
from urllib.parse import quote

encoded_string = quote(sys.argv[1])
print(encoded_string)