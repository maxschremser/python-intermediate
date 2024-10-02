#!/usr/bin/env python3
import urllib.request
import sys
import xml.etree.ElementTree as ET

format = "xml" # "json"
if len(sys.argv) != 3:
    raise SystemExit("Usage: busstop.py route stopid")
key = "b4RaaARiWi7H7QeGr3wD7B82E"
route = sys.argv[1]
stopid = sys.argv[2]
u = urllib.request.urlopen(f"http://ctabustracker.com/bustime/api/v3/gettime?key={key}&format={format}&stop={stopid}&route={route}")
data = u.read()
print(data)
doc = ET.fromstring(data)
print(str(doc))
for pt in doc.findall('.//tm'):
    print(pt.text)