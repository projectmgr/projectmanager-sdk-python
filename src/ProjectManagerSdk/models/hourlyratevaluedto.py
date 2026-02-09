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
class HourlyRateValueDto:
    """
    Represents the value of an hourly rate for a specific period,
    including audit information and references to the rate definition
    and period.
    """

    id: str | None = None
    """
    Gets or sets the unique identifier for this hourly rate value entry.
    """

    createBy: str | None = None
    """
    Gets or sets the identifier of the user or resource who created this
    hourly rate value.
    """

    createDate: str | None = None
    """
    Gets or sets the date and time when this hourly rate value was
    created.
    """

    modifyBy: str | None = None
    """
    Gets or sets the identifier of the user or resource who last
    modified this hourly rate value.
    """

    modifyDate: str | None = None
    """
    Gets or sets the date and time when this hourly rate value was last
    modified.
    """

    hourlyRateDefinitionId: str | None = None
    """
    Gets or sets the unique identifier of the hourly rate definition to
    which this value belongs.
    """

    hourlyRatePeriodId: str | None = None
    """
    Gets or sets the unique identifier of the hourly rate period to
    which this value applies.
    """

    periodStartDate: str | None = None
    """
    Gets or sets the start date of the hourly rate period for which this
    value applies. This value is sourced from the associated
    HourlyRatePeriod.
    """

    periodFinishDate: str | None = None
    """
    Gets or sets the finish date of the hourly rate period for which
    this value applies. This value is sourced from the associated
    HourlyRatePeriod.
    """

    value: float | None = None
    """
    Gets or sets the value of the hourly rate for the specified period.
    """


