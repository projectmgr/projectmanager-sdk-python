#
# ProjectManager API for Python
#
# (c) 2023-2024 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  2023-2024 ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#


from typing import List
import dataclasses

@dataclasses.dataclass
class UserError:
    """
    Represents an individual error for a specific Resource that could
    not be created in the context of a bulk Resource creation API call.
    """

    email: str | None = None
    """
    The email of the Resource that could not be created
    """

    reason: str | None = None
    """
    A description of the reason this Resource could not be created
    """

    statusCode: int | None = None
    """
    A status code explaining the category of reason this Resource could
    not be created
    """


