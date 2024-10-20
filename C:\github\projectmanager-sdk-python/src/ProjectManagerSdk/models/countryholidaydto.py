#
# ProjectManager API for Python
#
# (c) 2023-2024 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  2023-2024 ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#


from typing import List
import dataclasses

@dataclasses.dataclass
class CountryHolidayDto:
    """
    Country holiday entry
    """

    id: str | None = None
    """
    Holiday id
    """

    date: str | None = None
    """
    Date of holiday
    """

    countryId: int | None = None
    """
    The Country Id the holiday is associated to
    """

    countryName: str | None = None
    """
    The Country Name the holiday is associated to
    """


