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


from ProjectManagerSdk.models.hourlyratevaluedto import HourlyRateValueDto
from ProjectManagerSdk.models.partialresourcedto import PartialResourceDto
from ProjectManagerSdk.models.resourceskilldto import ResourceSkillDto
from ProjectManagerSdk.models.taskprojectdto import TaskProjectDto
from typing import List
import dataclasses

@dataclasses.dataclass
class HourlyRateDetailsDto:
    """
    Detailed information about a specific hourly rate, including task
    and resource counts.
    """

    id: str | None = None
    """
    The unique identifier of the Hourly Rate. This value is set by the
    system and cannot be set with a CreateHourlyRate or changed with an
    UpdateHourlyRate call.
    """

    createBy: str | None = None
    """
    Who created the Hourly rate
    """

    createDate: str | None = None
    """
    The timestamp in UTC when the Hourly Rate was created. This field is
    automatically determined by the system when this Hourly Rate is
    created and cannot be changed by the user.
    """

    modifyBy: str | None = None
    """
    Who last modified the Hourly rate
    """

    modifyDate: str | None = None
    """
    The timestamp in UTC when the Hourly Rate was most recently
    modified. This field is automatically determined by the system when
    this Hourly Rate is modified and cannot be directly changed by the
    user.
    """

    rateType: str | None = None
    """
    The type of the rate
    """

    projectId: str | None = None
    """
    The ProjectId the rate is for
    """

    project: TaskProjectDto | None = None
    """
    The Project the rate is for
    """

    resourceId: str | None = None
    """
    The ResourceId the rate is for
    """

    resource: PartialResourceDto | None = None
    """
    The Resource the rate is for
    """

    skillId: str | None = None
    """
    The SkillId the rate is for
    """

    skill: ResourceSkillDto | None = None
    """
    The Skill the rate is for
    """

    values: List[HourlyRateValueDto] | None = None
    """
    A list of all rates for each rate period
    """

    isActive: bool | None = None
    """
    If this is an archived rate
    """

    taskCount: int | None = None
    """
    Total number of tasks with at least 1 association to this rate
    """

    resourceCount: int | None = None
    """
    Total number of resources using this rate
    """

    hourlyRateTimesheetCount: int | None = None
    """
    Total number of timesheets using this rate
    """


