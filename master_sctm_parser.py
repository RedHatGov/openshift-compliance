import jinja2
import openpyxl
import os
import sys

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

# Build the sctm dict
sctm = {}
for row in ws.rows:
    r = {}
    i = 0
    for cell in row:
        r[column_index[i]] = cell.value
        i += 1

    r["Title"] = nt_map[r["NIST Ref #"]]
    # Generate the SCMT .rst for this row
    print template.generate(r)

