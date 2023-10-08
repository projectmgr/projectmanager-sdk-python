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

@dataclass
class AstroResult:
    """
    An API result that contains different values depending on whether
    the API call succeeded or failed. Use the `Success` value to
    determine if the API call succeeded. If the API call failed, you can
    examine the `Error` value to determine what went wrong.
    """

    error: object | None = None
    success: object | None = None
    hasError: object | None = None
    statusCode: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
