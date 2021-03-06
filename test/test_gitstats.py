from __future__ import with_statement
import unittest
import gitstats
import tempfile
import shutil
from itertools import repeat
from gitstats import GitStats

TEST_REPOS = list(repeat('.', 8))

class GitStatsTest(unittest.TestCase):
    def setUp(self):
        self.stats = GitStats()
        self.sourcedirs = TEST_REPOS
        self.destdir = tempfile.mkdtemp()

    def test_selfcheck(self):
        self.stats.run(self.sourcedirs + [self.destdir])

    def tearDown(self):
        # Change to self.sourcedirs and behold!
        shutil.rmtree(self.destdir)


if __name__ == '__main__':
    unittest.runtests()
