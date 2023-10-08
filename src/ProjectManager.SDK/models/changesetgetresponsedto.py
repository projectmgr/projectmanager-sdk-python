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

    id: object | None = None
    success: object | None = None
    state: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
