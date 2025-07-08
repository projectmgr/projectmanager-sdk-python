#
# ProjectManager API for Python
#
# (c) ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#


from ProjectManagerSdk.models.timesheetfileresponsedto import TimesheetFileResponseDto
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

    minutes: int | None = None
    """
    Total Minutes
    """

    isCopied: bool | None = None
    """
    Is the timesheet entry copied from another week?
    """

    lastUpdatedDate: str | None = None
    """
    Is the last timesheet modified by the user
    """

    documents: List[TimesheetFileResponseDto] | None = None
    """
    Document Details
    """


