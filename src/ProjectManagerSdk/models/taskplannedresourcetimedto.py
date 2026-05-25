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


from ProjectManagerSdk.models.taskplannedallocationdto import TaskPlannedAllocationDto
from typing import List
import dataclasses

@dataclasses.dataclass
class TaskPlannedResourceTimeDto:
    """
    Planned time for one resource assigned to the task.
    """

    id: str | None = None
    """
    Resource identifier for this planned row.
    """

    totalMinutes: int | None = None
    """
    Total planned minutes for this resource (sum of allocations when
    broken down by day).
    """

    allocations: List[TaskPlannedAllocationDto] | None = None
    """
    Planned minutes grouped by calendar date for this resource.
    """


