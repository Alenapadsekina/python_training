from model.group import Group
import random
import string
import os.path
import jsonpickle
import getopt
import sys



try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "\data\groups.json"
print(f)
for o, a in opts:
    if o == "-n":
        n=int(a)
    elif o== "-f":
        f = a
print(f)
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ' '
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("NAME_", 10), header=random_string("header_", 10), footer=random_string("footer_", 10))
    for i in range(5)
    ]
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file = root+f

with open(file, 'w') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
