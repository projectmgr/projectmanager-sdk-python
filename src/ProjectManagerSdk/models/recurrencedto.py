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
class RecurrenceDto:
    """
    A single recurrence instance created by a recurring Task, NPT, or
    Meeting action
    """

    id: str | None = None
    """
    The unique identifier of the created recurrence instance
    """

    startDate: str | None = None
    """
    The occurrence start (UTC). For Meetings this carries the meeting
    time.
    """

    endDate: str | None = None
    """
    The occurrence finish (UTC)
    """


