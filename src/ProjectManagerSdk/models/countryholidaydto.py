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


from dataclasses import dataclass

@dataclass
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
    Country id holiday associated to
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
