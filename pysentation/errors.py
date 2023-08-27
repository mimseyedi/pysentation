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
    This is the most general and parent of all pysentation related errors.
    """


class InterpretationError(PysentationError):
    """
    This is an interpretation error and it is the parent of all errors that are raised during file interpretation.
    """


class ScreenError(PysentationError):
    """
    This error refers to all errors related to screen.
    """


class ScopeDetectionError(InterpretationError):
    """
    This error occurs when the range or scope of the pysentation cannot be identified.
    """


class PropertyError(InterpretationError):
    """
    This error can be raised when there is a problem in reading and recognizing the properties.
    """


class CommentRenderingError(InterpretationError):
    """
    This error can be raised when there is a problem in rendering the comment. Like not closing style tags.
    """


class NotAPysentationFileError(PysentationError):
    """
    This error can be raised when the source path points to a non-pysentation file != (.py|.pysent).
    """
