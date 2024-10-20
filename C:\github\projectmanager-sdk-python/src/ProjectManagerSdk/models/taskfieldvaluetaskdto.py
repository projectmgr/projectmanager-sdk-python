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
class TaskFieldValueTaskDto:
    """
    The TaskFieldTask is a summary of the Task that this TaskFieldValue
    relates to.
    """

    id: str | None = None
    """
    The unique identifier of this Task.
    """

    shortId: str | None = None
    """
    The unique Short Id of this Task.
    """

    name: str | None = None
    """
    The common name of this Task.
    """


