from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys



try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "/data/contacts.json"

for o, a in opts:
    if o == "-n":
        n=int(a)
    elif o== "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ' '
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))

testdata = [Contact(first_name=first_name, last_name=last_name, mobile_phone=mobile_phone, email_1=email_1)
    for first_name in ['', random_string("first_name_", 5)]
    for last_name in ['', random_string("last_name_", 5)]
    for mobile_phone in ['', random_string("", 10)]
    for email_1 in ['', random_string("email@test.", 4)]
    ]


#file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

file = os.path.split(os.path.dirname( __file__ ))[0]+f

with open(file, 'w') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
