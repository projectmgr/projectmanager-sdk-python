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
class ChangeSetStatusDto:
    """
    Returns the id of a specific ChangeSet
    """

    changeSetId: str | None = None
    """
    The unique identifier of this Changeset
    """

    id: str | None = None
    """
    The unique identifier of the entity affected by this Changeset. For
    example, if this Changeset was created for a Task, this value will
    be the unique identifier for the Task.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
