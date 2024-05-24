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


from ProjectManagerSdk.models.reactgridlayoutitemdto import ReactGridLayoutItemDto
from typing import List
import dataclasses

@dataclasses.dataclass
class ReactGridLayoutDto:
    """
    A setting for react grid layout sizes
    """

    lg: List[ReactGridLayoutItemDto] | None = None
    """
    Used for large screen size (1200)
    """

    md: List[ReactGridLayoutItemDto] | None = None
    """
    Used for medium screen size (996)
    """

    sm: List[ReactGridLayoutItemDto] | None = None
    """
    Used for small screen size (768)
    """

    xs: List[ReactGridLayoutItemDto] | None = None
    """
    Used for extra small screen size (480)
    """

    xxs: List[ReactGridLayoutItemDto] | None = None
    """
    Used for super small screen size (0)
    """


