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


all:
	nix-shell ./_lectures/default.nix \
		--indirect --add-root .gcroots/dep \
		--run "make html"

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html

clean:
	rm -rf $(BUILDDIR)

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck

# vim:ft=make
#
