#
# ProjectManager API for Python
#
# (c) 2023-2023 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  2023-2023 ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#


from dataclasses import dataclass
from astroerror import AstroError
from typing import TypeVar, Generic

T = TypeVar('T')

@dataclass
class AstroResult(Generic[T]):
    """
    An API result that contains different values depending on whether
    the API call succeeded or failed. Use the `Success` value to
    determine if the API call succeeded. If the API call failed, you can
    examine the `Error` value to determine what went wrong.
    """

    error: AstroError | None = None
    """
    If the API call failed, this will contain information about the
    error that occurred.
    """

    success: bool | None = None
    """
    True if the API call succeeded; false otherwise.
    """

    hasError: bool | None = None
    """
    True if the API call failed.
    """

    statusCode: int | None = None
    """
    The HTTP code of the response.
    """

    data: T | None = None
    """
    If successful, the data that was returned by this API call
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
