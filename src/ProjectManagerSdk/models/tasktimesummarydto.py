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


from ProjectManagerSdk.models.taskactualresourcetimedto import TaskActualResourceTimeDto
from ProjectManagerSdk.models.taskplannedresourcetimedto import TaskPlannedResourceTimeDto
from typing import List
import dataclasses

@dataclasses.dataclass
class TaskTimeSummaryDto:
    """
    Task-level planned work (TotalPlannedMinutes from task Work),
    per-resource assigned breakdown (Assigned / TotalAssignedMinutes),
    workspace-wide reported actual total (TotalActualMinutes),
    per-resource reported timesheet rows (Actual), scoped by permission,
    and HasTimeEntries (whether any logged minutes exist for the task in
    the workspace, regardless of Actual visibility).
    """

    totalPlannedMinutes: int | None = None
    """
    The task's planned work (Work), in minutes — same as the Gantt
    "Work" / planned effort on the task.
    """

    totalAssignedMinutes: int | None = None
    """
    Sum of minutes assigned (per-resource assigned/planned effort from
    allocations or assignment split).
    """

    totalActualMinutes: int | None = None
    """
    Sum of reported minutes on this task from all resources in the
    workspace (same merge as internal totals: direct task id, original
    task id, and weekly timesheet-task links). This is not limited to
    the caller's own entries.
    """

    hasTimeEntries: bool | None = None
    """
    True when at least one timesheet row for this task has non-zero
    reported minutes in the workspace (same merge as
    Astro.Api.Dto.Tasks.TaskTimeSummaryDto.TotalActualMinutes). False
    when there are none. Unlike Astro.Api.Dto.Tasks.TaskTimeSummaryDto.Actual,
    this does not depend on whether the caller can see other resources'
    entries.
    """

    assigned: List[TaskPlannedResourceTimeDto] | None = None
    """
    Planned effort by resource, including per-day allocation breakdown
    where available.
    """

    actual: List[TaskActualResourceTimeDto] | None = None
    """
    Reported timesheet time by resource, including individual timesheet
    rows. Callers with edit-all-projects or edit-team-timesheets
    workspace permission see every resource returned by secured
    timesheet queries; otherwise only the caller's own timesheet rows
    (same idea as the Edit all timesheets / team timesheet capability in
    roles).
    """


