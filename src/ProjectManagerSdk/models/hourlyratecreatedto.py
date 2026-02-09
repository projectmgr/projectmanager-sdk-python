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
class HourlyRateCreateDto:
    """
    The payload to create a hourly rate
    """

    resourceId: str | None = None
    """
    The ResourceId that the rate is for
    """

    skillId: str | None = None
    """
    The SkillId that the rate is for
    """

    projectId: str | None = None
    """
    The ProjectId that the rate is for
    """

    hourlyRate: float | None = None
    """
    The hourly rate value, the rate will be created for all periods with
    this value. Either hourlyRate or copyFromRateId has to be specified
    but not both.
    """

    copyFromRateId: str | None = None
    """
    The rateId to copy from. The values for each rate period will match
    the values for the source rate. Either hourlyRate or copyFromRateId
    has to be specified but not both.
    """


