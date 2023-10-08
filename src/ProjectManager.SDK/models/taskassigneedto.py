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
class TaskAssigneeDto:
    """
    A TaskAssignee is the person to whom a Task is assigned. A single
    Task can be assigned to multiple TaskAssignees.
    """

    id: object | None = None
    initials: object | None = None
    name: object | None = None
    description: object | None = None
    isActive: object | None = None
    color: object | None = None
    firstName: object | None = None
    lastName: object | None = None
    shortName: object | None = None
    avatarUrl: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
