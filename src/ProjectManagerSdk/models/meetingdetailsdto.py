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
from ProjectManagerSdk.models.meetingprojectdto import MeetingProjectDto
from ProjectManagerSdk.models.recurringtasksettingsdto import RecurringTaskSettingsDto
from ProjectManagerSdk.models.taskownerdto import TaskOwnerDto
from ProjectManagerSdk.models.tasktagdto import TaskTagDto
from ProjectManagerSdk.models.tasktododto import TaskTodoDto
from typing import List
import dataclasses

@dataclasses.dataclass
class MeetingDetailsDto:
    """
    A Meeting is a lightweight calendar event that may or may not belong
    to a project. It is only visible to the person who created it and
    the users assigned to it.
    """

    id: str | None = None
    """
    The unique identifier of the Meeting
    """

    name: str | None = None
    """
    The common name of this Meeting.
    """

    description: str | None = None
    """
    This field contains the Meeting's description.
    """

    plannedStartDate: str | None = None
    """
    The planned start date/time for this Meeting, in UTC. Clients should
    convert to local time only when displaying to the user.
    """

    plannedFinishDate: str | None = None
    """
    The planned finish date/time for this Meeting, in UTC. Clients
    should convert to local time only when displaying to the user.
    """

    plannedDuration: int | None = None
    """
    The planned duration (in minutes) for this Meeting.
    """

    plannedEffort: int | None = None
    """
    The planned effort (in minutes) for this Meeting.
    """

    priorityId: int | None = None
    """
    Return the priority of a Meeting
    """

    assignees: List[MeetingAssigneeDto] | None = None
    """
    The list of resources assigned to this Meeting
    """

    shortId: str | None = None
    """
    A short ID that can be used to refer to this Meeting. This short ID
    is guaranteed to be unique within your Workspace.
    """

    tags: List[TaskTagDto] | None = None
    """
    The tags that apply to this Meeting.
    """

    todos: List[TaskTodoDto] | None = None
    """
    A list of todo items for this Meeting.
    """

    createDate: str | None = None
    """
    Timestamp when the Meeting was created
    """

    owner: TaskOwnerDto | None = None
    """
    The owner of this Meeting.
    """

    ownerId: str | None = None
    """
    The ownerId of this Meeting.
    """

    project: MeetingProjectDto | None = None
    """
    The project this meeting belongs to
    """

    discussionData: DiscussionDataDto | None = None
    """
    Discussion data - number of comments, last read time
    """

    fileData: FileDataDto | None = None
    """
    File data - number of files, last read time
    """

    recurring: bool | None = None
    """
    Indicates whether this meeting is part of a recurring meeting series
    """

    recurringParentTaskId: str | None = None
    """
    The parent task in the recurring meeting series
    """

    recurringSettings: RecurringTaskSettingsDto | None = None
    """
    The meeting's recurrency settings
    """


