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
class TaskStatusMoveResultDto:
    """
    The result of moving a single Task into a TaskStatus. One result is
    returned per requested Task move, in the same order as the request.
    """

    taskId: str | None = None
    """
    The unique identifier of the Task that was moved.
    """

    success: bool | None = None
    """
    Whether the move was accepted for this Task.
    """

    message: str | None = None
    """
    The reason the move was rejected, when Success is false.
    """

    changeSetId: str | None = None
    """
    When the Task belongs to a Project, the move is applied
    asynchronously as a Changeset and this contains its unique
    identifier. You can use RetrieveChangeset to check the progress of
    the move. This is null when the move was applied immediately.
    """


