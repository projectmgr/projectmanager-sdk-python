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
class ExportPriorityFilterDto:
    """
    Priority filter settings
    """

    isNone: bool | None = None
    """
    Include items with no priority
    """

    isVeryLow: bool | None = None
    """
    Include items with very low priority
    """

    isLow: bool | None = None
    """
    Include items with low priority
    """

    isMedium: bool | None = None
    """
    Include items with medium priority
    """

    isHigh: bool | None = None
    """
    Include items with high priority
    """

    isVeryHigh: bool | None = None
    """
    Include items with very high priority
    """

    isCritical: bool | None = None
    """
    Include items with critical priority
    """


