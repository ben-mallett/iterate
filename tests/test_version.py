import unittest
from src.version import Version, VersionType

class TestVersion(unittest.TestCase):
    def test_IncrementVersion(self):
        # test fresh version is v0.0.0
        vZero: Version = Version()
        self.assertEqual(vZero.major, 0)
        self.assertEqual(vZero.minor, 0)
        self.assertEqual(vZero.patch, 0)

        # test incrementing patch only increments patch
        vZero.incrementVersion()
        self.assertEqual(vZero.major, 0)
        self.assertEqual(vZero.minor, 0)
        self.assertEqual(vZero.patch, 1)

        # test incrementing minor only increments minor
        vZero.incrementVersion(VersionType.MINOR)
        self.assertEqual(vZero.major, 0)
        self.assertEqual(vZero.minor, 1)
        self.assertEqual(vZero.patch, 1)

        # test incrementing major only increments major
        vZero.incrementVersion(VersionType.MAJOR)
        self.assertEqual(vZero.major, 1)
        self.assertEqual(vZero.minor, 1)
        self.assertEqual(vZero.patch, 1)

    def test_ToString(self):
        # tests full major, minor, patch versions
        v2_3_4 = Version(2, 3, 4)
        self.assertEqual('v2.3.4', str(v2_3_4))

        # tests empty version
        v0 = Version()
        self.assertEqual('v0.0.0', str(v0))

    def failingTest(self):
        self.assertEqual(1, 0)

if __name__ == '__main__':
    unittest.main()