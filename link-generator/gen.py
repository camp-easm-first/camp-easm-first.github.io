import random
import string
import os

HTMLTEMPLATE = """
<html>
 <head>
   <title>Disobey workshop example data</title>
 </head>
 <body>
 Nothing to {} here
 </body>
</html>
"""

BASEHTML = """
<html>
 <head>
    <title>Totally sane link list</title>
 </head>
 <body>
 {}
 </body>
</html>
"""


TOTAL = 200

baseurls = ["thisisfine.okyoufoundme.com", "notonfire.okyoufoundme.com"]

outputdir = "outputdir"

with open('kaikkisanat.txt','r') as fh:
    data = fh.readlines()


def rndkey():
    return ''.join(random.choice(string.ascii_uppercase) for i in range(20))

def rndword(d):
    return random.choice(d).replace(" ","")

def rndurl(bu):
    return random.choice(bu)

i=0
links = []
while i<TOTAL:
    rndpath = "{}-{}-{}".format(rndword(data).strip(), rndword(data).strip(), rndword(data).strip())
    newurl = "https://{}/{}/".format(rndurl(baseurls), rndpath)
    links.append("<a href='{}'>{}</a><br />".format(newurl, newurl))
    newdir = "{}/{}".format(outputdir, rndpath)
    newfile = "{}/index.html".format(newdir)
    os.makedirs(newdir)
    with open(newfile, 'w') as fh:
        fh.write(HTMLTEMPLATE.format(rndkey()))
    i += 1

with open(outputdir+"/index.html", 'w') as fh:
    fh.write(BASEHTML.format('\n'.join(links)))



