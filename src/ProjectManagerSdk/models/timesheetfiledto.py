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
class TimesheetFileDto:
    """
    Represents information about a file attached to a Timesheet.
    """

    id: str | None = None
    """
    The identifier for this file
    """

    name: str | None = None
    """
    The name of the file
    """

    url: str | None = None
    """
    The url of the file which can be used for downloading
    """


