import jinja2
import openpyxl
import os
import sys

from collections import OrderedDict
from ntmap import *

# Get the path of this file
dir_path = os.path.dirname(os.path.realpath(__file__))

# Load the Jinja2 template
loader = jinja2.FileSystemLoader(dir_path)
environment = jinja2.Environment(loader=loader)
template = environment.get_template('security_control.j2')

# Open the SCTM Excel workbook
wb = openpyxl.load_workbook(sys.argv[1], read_only=True)
ws = wb['Matrix']

# Build the column index
column_index = {}
index_number = 0
for cell in ws.rows[0]:
    column_index[int(index_number)] = cell.value
    index_number += 1

# Init the sctm dict, keyed to control title
sctm = {}

# Iterate over every row in the sheet, starting at the 2nd row
for row in ws.rows[1:]:
    # Temporary dict for this iteration
    r = {}

    # Cell index
    i = 0

    # Iterate over the cells and insert the values into the temporary dict r
    # keyed with the column name.
    for cell in row:
        # If the cell is non-blank, insert the cell's contents into the temp
        # dict r keyed by column name.
        if cell.value and cell.value != '':
            r[column_index[i]] = cell.value
        else:
            r[column_index[i]] = 'undefined'
        i += 1

    # Build the control title with nice capitalization
    r["Title"] = " ".join(w.capitalize() for w in nt_map[r["NIST Ref #"]].split())

    # First we check to see if this control has been processed before
    req = ''
    if sctm.get(r['NIST Ref #']):
        # If it has, we concat the control language
        swap = sctm['NIST Ref #']['Requirements']
        req = swap + '\n' + r['Requirements']
    else:
        # Otherwise we start fresh
        req = r['Requirements']
    # Then we build a complete requirements value
    r['Original Requirements'] = req

    # Now we build a list of control parts and store it under the same key
    parts = []
    if sctm.get(r['NIST Ref #']):
        parts = sctm[r['NIST Ref #']]
        parts.append(r)
        sctm[r['NIST Ref #']] = parts
    else:
        sctm['NIST Ref #'] = [r]

sctm_keys = sorted(sctm.keys())
for key in sctm_keys:
    control = sctm[key]
    print template.render(key)

