Basic template for python projects.

Version and some other information is pulled from git, so makefile won't work
if you are not in a git repo. Build targets (make rpm, make deb, etc) Require at least
one git tag to have been created.

There are sample rpm spec and debian control files, as well as init scripts, and other tidbits.


Makefile for someproject, currently supports deb and rpm 
 builds from current source tree.


Usage: make <target>
Available targets are:
	deb			Create deb
	sources			Create tarball
	srpm			Create srpm
	rpm			Create rpm
	clean			Remove work dir
	check			Build all the things, then clean them up

