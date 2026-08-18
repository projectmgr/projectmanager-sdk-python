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
class WorkspaceWorkingDaysDto:
    """
    Working hours per weekday (0 = non-working day). On update, omit a
    property (or send null) to leave that day unchanged.
    """

    monday: float | None = None
    """
    Working hours on Monday.
    """

    tuesday: float | None = None
    """
    Working hours on Tuesday.
    """

    wednesday: float | None = None
    """
    Working hours on Wednesday.
    """

    thursday: float | None = None
    """
    Working hours on Thursday.
    """

    friday: float | None = None
    """
    Working hours on Friday.
    """

    saturday: float | None = None
    """
    Working hours on Saturday.
    """

    sunday: float | None = None
    """
    Working hours on Sunday.
    """


