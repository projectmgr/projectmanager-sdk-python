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


from ProjectManagerSdk.models.nptassigneedto import NptAssigneeDto
from ProjectManagerSdk.models.nptstatusdto import NptStatusDto
from typing import List
import dataclasses

@dataclasses.dataclass
class NptDto:
    """
    A Npt is a task that does not belong to the project. It is only
    visible to the person who created it, and the users assigned to it.
    NPT's are a lightweight version of a project task.
    """

    id: str | None = None
    """
    The unique identifier of the NPT
    """

    name: str | None = None
    """
    The common name of this Task.
    """

    description: str | None = None
    """
    This field contains the task's "Note" or "Description", which is a
    description of the work to be done to complete the task. Within the
    ProjectManager application, you can use this field as follows: *
    When in the Board or List view, click on a task to open the task
    panel, then edit the "Description" field.
    """

    plannedStartDate: str | None = None
    """
    The date when work on this Task is planned to begin. This value
    contains only the date in year-month-day format. For display, this
    date will always be shown as this same year-month-day regardless of
    time zone.
    """

    plannedFinishDate: str | None = None
    """
    The date when work on this Task is expected to complete. This value
    contains only the date in year-month-day format. For display, this
    date will always be shown as this same year-month-day regardless of
    time zone.
    """

    actualEffort: int | None = None
    """
    The actual effort (in minutes) for this Task.
    """

    priorityId: int | None = None
    """
    Return the priority of a task
    """

    percentComplete: int | None = None
    """
    The numerical percentage, from 0-100, representing the percentage
    completion for this Task. Any numbers below zero or above 100 will
    be clamped to the minimum or maximum value. This value can be edited
    manually in the Gantt chart view of the application, or can be
    selected on the Task Detail page within the Kanban board.
    """

    status: NptStatusDto | None = None
    """
    The status assigned to this Npt
    """

    assignees: List[NptAssigneeDto] | None = None
    """
    The list of resources assigned to this Npt
    """


