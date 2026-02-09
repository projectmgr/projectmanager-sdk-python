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
from typing import List
import dataclasses

@dataclasses.dataclass
class HourlyRatePeriodDto:
    """
    Represents a period of time for which a specific hourly rate is
    applicable.
    """

    id: str | None = None
    """
    The unique identifier of the hourly rate period.
    """

    startDate: str | None = None
    """
    The start date of the hourly rate period. If null this is the first
    period.
    """

    finishDate: str | None = None
    """
    The finish date of the hourly rate period. If null this is the last
    period.
    """

    isCurrent: bool | None = None
    """
    Indicates whether the hourly rate period is the current period.
    """

    createBy: str | None = None
    """
    The resourceId who created the hourly rate period.
    """

    createDate: str | None = None
    """
    The date and time the hourly rate period was created.
    """

    modifyBy: str | None = None
    """
    The resourceId who last modified the hourly rate period.
    """

    modifyDate: str | None = None
    """
    The date and time the hourly rate period was last modified.
    """

    values: List[HourlyRateValueDto] | None = None
    """
    A list of all the rates for the rate period
    """


