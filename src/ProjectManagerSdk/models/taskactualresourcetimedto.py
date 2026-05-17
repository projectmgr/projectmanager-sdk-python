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


from ProjectManagerSdk.models.taskactualtimeentrydto import TaskActualTimeEntryDto
from typing import List
import dataclasses

@dataclasses.dataclass
class TaskActualResourceTimeDto:
    """
    Reported (timesheet) time for one resource on the task.
    """

    id: str | None = None
    """
    Resource identifier for this actual row.
    """

    totalMinutes: int | None = None
    """
    Total reported minutes for this resource (sum of
    Astro.Api.Dto.Tasks.TaskActualResourceTimeDto.TimeEntries).
    """

    timeEntries: List[TaskActualTimeEntryDto] | None = None
    """
    Individual timesheet entries contributing to totalMinutes.
    """


