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
class MeetingTodoUpdateDto:
    """
    The properties for updating a MeetingTodo.
    """

    text: str | None = None
    """
    The full description of this MeetingTodo.
    """

    complete: bool | None = None
    """
    True if this MeetingTodo is complete.
    """


