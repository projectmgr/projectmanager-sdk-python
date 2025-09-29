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
class NptUpdateDto:
    """
    A Npt is a task that does not belong to the project. It is only
    visible to the person who created it, and the users assigned to it.
    NPT's are a lightweight version of a project task.
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

    statusId: str | None = None
    """
    The status assigned to this Npt
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
    If set, this is the actual date when work was completed on the Task.
    This value contains only the date in year-month-day format. For
    display, this date will always be shown as this same year-month-day
    regardless of time zone. For reporting purposes, this date is
    calculated against the official time zone of the Workspace. For
    example: A Task has a planned completion date of July 5, 2023 in a
    Workspace that has a time zone of US Pacific Time (GMT-7 or GMT-8,
    depending on daylight savings time). This project is considered
    overdue on 12:01 AM July 6th 2023 in US Pacific time.
    """

    actualDuration: int | None = None
    """
    The actual duration (in minutes) for this Task. Cannot be negative.
    """

    actualCost: float | None = None
    """
    If set, this represents the actual tracked cost for this Task.
    """

    assignees: List[str] | None = None
    """
    If specified, replaces the list of resources assigned to this npt.
    """

    recurring: bool | None = None
    """
    Indicates whether this task participates in a recurring series. true
    if the task is part of a recurrence (series parent when is, or a
    child otherwise); false if it is a standalone task. When saved as
    false during an update, the service layer detaches the task from its
    series, which clears parent/child relationships including and
    recurringSettings.
    """


