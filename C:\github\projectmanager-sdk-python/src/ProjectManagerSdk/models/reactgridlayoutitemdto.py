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
class ReactGridLayoutItemDto:
    """
    React grid layout item object
    """

    w: int | None = None
    """
    Width
    """

    h: int | None = None
    """
    Height
    """

    x: int | None = None
    """
    X position
    """

    y: int | None = None
    """
    Y position
    """

    i: str | None = None
    """
    ID
    """

    moved: bool | None = None
    """
    Moved indicator
    """

    static: bool | None = None
    """
    If true, equal to `isDraggable: false, isResizable: false`
    """


