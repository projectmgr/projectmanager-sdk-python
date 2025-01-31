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


from typing import List
import dataclasses

@dataclasses.dataclass
class TaskCreateDto:
    """
    A Task is an individual element of work that must be performed to
    complete a Project. A Task can have one or more Resources assigned
    to it. Tasks can be linked to other Tasks to indicate whether they
    have a dependency or a connection.
    """

    name: str | None = None
    """
    The common name of this Task.
    """

    description: str | None = None
    """
    A description of the work to be performed in this Task.
    """

    percentComplete: int | None = None
    """
    The numerical percentage, from 0-100, representing the percentage
    completion for this Task. Any numbers below zero or above 100 will
    be clamped to the minimum or maximum value. This value can be edited
    manually in the Gantt chart view of the application, or can be
    selected on the Task Detail page within the Kanban board.
    """

    statusId: str | None = None
    """
    The unique identifier of the TaskStatus for this Task
    """

    priorityId: int | None = None
    """
    A numerical value representing the Priority of this Task
    """

    assignees: List[str] | None = None
    """
    A list of unique identifiers of TaskAssignees to be assigned to this
    Task
    """

    plannedStartDate: str | None = None
    """
    The date when work on this Task is planned to begin.
    """

    plannedFinishDate: str | None = None
    """
    The date when work on this Task is expected to complete.
    """

    plannedDuration: int | None = None
    """
    The planned duration (in minutes) for this Task. Cannot be negative.
    """

    plannedEffort: int | None = None
    """
    The planned effort (in minutes) for this Task. Cannot be negative.
    """

    plannedCost: float | None = None
    """
    The planned cost for this Task. Cannot be negative.
    """

    actualStartDate: str | None = None
    """
    The date when work on this Task actually started, if known.
    """

    actualCost: float | None = None
    """
    The actual cost of this Task to date, if known.
    """

    theme: str | None = None
    """
    Color theme definition for this task. eg. Blue, Brown, DarkBlue,
    DarkGrey, Gold, Green, Grey, LightBrown, LightGreen, LightGrey,
    LightPurple, LightYellow, Magenta, Mauve, Navy, Orange, Purple, Red.
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


