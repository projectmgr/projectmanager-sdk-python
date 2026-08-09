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
    Indicates whether this Meeting participates in a recurring series.
    true if the Meeting is part of a recurrence (series parent when is,
    or a child otherwise); false if it is a standalone Meeting. When
    saved as false during an update, the service layer detaches the
    Meeting from its series, which clears parent/child relationships
    including and recurringSettings.
    """

    moveToProject: MoveTaskToProjectDto | None = None
    """
    Object contains data to move meeting to another project
    """


