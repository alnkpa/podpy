#!/usr/bin/env python

from setuptools import setup
from version import get_git_version

setup(name="podpy",
      version=get_git_version(),
      description="""podpy is a simple small-footprint podcatcher planned to
 be expanded to be a full-fledged podcast client""",
      author="Patrick Schmidt",
      author_email="patrick@alnkpa.de",
      url="https://github.com/alnkpa/podpy",
      packages=["podpyclient"],
      install_requires=["libtorrent", "feedparser"],
      provides=["pypodclient"],
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
