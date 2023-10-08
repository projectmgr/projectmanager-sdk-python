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

    id: str | None = None
    initials: str | None = None
    name: str | None = None
    description: str | None = None
    isActive: bool | None = None
    color: str | None = None
    firstName: str | None = None
    lastName: str | None = None
    shortName: str | None = None
    avatarUrl: str | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
