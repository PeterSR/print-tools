class BaseLayoutError(Exception):
    """Base class for all layout-related errors."""

    pass


class InsufficientContainersError(BaseLayoutError):
    """Raised when there are not enough containers to fit the boxes."""

    def __init__(self, message: str):
        super().__init__(message)
