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


from ProjectManagerSdk.models.timesheetadmintypedto import TimesheetAdminTypeDto
from ProjectManagerSdk.models.timesheetfiledto import TimesheetFileDto
from ProjectManagerSdk.models.timesheetprojectdto import TimeSheetProjectDto
from ProjectManagerSdk.models.timesheetresourcedto import TimesheetResourceDto
from ProjectManagerSdk.models.timesheettaskdto import TimesheetTaskDto
import dataclasses

@dataclasses.dataclass
class TimesheetDto:
    """
    Created Time entry response data
    """

    id: str | None = None
    """
    TimesheetId
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

    modifiedDate: str | None = None
    """
    Date and time (in UTC) that this timesheet entry was last modified.
    """

    task: TimesheetTaskDto | None = None
    """
    The task associated with this timesheet entry
    """

    project: TimeSheetProjectDto | None = None
    """
    The project associated with this timesheet entry
    """

    resource: TimesheetResourceDto | None = None
    """
    The resource associated with this timesheet entry
    """

    adminType: TimesheetAdminTypeDto | None = None
    """
    The administration type associated with this timesheet entry
    """

    files: list[TimesheetFileDto] | None = None
    """
    The list of files associated with this Timesheet, if any. This field
    will be present when you fetch a single object. When you query for
    multiple objects, this field is not included in results by default.
    To expand this field, specify the name of this field in the
    `$expand` parameter.
    """


