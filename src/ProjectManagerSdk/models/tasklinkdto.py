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
class TaskLinkDto:
    """
    Represents an existing link (dependency) from a Task to another
    Task.
    """

    successorTaskId: str | None = None
    """
    The unique identifier of the successor Task this link points to.
    """

    linkType: str | None = None
    """
    The type of dependency between the two Tasks. One of: finishToStart,
    startToStart, finishToFinish, startToFinish.
    """

    lag: int | None = None
    """
    The number of days of lag (or lead, if negative) between the two
    Tasks.
    """


