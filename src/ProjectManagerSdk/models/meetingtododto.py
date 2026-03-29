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
class MeetingTodoDto:
    """
    A MeetingTodo is a sub-item that represents a unit of work on the
    Meeting. You can use MeetingTodo to represent individual items for a
    larger piece of work (e.g. agenda items, action items).
    """

    id: str | None = None
    """
    The unique identifier of this MeetingTodo.
    """

    text: str | None = None
    """
    The full description of this MeetingTodo.
    """

    complete: bool | None = None
    """
    True if this MeetingTodo is complete.
    """

    createDate: str | None = None
    """
    The timestamp in UTC when this object was created.
    """

    modifyDate: str | None = None
    """
    The timestamp in UTC when this object was last modified.
    """


