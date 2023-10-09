#
# ProjectManager API for Python
#
# (c) 2023-2023 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  2023-2023 ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#


from ProjectManagerSdk.models.reactgridlayoutdto import ReactGridLayoutDto
from dataclasses import dataclass

@dataclass
class DashboardSettingCreateDto:
    """
    User dashboard create or update dto
    """

    id: str | None = None
    """
    Unique ID
    """

    userId: str | None = None
    """
    User ID
    """

    type: str | None = None
    """
    Either custom or one of DashboardType enum
    """

    reactGridLayout: ReactGridLayoutDto | None = None
    """
    React grid layout configuration
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
