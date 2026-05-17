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
    Task-level planned work (Astro.Api.Dto.Tasks.TaskTimeSummaryDto.TotalPlannedMinutes
    from task Work), per-resource assigned breakdown
    (Astro.Api.Dto.Tasks.TaskTimeSummaryDto.Assigned /
    Astro.Api.Dto.Tasks.TaskTimeSummaryDto.TotalAssignedMinutes), and
    reported timesheet time (Astro.Api.Dto.Tasks.TaskTimeSummaryDto.Actual).
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
    Sum of reported minutes across all resources in actual.
    """

    assigned: List[TaskPlannedResourceTimeDto] | None = None
    """
    Planned effort by resource, including per-day allocation breakdown
    where available.
    """

    actual: List[TaskActualResourceTimeDto] | None = None
    """
    Reported timesheet time by resource, including individual timesheet
    rows.
    """


