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


