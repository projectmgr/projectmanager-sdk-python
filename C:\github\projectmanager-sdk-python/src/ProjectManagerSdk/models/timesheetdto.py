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
from typing import List
import dataclasses

@dataclasses.dataclass
class TimesheetDto:
    """
    A Timesheet entry is a single record that contains information about
    time spent by a person on a task. Each Timesheet entry object
    contains information about one task/day/person combination. A fully
    completed Timesheet will often contain multiple records for the same
    date range which must be combined to produce a finished Timesheet.
    """

    id: str | None = None
    """
    A unique identifier of a timesheet data entry
    """

    resourceId: str | None = None
    """
    The unique identifier of the resource who is preparing this
    Timesheet. You can filter on this value to measure the total work
    performed by this specific Resource.
    """

    taskId: str | None = None
    """
    The unique identifier of the task worked on for this Timesheet. You
    can filter on this value to measure the total work performed against
    a specific Task.
    """

    projectId: str | None = None
    """
    The unique identifier of the project worked on for this Timesheet.
    You can filter on this value to measure the total work performed
    against a specific Project.
    """

    date: str | None = None
    """
    The date of this time entry record. You can filter on this value to
    obtain Timesheet data for a specific date range.
    """

    notes: str | None = None
    """
    Notes associated with this Timesheet, if any
    """

    approved: bool | None = None
    """
    True if this Timesheet was approved by a person with the role of a
    Timesheet approver
    """

    hours: float | None = None
    """
    Total Hours spent on this Task by this Resource on this specific
    Date
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

    files: List[TimesheetFileDto] | None = None
    """
    The list of files associated with this Timesheet, if any. This field
    will be present when you fetch a single object. When you query for
    multiple objects, this field is not included in results by default.
    To expand this field, specify the name of this field in the
    `$expand` parameter.
    """


