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
class TaskStatusDto:
    """
    A TaskStatus is a named status level used by your business to
    determine how to measure the progress of Tasks. You can define your
    own named status levels that are appropriate for your business and
    determine which status levels are considered done.
    """

    id: str | None = None
    """
    The unique identifier of this TaskStatus.
    """

    projectId: str | None = None
    """
    The unique identifier of the Project to which this TaskStatus
    belongs.
    """

    name: str | None = None
    """
    The name of this TaskStatus.
    """

    order: int | None = None
    """
    A numerical value that can be used to sort TaskStatus values
    according to the needs of your business.
    """

    isDone: bool | None = None
    """
    True if a Task in this TaskStatus is considered done.
    """


