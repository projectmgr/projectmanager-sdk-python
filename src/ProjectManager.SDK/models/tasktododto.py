#
# ProjectManager API for Python
#
# (c) 2023-2023 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  2023-2023 ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#


from dataclasses import dataclass

@dataclass
class TaskTodoDto:
    """
    A TaskTodo is a sub-task that represents a unit of work on the Task.
    You can use TaskTodo to represent individual items for a larger
    piece of work.
    """

    id: str | None = None
    text: str | None = None
    complete: bool | None = None
    createDate: str | None = None
    modifyDate: str | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
