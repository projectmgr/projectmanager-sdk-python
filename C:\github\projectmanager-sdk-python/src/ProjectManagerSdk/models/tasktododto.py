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
class TaskTodoDto:
    """
    A TaskTodo is a sub-task that represents a unit of work on the Task.
    You can use TaskTodo to represent individual items for a larger
    piece of work.
    """

    id: str | None = None
    """
    The unique identifier of this TaskTodo.
    """

    text: str | None = None
    """
    The full description of this TaskTodo.
    """

    complete: bool | None = None
    """
    True if this TaskTodo is complete.
    """

    createDate: str | None = None
    """
    The timestamp in UTC when this object was created.
    """

    modifyDate: str | None = None
    """
    The timestamp in UTC when this object was last modified.
    """


