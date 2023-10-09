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


from ProjectManagerSdk.models.taskassigneedto import TaskAssigneeDto
from ProjectManagerSdk.models.taskprojectdto import TaskProjectDto
from ProjectManagerSdk.models.taskstatusdto import TaskStatusDto
from ProjectManagerSdk.models.tasktagdto import TaskTagDto
from ProjectManagerSdk.models.tasktododto import TaskTodoDto
from dataclasses import dataclass

@dataclass
class TaskDetailsDto:
    """
    A Task is an individual element of work that must be performed to
    complete a Project. A Task can have one or more Resources assigned
    to it. Tasks can be linked to other Tasks to indicate whether they
    have a dependency or a connection.
    """

    id: str | None = None
    """
    The unique identifier of this Task.
    """

    project: TaskProjectDto | None = None
    """
    The Project to which this Task belongs.
    """

    tags: list[TaskTagDto] | None = None
    """
    The TaskTags that apply to this Task.
    """

    assignees: list[TaskAssigneeDto] | None = None
    """
    The list of assignees who are to work on this Task, if any.
    """

    todos: list[TaskTodoDto] | None = None
    """
    A list of TaskTodo items, which are sub-tasks within this Task.
    """

    shortId: str | None = None
    """
    A short ID that can be used to refer to this Task. This short ID is
    guaranteed to be unique within your Workspace.
    """

    name: str | None = None
    """
    The common name of this Task.
    """

    description: str | None = None
    """
    A description of the work to be performed in this Task.
    """

    status: TaskStatusDto | None = None
    """
    The TaskStatus assigned to this Task.
    """

    priorityId: int | None = None
    """
    The unique identifier of the TaskPriority
    """

    plannedStartDate: str | None = None
    """
    The date when work on this Task is planned to begin.
    """

    plannedFinishDate: str | None = None
    """
    The date when work on this Task is expected to complete.
    """

    actualStartDate: str | None = None
    """
    If set, this is the actual date when work began on the Task.
    """

    actualFinishDate: str | None = None
    """
    If set, this is the actual date when work was completed on this
    Task.
    """

    modifyDate: str | None = None
    """
    The timestamp in UTC when this Task was most recently modified.
    """

    createDate: str | None = None
    """
    The timestamp in UTC when this Task was created.
    """

    percentComplete: int | None = None
    """
    The numerical percentage, from 0-100, representing the percentage
    completion for this Task. Any numbers below zero or above 100 will
    be clamped to the minimum or maximum value. This value can be edited
    manually in the Gantt chart view of the application, or can be
    selected on the Task Detail page within the Kanban board.
    """

    isSummary: bool | None = None
    """
    True if this Task is the parent of multiple Tasks underneath it. A
    parent Task is a "rolled-up" view of multiple children that allows
    you to view a section of work at a glance. You can create a summary
    Task in the Gantt chart view of the application by adding child
    tasks underneath a parent Task.
    """

    wbs: str | None = None
    """
    The WBS (Work Breakdown Structure) number for this task within the
    Gantt chart hierarchy. See [What Is a Work Breakdown Structure
    (WBS)?](https://www.projectmanager.com/guides/work-breakdown-structure)
    on Project Manager for more information. The WBS number is an
    outline number in the form `#.#.#.#` which indicates how tasks are
    organized and sorted. The WBS value is only available to users at
    certain edition levels. This value can only be changed if you are a
    Project Editor.
    """

    actualCost: float | None = None
    """
    The actual cost of this Task to date, if known.
    """

    plannedCost: float | None = None
    """
    The planned cost for this Task. Cannot be negative.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
