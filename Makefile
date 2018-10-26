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

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck

test:
	rstcheck \
		`find . -not -path "./.env/*" -name "*.rst" -printf "%p "` \
		--ignore-roles github,l,man --ignore-language bash --report 2

# vim:ft=make
#
