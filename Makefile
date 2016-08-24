#
# Makefile
# uralbash, 2016-08-24 10:13
#

SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = build
SOURCEDIR     = docs
ALLSPHINXOPTS = -d $(BUILDDIR)/doctrees $(SPHINXOPTS) $(SOURCEDIR)

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html

clean:
	rm -rf $(BUILDDIR)


# vim:ft=make
#
