#!/usr/bin/env python

from distutils.core import setup

setup(name="podpy",
      version="0.1.1",
      description="""podpy is a simple small-footprint podcatcher planned to
to be expanded to be a full-fledged podcast client""",
      author="Patrick Schmidt",
      author_email="patrick@alnkpa.de",
      url="https://github.com/alnkpa/podpy",
      packages=["podpyclient"],
      requires=["libtorrent", "feedparser"],
      scripts=["podpy"],
      download_url="https://github.com/alnkpa/podpy/archive/master.zip",
      classifiers=["Development Status :: 2 - Pre-Alpha",
                   "Environment :: Console :: Curses",
                   "Intended Audience :: End Users/Desktop",
                   "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
                   "Natural Language :: English",
                   "Programming Language :: Python",
                   "Topic :: Communications :: File Sharing",
                   "Topic :: Internet",
                   "Topic :: Multimedia :: Sound/Audio"
                   ]
      )
