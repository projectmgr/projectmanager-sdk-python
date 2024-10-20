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
class TimesheetCreateRequestDto:
    """
    Payload to create time entry
    """

    date: str | None = None
    """
    Time entry date
    """

    hours: float | None = None
    """
    Reported hours
    """

    taskId: str | None = None
    """
    Task id that time reported to
    """

    adminTypeId: str | None = None
    """
    Admin task id that time reported to
    """

    resourceId: str | None = None
    """
    Resource id that time reported to
    """

    notes: str | None = None
    """
    Notes
    """


