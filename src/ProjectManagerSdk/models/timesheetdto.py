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


from ProjectManagerSdk.models.timesheetadmintypedto import TimesheetAdminTypeDto
from ProjectManagerSdk.models.timesheetprojectdto import TimeSheetProjectDto
from ProjectManagerSdk.models.timesheetresourcedto import TimesheetResourceDto
from ProjectManagerSdk.models.timesheettaskdto import TimesheetTaskDto
from dataclasses import dataclass

@dataclass
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


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
