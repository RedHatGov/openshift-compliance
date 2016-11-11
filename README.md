# openshift-compliance
OpenShift Compliance documentation

## ReStructuredText Primer

For help with ReStructuredText syntax, check out the [Quickstart Guide](http://docutils.sourceforge.net/docs/user/rst/quickstart.html).

This one is good too: [Sphinx reST Syntax](http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html).

## Getting started

To get started, install Sphinx and the RTD Python modules.

```
$ sudo pip install Sphinx
$ sudo pip install sphinx_rtd_theme
$ sudo pip install openpyxl
```

The master security control tracibility matrix (SCTM) is [master_sctm.xlsx](master_sctm.xlsx). It needs to be parsed by [master_sctm_parser.py](master_sctm_parser.py), which generates [controls.rst](controls.rst) via the [security_control.j2](security_control.j2) [Jinja2](http://jinja.pocoo.org/docs/dev/) template.

When you make the html target, this parsing happens automatically. If you want to explicitly parse the template, you can:

```
$ python master_sctm_parser.py master_sctm.xlsx
```

**Spreadsheet warnings**: 
* Do not edit this spreadsheet with LibreOffice Calc. It will break the spreadhseet and make it unparseable by ```openpyxl```. 
* The spreadsheet is filtered by FISMA High controls. If you change the filters the resultant .rst file will be different, too.

Once you have made changes to your docs, commit your changes. You can build the docs to view locally.

```
$ git add -A
$ git commit -am 'my commit message'
$ make html
```

Sanity check the output for errors. The docs can be viewed in the ```_biuld/html``` directory.

## Read the Docs

For the time being, this project is being distributed via [Read the Docs](http://readthedocs.org)

The main page is at [http://openshift-compliance-guide.readthedocs.io](http://openshift-compliance-guide.readthedocs.io/en/latest/index.html).

