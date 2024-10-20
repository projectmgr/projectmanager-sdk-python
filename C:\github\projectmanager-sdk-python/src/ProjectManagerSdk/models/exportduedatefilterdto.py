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
class ExportDueDateFilterDto:
    """
    Due Date Filter Settings
    """

    includeNoDueDate: bool | None = None
    """
    Include items without a due date
    """

    includeOverdue: bool | None = None
    """
    Include items with a due date in the past
    """

    includeToday: bool | None = None
    """
    Include items with a due date of today
    """

    includeThisWeek: bool | None = None
    """
    Include items due within the current week
    """

    includeNextWeek: bool | None = None
    """
    Include items due within the next week
    """

    includeLater: bool | None = None
    """
    Include items due later
    """


