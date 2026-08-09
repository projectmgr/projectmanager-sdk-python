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
class MeetingCreateDto:
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

    startDate: str | None = None
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
    Specify a list of resources to assign to this Meeting
    """

    priority: int | None = None
    """
    The numeric of the Priority for this Meeting
    """

    projectId: str | None = None
    """
    The unique identifier of the Project for this Meeting
    """


