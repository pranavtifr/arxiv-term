#! /usr/bin/env python
import sys
import urllib

if sys.version_info[0] < 3:
    import urllib2
else:
    import requests
import argparse
from subprocess import call

def downpaper(down): #Code for Downloading the Paper with the corresponding ID
    downurl = 'https://arxiv.org/pdf/' + down 
    print(downurl)
    call(["wget","-U firefox","-nc",downurl])

def getpage(url): #Fetch the Entire page as a string
    f=None
    if sys.version_info[0] < 3:
        f = urllib2.urlopen(url)
    else:
        f = urllib.request.urlopen(url)
    s=str(f.read())
    return s

class Paper():
    def __init__(self):
        self.title = None
        self.author = None
        self.abstract = None
        self.ID = None


    def setID(self,idd):
        self.ID = idd

    def gettitle(self):
        return self.title

    def getID(self):
        return self.ID

    def setinfo(self,s):
        titlestart = s.find('<span class="descriptor">Title:</span>')
        IDstart=s[:titlestart].rfind('title="Abstract">arXiv:')
        self.ID = s[IDstart+ 23:s.find('</a>',IDstart)]
        if titlestart == -1:
            return titlestart
        self.title = s[titlestart+37:s.find('</div>',titlestart+1)]
        return titlestart

    def setabs(self):
        paperpage = getpage("https://arxiv.org/abs/"+self.ID)
        if self.title == None:
            titlestart = paperpage.find('<span class="descriptor">Title:</span>')
            self.title = paperpage[titlestart+40:paperpage.find('</h1>',titlestart+1)]
        absstart = paperpage.find('<span class="descriptor">Abstract:</span> ')
        self.abstract = paperpage[absstart+41:paperpage.find('</blockquote>',absstart)]

    def display(self):
        print(self.title)
        print(self.ID)
        print(self.abstract)

    def download(self):
        downpaper(self.ID)
        
    def view(self):
        self.setabs()
        self.display()
        try:
            dload = raw_input("Download this paper (y/N)? ")
        except:
            dload = input("Download this paper (y/N)? ")

        if dload == 'y':
            self.download()

def getpaper(s):
    paperobj = Paper()
    titlestart = paperobj.setinfo(s)
    return paperobj,titlestart+3

fieldname = None
typesname = None
parser = argparse.ArgumentParser()
field = parser.add_mutually_exclusive_group()
field.add_argument("--astro_ph", help="High Energy Physics Theory", action="store_true")
field.add_argument("--cond_mat", help="Condensed Matter Physics", action="store_true")
field.add_argument("--gr_qc", help="General Relativity and Cosmology", action="store_true")
field.add_argument("--hep_ex", help="High Energy Physics Experiment", action="store_true")
field.add_argument("--hep_lat", help="High Energy Physics Lattice", action="store_true")
field.add_argument("--hep_ph", help="High Energy Physics Phenomenology", action="store_true")
field.add_argument("--hep_th", help="High Energy Physics Theory", action="store_true")

types = parser.add_mutually_exclusive_group()
types.add_argument("--new", help="From /<department>/new", action="store_true")
types.add_argument("--recent", help="From /<department>/recent", action="store_true")

parser.add_argument("-r","--replacement", help="Include Replacement papers in new", action="store_true")
parser.add_argument("-d","--download",help="Download the pdf of the given arxiv ID",type=str)
parser.add_argument("-v","--view",help="View the details of the given arxiv ID",type=str)
args = parser.parse_args()
if args.download:
    downpaper(args.download)
    exit(0)

if args.view:
    pap = Paper()
    pap.setID(args.view)
    pap.view()
    exit(0)

if args.astro_ph:
    fieldname = 'astro-ph'
if args.cond_mat:
    fieldname = 'cond-mat'
if args.gr_qc:
    fieldname = 'gr-qc'
if args.hep_ex:
    fieldname = 'hep-ex'
if args.hep_lat:
    fieldname = 'hep-lat'
if args.hep_ph:
    fieldname = 'hep-ph'
if args.hep_th:
    fieldname = 'hep-th'

if args.new:
    typesname = '/new'
if args.recent:
    typesname = '/recent'

if fieldname == None or typesname == None :
    print('Please enter the Arguments')
    print('Use -h flag for details')
    exit(0)

url = "https://arxiv.org/list/"+fieldname+typesname
s = getpage(url)

if not args.replacement:
    temp = s[:s.find('<h3>Replacements')]
    s = temp

i = 1
papercoll = []
while True:
    paper,endlink = getpaper(s)
    if paper.gettitle() == None:
        break
    papercoll.append(paper)
    print(i,paper.gettitle(),paper.getID())
    i = i + 1
    s=s[endlink:]
try:
    try:
        choice = int(raw_input("Choose a Paper (Invalid Numbers or strings exit the program) "))
    except:
        choice = int(input("Choose a Paper (Invalid Numbers or strings exit the program) "))
except ValueError:
    exit(0)

if choice - 1 > len(papercoll):
    exit(0)
papercoll[choice -1].view()
