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
class WeeklyRecurringSettingsDto:
    """
    Settings for Weeky Recurring Tasks
    """

    recurringEndDate: str | None = None
    """
    RecurringEndDate
    """

    endAfterNumberOfOccurences: int | None = None
    """
    EndAfterNumberOfOccurences
    """

    repeatOnEveryNumberOfWeeks: int | None = None
    """
    RepeatOnEveryNumberOfWeeks
    """

    repeatWeekDays: List[int] | None = None
    """
    RepeatWeekDays
    """


