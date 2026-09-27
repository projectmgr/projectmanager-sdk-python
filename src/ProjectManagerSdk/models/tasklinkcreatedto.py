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
class TaskLinkCreateDto:
    """
    Represents a new link (dependency) to create from one Task to
    another.
    """

    successorTaskId: str | None = None
    """
    The unique identifier of the successor Task to link to. This Task
    must be in the same Project as the predecessor Task the link is
    being created from.
    """

    linkType: str | None = None
    """
    The type of dependency between the two Tasks. Case-insensitive;
    stored and returned in camelCase. Valid values: finishToStart,
    startToStart, finishToFinish, startToFinish. Defaults to
    finishToStart when omitted.
    """

    lag: int | None = None
    """
    The number of days of lag (or lead, if negative) between the two
    Tasks.
    """


