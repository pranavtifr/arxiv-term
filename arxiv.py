#! /usr/bin/env python
import urllib
import requests
import argparse
fieldname = None
typesname = None
parser = argparse.ArgumentParser()
field = parser.add_mutually_exclusive_group(required=True)
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

args = parser.parse_args()
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


url = "https://arxiv.org/list/"+fieldname+typesname
#f = urllib.urlopen(url)
f = urllib.request.urlopen(url)
s=str(f.read())

def getabs(s):
    titlestart = s.find('<span class="descriptor">Title:</span>')
    if titlestart == -1:
        return None,0
    title = s[titlestart+37:s.find('</div>',titlestart+1)]
    return title,titlestart+3

i = 1
while True:
    url,endlink = getabs(s)
    if url == None:
        print("End of Page")
        break
    print(i,url)
    i = i + 1
    s=s[endlink:]
