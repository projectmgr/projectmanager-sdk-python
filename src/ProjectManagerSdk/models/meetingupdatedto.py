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


from ProjectManagerSdk.models.movetasktoprojectdto import MoveTaskToProjectDto
from typing import List
import dataclasses

@dataclasses.dataclass
class MeetingUpdateDto:
    """
    A Meeting is a lightweight calendar event that may or may not belong
    to a project. It is only visible to the person who created it and
    the users assigned to it.
    """

    name: str | None = None
    """
    The common name of this Meeting.
    """

    description: str | None = None
    """
    This field contains the Meeting's description.
    """

    priorityId: int | None = None
    """
    Return the priority of a Meeting
    """

    plannedStartDate: str | None = None
    """
    The planned start date/time for this Meeting, in UTC. Time must be
    on a 15-minute boundary (0, 15, 30, or 45 minutes). Clients should
    convert to local time only when displaying to the user.
    """

    durationMinutes: int | None = None
    """
    The duration (in 15-minute increments) for this Meeting.
    """

    assignees: List[str] | None = None
    """
    If specified, replaces the list of resources assigned to this
    meeting.
    """

    recurring: bool | None = None
    """
    Deprecated - please use BreakRecurrency instead. When sent as false,
    this breaks the Meeting out of its recurring series. Sending true or
    omitting it leaves the series intact.
    """

    breakRecurrency: bool | None = None
    """
    Set this to true to break this Meeting out of its recurring series
    as part of this update. The Meeting is detached from its series,
    clearing its parent/child relationship and its recurrence settings.
    Any other changes in the same update are then applied to this
    Meeting alone rather than being propagated across the rest of the
    series. This has no effect if the Meeting is not part of a recurring
    series. A Meeting can only be made recurring through the
    MeetingRecurrency endpoints.
    """

    moveToProject: MoveTaskToProjectDto | None = None
    """
    Object contains data to move meeting to another project
    """


