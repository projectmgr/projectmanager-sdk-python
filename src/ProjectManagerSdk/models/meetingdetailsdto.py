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


from ProjectManagerSdk.models.discussiondatadto import DiscussionDataDto
from ProjectManagerSdk.models.filedatadto import FileDataDto
from ProjectManagerSdk.models.meetingassigneedto import MeetingAssigneeDto
from ProjectManagerSdk.models.recurringtasksettingsdto import RecurringTaskSettingsDto
from ProjectManagerSdk.models.taskownerdto import TaskOwnerDto
from ProjectManagerSdk.models.tasktagdto import TaskTagDto
from ProjectManagerSdk.models.tasktododto import TaskTodoDto
from typing import List
import dataclasses

@dataclasses.dataclass
class MeetingDetailsDto:
    """
    A Npt is a task that does not belong to the project. It is only
    visible to the person who created it, and the users assigned to it.
    NPT's are a lightweight version of a project task.
    """

    id: str | None = None
    """
    The unique identifier of the Meeting
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

    assignees: List[MeetingAssigneeDto] | None = None
    """
    The list of resources assigned to this Meeting
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
    Timestamp when the Meeting was created
    """

    owner: TaskOwnerDto | None = None
    """
    The owner of this Task.
    """

    ownerId: str | None = None
    """
    The ownerId of this Task.
    """

    discussionData: DiscussionDataDto | None = None
    """
    Task file data - number of comments, last read time
    """

    fileData: FileDataDto | None = None
    """
    Task file data - number of files, last read time
    """

    recurring: bool | None = None
    """
    If this is a recurring Npt task
    """

    recurringParentTaskId: str | None = None
    """
    The parent task in the recurring Npt task sequence
    """

    recurringSettings: RecurringTaskSettingsDto | None = None
    """
    The Npt Task Recurrency settings
    """


