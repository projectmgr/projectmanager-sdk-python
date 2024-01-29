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


from ProjectManagerSdk.models.astroerror import AstroError
from requests.models import Response
from dataclasses import dataclass
from typing import TypeVar, Generic
import dacite
import json

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
    If this API call was successful, contains the results.
    """

    def __init__(self, error: AstroError | None, success: bool | None, hasError: bool | None, statusCode: int | None, data: T | None):
        self.error = error
        self.success = success
        self.hasError = hasError
        self.statusCode = statusCode
        self.data = data

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
    
    def load_error(self, result: Response):
        self.error = dacite.from_dict(data_class=AstroError, data=json.loads(result.content)['error'])
