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
class TaskActualTimeEntryDto:
    """
    A single timesheet line for the task and resource.
    """

    id: str | None = None
    """
    Timesheet row identifier.
    """

    date: str | None = None
    """
    Calendar date of the time entry (date-only).
    """

    minutes: int | None = None
    """
    Minutes reported on this timesheet row for the task.
    """


