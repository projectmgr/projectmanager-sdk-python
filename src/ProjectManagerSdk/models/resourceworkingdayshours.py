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
class ResourceWorkingDaysHours:
    """
    Whole hours per weekday for scheduling (matches workspace/resource
    calendar rows). Property order is Monday through Sunday for
    documentation and OpenAPI schema clarity. On read, all seven values
    are set. On create/update, omit a property (or send null) to leave
    that day unchanged; specified values merge over workspace defaults
    when building the resource calendar.
    """

    monday: float | None = None
    """
    Hours available on Monday.
    """

    tuesday: float | None = None
    """
    Hours available on Tuesday.
    """

    wednesday: float | None = None
    """
    Hours available on Wednesday.
    """

    thursday: float | None = None
    """
    Hours available on Thursday.
    """

    friday: float | None = None
    """
    Hours available on Friday.
    """

    saturday: float | None = None
    """
    Hours available on Saturday.
    """

    sunday: float | None = None
    """
    Hours available on Sunday.
    """


