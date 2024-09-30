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


from ProjectManagerSdk.models.taskassigneedto import TaskAssigneeDto
from ProjectManagerSdk.models.taskfieldvaluedto import TaskFieldValueDto
from ProjectManagerSdk.models.taskfiledto import TaskFileDto
from ProjectManagerSdk.models.taskprojectdto import TaskProjectDto
from ProjectManagerSdk.models.taskstatusdto import TaskStatusDto
from ProjectManagerSdk.models.tasktagdto import TaskTagDto
from ProjectManagerSdk.models.tasktododto import TaskTodoDto
from typing import List
import dataclasses

@dataclasses.dataclass
class TaskDto:
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

    tags: List[TaskTagDto] | None = None
    """
    The TaskTags that apply to this Task.
    """

    projectId: str | None = None
    """
    The unique identifier of the Project to which this Task belongs.
    """

    assignees: List[TaskAssigneeDto] | None = None
    """
    The list of assignees who are to work on this Task, if any.
    """

    todos: List[TaskTodoDto] | None = None
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

    plannedStartDate: str | None = None
    """
    The date when work on this Task is planned to begin. This value
    contains only the date in year-month-day format. For display, this
    date will always be shown as this same year-month-day regardless of
    time zone. For reporting purposes, this date is calculated against
    the official time zone of the Workspace. For example: A Task has a
    planned completion date of July 5, 2023 in a Workspace that has a
    time zone of US Pacific Time (GMT-7 or GMT-8, depending on daylight
    savings time). This project is considered overdue on 12:01 AM July
    6th 2023 in US Pacific time.
    """

    plannedFinishDate: str | None = None
    """
    The date when work on this Task is expected to complete. This value
    contains only the date in year-month-day format. For display, this
    date will always be shown as this same year-month-day regardless of
    time zone. For reporting purposes, this date is calculated against
    the official time zone of the Workspace. For example: A Task has a
    planned completion date of July 5, 2023 in a Workspace that has a
    time zone of US Pacific Time (GMT-7 or GMT-8, depending on daylight
    savings time). This project is considered overdue on 12:01 AM July
    6th 2023 in US Pacific time.
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

    isLocked: bool | None = None
    """
    Unlocked tasks can be adjusted by changes to their dependencies,
    resource leveling, or other factors. All tasks are unlocked by
    default. If a task is set to `IsLocked` = `true`, the dates and
    assigned resources are locked for this task and will not be
    automatically changed by any process.
    """

    isMilestone: bool | None = None
    """
    True if this task is a milestone. Milestones represent a specific
    point in time for the project. When a milestone is locked, it
    represents a fixed time within the project that can be used to
    relate to other tasks.
    """

    priorityId: int | None = None
    """
    Return the priority of a task
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

    color: str | None = None
    """
    The hexadecimal RRGGBB Task Color as set in the Gantt. This value is
    read-only; to set this value, change the `Theme` field.
    """

    theme: str | None = None
    """
    Color theme definition for this Task. eg. Blue, Brown, DarkBlue,
    DarkGrey, Gold, Green, Grey, LightBrown, LightGreen, LightGrey,
    LightPurple, LightYellow, Magenta, Mauve, Navy, Orange, Purple, Red.
    """

    actualCost: float | None = None
    """
    The actual cost of this Task to date, if known.
    """

    actualResourceCost: float | None = None
    """
    The actual resource cost of this Task
    """

    plannedCost: float | None = None
    """
    The planned cost for this Task. Cannot be negative.
    """

    plannedResourceCost: float | None = None
    """
    The planned resource cost of this Task
    """

    plannedDuration: int | None = None
    """
    The planned duration (in minutes) for this Task.
    """

    plannedEffort: int | None = None
    """
    The planned effort (in minutes) for this Task.
    """

    fields: List[TaskFieldValueDto] | None = None
    """
    Obsolete - use FieldValues instead
    """

    fieldValues: List[TaskFieldValueDto] | None = None
    """
    Task fields array with values
    """

    files: List[TaskFileDto] | None = None
    """
    The list of files associated with this Task, if any. This field will
    be present when you fetch a single object. When you query for
    multiple objects, this field is not included in results by default.
    To expand this field, specify the name of this field in the
    `$expand` parameter.
    """


