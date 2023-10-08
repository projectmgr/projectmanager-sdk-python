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
class AssigneeUpsertDto:
    """
    An AssigneeUpsert is a create-or-update process that will either
    create a new assignment of effort to a TaskAssignee or update an
    existing effort amount for an existing TaskAssignee.
    """

    id: str | None = None
    """
    The unique identifier of the TaskAssignee to which work is being
    assigned.
    """

    assignedEffort: int | None = None
    """
    The new amount of effort to assign for this Resource.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
