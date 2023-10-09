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


from ProjectManagerSdk.models.timesheetprojectdto import TimeSheetProjectDto
from ProjectManagerSdk.models.timesheettaskdto import TimesheetTaskDto
from dataclasses import dataclass

@dataclass
class TimesheetGetResponseDto:
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

    task: TimesheetTaskDto | None = None
    """
    associated tasks with time sheet
    """

    project: TimeSheetProjectDto | None = None
    """
    associated projects with timesheet
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
