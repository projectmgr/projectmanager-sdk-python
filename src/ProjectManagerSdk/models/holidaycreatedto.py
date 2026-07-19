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
class HolidayCreateDto:
    """
    Request body for creating a holiday. One occurrence per calendar day
    from DateFrom through DateTo (inclusive). Omit both lists for a
    global holiday; set ResourceIds for people scope; set CountryId for
    country scope (ISO 3166-1 alpha-2).
    """

    reason: str | None = None
    """
    Reason or label for the holiday (for example, public holiday name or
    company shutdown).
    """

    dateFrom: str | None = None
    """
    First calendar day of the holiday (inclusive).
    """

    dateTo: str | None = None
    """
    Last calendar day of the holiday (inclusive). Must be on or after
    DateFrom.
    """

    resourceIds: List[str] | None = None
    """
    Resources this holiday applies to (people scope). Mutually exclusive
    with CountryId.
    """

    countryId: List[str] | None = None
    """
    ISO 3166-1 alpha-2 country identifiers this holiday applies to
    (country scope). Mutually exclusive with ResourceIds.
    """


