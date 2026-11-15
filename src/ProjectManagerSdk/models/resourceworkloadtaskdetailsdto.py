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


from ProjectManagerSdk.models.taskstatusdto import TaskStatusDto
from ProjectManagerSdk.models.tasktagdto import TaskTagDto
from typing import List
import dataclasses

@dataclasses.dataclass
class ResourceWorkloadTaskDetailsDto:
    """
    Basic details of the Task a workload entry belongs to. Only
    populated when the request specifies `include=task`.
    """

    id: str | None = None
    """
    The unique identifier of the Task.
    """

    projectId: str | None = None
    """
    The unique identifier of the Project this Task belongs to.
    """

    name: str | None = None
    """
    The name of the Task.
    """

    description: str | None = None
    """
    The Task's description, in markdown format.
    """

    percentComplete: int | None = None
    """
    The percentage of the task duration completed.
    """

    plannedStartDate: str | None = None
    """
    The planned start date of the Task.
    """

    plannedFinishDate: str | None = None
    """
    The planned finish date of the Task.
    """

    actualStartDate: str | None = None
    """
    The actual start date of the Task.
    """

    actualFinishDate: str | None = None
    """
    The actual finish date of the Task.
    """

    status: TaskStatusDto | None = None
    """
    The Task's current status (board column).
    """

    tags: List[TaskTagDto] | None = None
    """
    The TaskTags that apply to this Task.
    """


