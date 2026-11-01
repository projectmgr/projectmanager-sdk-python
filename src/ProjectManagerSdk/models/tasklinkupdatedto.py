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
class TaskLinkUpdateDto:
    """
    Represents an update to the type and/or lag of an existing link
    (dependency) between two Tasks.
    """

    linkType: str | None = None
    """
    The type of dependency between the two Tasks. Case-insensitive;
    stored and returned in camelCase. Valid values: finishToStart,
    startToStart, finishToFinish, startToFinish.
    """

    lag: int | None = None
    """
    The number of days of lag (or lead, if negative) between the two
    Tasks.
    """


