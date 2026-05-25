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
class TaskPlannedAllocationDto:
    """
    Planned minutes attributed to a single calendar day for a resource.
    """

    date: str | None = None
    """
    Calendar date for this planned segment (date-only; workspace
    calendar applies).
    """

    minutes: int | None = None
    """
    Planned minutes on date for this resource.
    """


