Basic template for python projects.

someproject
├── LICENSE   (GPL2 by default)
├── Makefile  (Has make targets for source, rpm, srpm packages, deb
├── packaging
│   ├── authors.sh
│   ├── deb  Working using equivs, will likely move that to debtools soon
│   └── rpm
│       └── someproject.spec
├── README.md
└── src
    └── someproject.py  The project

Version and some other information is pulled from git, so makefile won't work
if you are not in a git repo. Build targets (make rpm, make deb, etc) Require at least
on git tag to have been created. Might work on that later.
