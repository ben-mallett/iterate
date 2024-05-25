from enum import Enum

class VersionType(Enum):
    MAJOR = 1
    MINOR = 2
    PATCH = 3

class Version:
    """
    Represents a semantic version.

    Members:
        major : int : major version number
        minor : int : minor version number
        patch : int : patch version number
    """
    major: int = 0
    minor: int = 0
    patch: int = 0

    def __init__(self, major: int = 0, minor: int = 0, patch: int = 0):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self):
        return f'v{self.major}.{self.minor}.{self.patch}'

    def incrementVersion(self, versionType: VersionType = VersionType.PATCH):
        """
        Increments the version based on the version type

        Params:
            versionType : VersionType : supported version type to increment
        """
        if versionType == VersionType.MAJOR:
            self.major += 1
        elif versionType == VersionType.MINOR:
            self.minor += 1
        elif versionType == VersionType.PATCH:
            self.patch += 1