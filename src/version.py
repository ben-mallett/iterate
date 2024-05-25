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

    def incrementVersion(self, versionType: VersionType):
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

def getVersionFromFilepath(filepath: str):
    """
    Gets the current version of the resource at the given filepath

    Params:
        filepath : str : path to resource to get version of

    Returns:
        version : Version : version object of requested resource

    Raises:
        error : FileNotFoundError : file not found error if resource does not exist in filesystem
    """
    filesystemMock = {
        "some/path/to/models/model.py": Version(1, 0, 0),
        "some/path/to/models/upgraded.py": Version(1, 1, 0),
        "some/path/to/models/downgraded.py": Version(0, 9, 9),
        "some/path/to/models/initial.py": Version(),
    }
    if filepath in filesystemMock:
        return filesystemMock[filepath]
    else:
        raise FileNotFoundError("Could not find file")
    

def incrementVersionOfResource(filepath: str, versionType: VersionType = VersionType.PATCH):
    """
    Increments the given version type of version associated with the given filepath 

    Params:
        filepath : str : filepath of resource to increment
        versionType : VersionType : suppported version type from VersionType - defaults to patch

    Raises:
        error : FileNotFoundError : File not found error if resource cannot be located
    """
    try:
        version = getVersionFromFilepath(filepath)
        version.incrementVersion(versionType)
    except FileNotFoundError as error:
        print(f'File not found {filepath}')
        raise error