"""
██████╗ ██╗   ██╗███████╗███████╗███╗   ██╗████████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝██╔════╝██╔════╝████╗  ██║╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
██████╔╝ ╚████╔╝ ███████╗█████╗  ██╔██╗ ██║   ██║   ███████║   ██║   ██║██║   ██║██╔██╗ ██║
██╔═══╝   ╚██╔╝  ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
██║        ██║   ███████║███████╗██║ ╚████║   ██║   ██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝        ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

pysentation Github repository: https://github.com/mimseyedi/pysentation
"""


class PysentationError(Exception):
    """
    This error refers to all errors in pysentation and is the superclass of all errors.
    """


class PysentationScreenError(PysentationError):
    """
    This error refers to all errors related to screen.
    """


class PysentationSlideError(PysentationError):
    """
    This error refers to all errors related to slides.
    """


class PysentationPropertyError(PysentationSlideError):
    """
    This error can be raised when there is a problem in reading and recognizing the properties.
    """


class PysentationInitError(PysentationSlideError):
    """
    This error can be raised when the initial setup steps to detect the pysentation range have a problem and the range is not recognized.
    """


class PysentationScopeRangeError(PysentationSlideError):
    """
    This error can be raised when the end of the pysentation range is incorrectly specified or not defined.
    """


class PysentationCommentError(PysentationSlideError):
    """
    This error can be raised when there is a problem in rendering the comment. Like not closing style tags.
    """


class PysentationFileNotFoundError(PysentationError):
    """
    This error can be raised when the source file does not exist in the entered path.
    """


class PysentationIsADirectoryError(PysentationError):
    """
    This error can be raised when the source path is a directory, not a file.
    """


class PysentationNotAPythonFileError(PysentationError):
    """
    This error can be raised when the source path points to a non-Python file.
    """


class PysentationEmptyScreenError(PysentationScreenError):
    """
    This error can be raised when the object created from PysentationScreen is empty of slides.
    """
