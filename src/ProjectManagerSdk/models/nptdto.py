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
from ProjectManagerSdk.models.taskownerdto import TaskOwnerDto
from ProjectManagerSdk.models.tasktagdto import TaskTagDto
from ProjectManagerSdk.models.tasktododto import TaskTodoDto
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

    actualStartDate: str | None = None
    """
    If set, this is the actual date when work began on the Task. This
    value contains only the date in year-month-day format. For display,
    this date will always be shown as this same year-month-day
    regardless of time zone. For reporting purposes, this date is
    calculated against the official time zone of the Workspace. For
    example: A Task has a planned completion date of July 5, 2023 in a
    Workspace that has a time zone of US Pacific Time (GMT-7 or GMT-8,
    depending on daylight savings time). This project is considered
    overdue on 12:01 AM July 6th 2023 in US Pacific time.
    """

    actualFinishDate: str | None = None
    """
    If set, this is the actual date when work was completed on this
    Task. This value contains only the date in year-month-day format.
    For display, this date will always be shown as this same
    year-month-day regardless of time zone. For reporting purposes, this
    date is calculated against the official time zone of the Workspace.
    For example: A Task has a planned completion date of July 5, 2023 in
    a Workspace that has a time zone of US Pacific Time (GMT-7 or GMT-8,
    depending on daylight savings time). This project is considered
    overdue on 12:01 AM July 6th 2023 in US Pacific time.
    """

    actualEffort: int | None = None
    """
    The actual effort (in minutes) for this Task.
    """

    actualDuration: int | None = None
    """
    The actual duration (in minutes) for this Task.
    """

    actualCost: float | None = None
    """
    The actual cost of this Task to date, if known.
    """

    plannedCost: float | None = None
    """
    The planned cost for this Task. Cannot be negative.
    """

    plannedDuration: int | None = None
    """
    The planned duration (in minutes) for this Task.
    """

    plannedEffort: int | None = None
    """
    The planned effort (in minutes) for this Task.
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

    shortId: str | None = None
    """
    A short ID that can be used to refer to this Task. This short ID is
    guaranteed to be unique within your Workspace.
    """

    tags: List[TaskTagDto] | None = None
    """
    The TaskTags that apply to this Task.
    """

    todos: List[TaskTodoDto] | None = None
    """
    A list of TaskTodo items, which are sub-tasks within this Task.
    """

    createDate: str | None = None
    """
    Timestamp when the NPT was created
    """

    owner: TaskOwnerDto | None = None
    """
    The owner of this Task.
    """

    ownerId: str | None = None
    """
    The ownerId of this Task.
    """


