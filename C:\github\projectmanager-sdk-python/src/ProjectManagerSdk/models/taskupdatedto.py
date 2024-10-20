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
class TaskUpdateDto:
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
    The TaskStatus assigned to this Task.
    """

    priorityId: int | None = None
    """
    The unique identifier of the TaskPriority
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

    actualCost: float | None = None
    """
    If set, this represents the actual tracked cost for this Task.
    """

    theme: str | None = None
    """
    Color theme definition for this task. eg. Blue, Brown, DarkBlue,
    DarkGrey, Gold, Green, Grey, LightBrown, LightGreen, LightGrey,
    LightPurple, LightYellow, Magenta, Mauve, Navy, Orange, Purple, Red.
    """


