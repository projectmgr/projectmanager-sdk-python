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
class TimesheetResponseDto:
    """
    Time entry representation
    """

    id: str | None = None
    """
    TimesheetId
    """

    taskId: str | None = None
    """
    associated task id
    """

    projectId: str | None = None
    """
    associated project id
    """

    resourceId: str | None = None
    """
    resource id time entry entered
    """

    timesheetAdminTypeId: str | None = None
    """
    admin task id
    """

    date: str | None = None
    """
    Date of time entry
    """

    notes: str | None = None
    """
    Notes
    """

    approved: bool | None = None
    """
    Shows if timesheet approved
    """

    hours: float | None = None
    """
    Total Hours
    """


