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


from ProjectManagerSdk.models.holidayresourcedto import HolidayResourceDto
from typing import List
import dataclasses

@dataclasses.dataclass
class HolidayListItemDto:
    """
    Summary information for a holiday, as returned from the list
    endpoint.
    """

    id: str | None = None
    """
    The public identifier of the holiday.
    """

    reason: str | None = None
    """
    Reason or label for the holiday.
    """

    type: str | None = None
    """
    Holiday scope: global, people, or country.
    """

    dateFrom: str | None = None
    """
    Start of the holiday date span (metadata).
    """

    dateTo: str | None = None
    """
    End of the holiday date span (metadata).
    """

    countryId: List[str] | None = None
    """
    ISO 3166-1 alpha-2 country identifiers when Type is country;
    otherwise empty.
    """

    resources: List[HolidayResourceDto] | None = None
    """
    Affected resources. For country and global holidays, all active
    non-guest resources in scope; for people holidays, the assigned
    resource(s).
    """


