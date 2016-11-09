# openshift-compliance
OpenShift Compliance documentation

## ReStructuredText Primer

For help with ReStructuredText syntax, check out the [Quickstart Guide](http://docutils.sourceforge.net/docs/user/rst/quickstart.html).

## Getting started

To get started, install Sphinx and the RTD Python modules.

```
$ sudo pip install Sphinx
$ sudo pip install sphinx_rtd_theme
```

Once you have made changes to your docs, commit your changes. You can build
the docs to view locally.

```
$ git add -A
$ git commit -am 'my commit message'
$ make html
```

Sanity check the output for errors. The docs can be viewed in the ```_biuld/html``` directory.

## Read the Docs

For the time being, this project is being distributed via [Read the Docs](http://readthedocs.org)

The main page is at [http://openshift-compliance-guide.readthedocs.io](http://openshift-compliance-guide.readthedocs.io/en/latest/index.html).

