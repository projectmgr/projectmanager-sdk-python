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


from ProjectManagerSdk.models.reactgridlayoutitemdto import ReactGridLayoutItemDto
from dataclasses import dataclass

@dataclass
class ReactGridLayoutDto:
    """
    A setting for react grid layout sizes
    """

    lg: list[ReactGridLayoutItemDto] | None = None
    """
    Used for large screen size (1200)
    """

    md: list[ReactGridLayoutItemDto] | None = None
    """
    Used for medium screen size (996)
    """

    sm: list[ReactGridLayoutItemDto] | None = None
    """
    Used for small screen size (768)
    """

    xs: list[ReactGridLayoutItemDto] | None = None
    """
    Used for extra small screen size (480)
    """

    xxs: list[ReactGridLayoutItemDto] | None = None
    """
    Used for super small screen size (0)
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
