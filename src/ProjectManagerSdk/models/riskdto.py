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


from ProjectManagerSdk.models.assignmentdto import AssignmentDto
from ProjectManagerSdk.models.taskownerdto import TaskOwnerDto
from ProjectManagerSdk.models.tasktagdto import TaskTagDto
from typing import List
import dataclasses

@dataclasses.dataclass
class RiskDto:
    """
    Represents a potential threat or uncertainty that could impact a
    project, system, or process. Contains information such as its
    likelihood, impact, response, and resolution details.
    """

    id: str | None = None
    """
    The unique identifier of this risk.
    """

    projectId: str | None = None
    """
    The unique identifier of the Project to which this Task belongs.
    """

    name: str | None = None
    """
    The common name of this Task.
    """

    dueDate: str | None = None
    """
    The date when work on this risk is expected to complete. This value
    contains only the date in year-month-day format. For display, this
    date will always be shown as this same year-month-day regardless of
    time zone. For reporting purposes, this date is calculated against
    the official time zone of the Workspace.
    """

    percentComplete: int | None = None
    """
    The numerical percentage, from 0-100, representing the percentage
    completion for this risk. Any numbers below zero or above 100 will
    be clamped to the minimum or maximum value.
    """

    priority: int | None = None
    """
    Indicates the level of importance assigned to a risk, with 500 being
    standard priority; the higher the number, the higher the priority.
    """

    impact: int | None = None
    """
    The potential effect of the risk.
    """

    likelihood: int | None = None
    """
    Probability or chance of the risk occurring.
    """

    responseId: int | None = None
    """
    The planned or implemented response to address the identified risk.
    Avoid, Mitigate, Transfer, Accept
    """

    resolution: str | None = None
    """
    The actions or strategy planned or taken to mitigate or eliminate
    the risk.
    """

    notes: str | None = None
    """
    Any additional comments, observations, or details related to the
    risk.
    """

    createDate: str | None = None
    """
    The timestamp in UTC when this risk was created.
    """

    modifyDate: str | None = None
    """
    The timestamp in UTC when this risk was most recently modified.
    """

    version: int | None = None
    """
    The risk version.
    """

    shortId: str | None = None
    """
    A short ID that can be used to refer to this risk. This short ID is
    guaranteed to be unique within your Workspace.
    """

    taskTypeId: int | None = None
    """
    Risk has a taskTypeId of 31
    """

    assignments: List[AssignmentDto] | None = None
    """
    Users assigned to the risk.
    """

    tags: List[TaskTagDto] | None = None
    """
    Tags applied to the risk.
    """

    owner: TaskOwnerDto | None = None
    """
    The user which created the risk.
    """

    filesCount: int | None = None
    """
    The number of files attached to the risk.
    """

    commentsCount: int | None = None
    """
    The number of comments added to the risk.
    """

    riskTypeId: int | None = None
    """
    The id of the Risk Type Risk = 1 Assumption = 2 Issue = 3 Dependency
    = 4 Change = 5
    """


