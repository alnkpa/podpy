#!/usr/bin/env python

from setuptools import setup
from version import get_git_version

setup(name="podpy",
      version=get_git_version(),
      description="""podpy is a simple small-footprint podcatcher planned to
 be expanded to be a full-fledged podcast client""",
      entry_points = {
            'gui_scripts': [
                  'podpy = podpyclient.script:start'
            ]
      },
      author="Patrick Schmidt",
      author_email="me@paschmidt.de",
      url="https://github.com/alnkpa/podpy",
      packages=["podpyclient"],
      install_requires=["libtorrent",
                        "feedparser",
                        "PySide",
                        "PyYAML"],
      provides=["podpyclient"],
     # scripts=["podpy"],
      license="MPL",
      download_url="https://github.com/alnkpa/podpy/archive/master.zip",
      classifiers=["Development Status :: 3 - Alpha",
                   "Environment :: X11 Applications :: Qt",
                   "Intended Audience :: End Users/Desktop",
                   "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
                   "Natural Language :: English",
                   "Programming Language :: Python",
                   "Operating System :: OS Independent",
                   "Topic :: Communications :: File Sharing",
                   "Topic :: Internet",
                   "Topic :: Multimedia :: Sound/Audio"
                   ]
      )
