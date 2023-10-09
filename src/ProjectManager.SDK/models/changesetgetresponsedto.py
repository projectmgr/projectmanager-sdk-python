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
class ChangesetGetResponseDto:
    """
    A Changeset is an individual edit that has been made to a project.
    Since multiple users can edit a project at the same time, individual
    Changesets are applied in a sequential fashion. If a Changeset
    causes a conflict or cannot be applied, it will be rejected. You can
    examine a Changeset to determine its conflict resolution status.
    """

    id: str | None = None
    """
    The unique identifier of this Changeset.
    """

    success: bool | None = None
    """
    True if this Changeset was successfully applied. If the Changeset
    has not been applied, this value is null.
    """

    state: str | None = None
    """
    A status flag that indicates the progress of the Changeset through
    resolution.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
