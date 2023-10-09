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


from ProjectManagerSdk.models.permissionoptionsdto import PermissionOptionsDto
from dataclasses import dataclass

@dataclass
class ProjectMemberDto:
    """
    A ProjectMember is a user who can collaborate on a Project. You can
    control permissions for what each ProjectMember can do and how they
    can interact with the Project using this model.
    """

    id: str | None = None
    """
    The unique identifier of the user of this ProjectMember.
    """

    initials: str | None = None
    """
    the initials of the user
    """

    name: str | None = None
    """
    The display name of the user
    """

    avatarUrl: str | None = None
    """
    Avatar URL
    """

    role: str | None = None
    """
    The role of the user in the project Obsolete use Permission instead
    """

    permission: str | None = None
    """
    The current permission of the user
    """

    color: str | None = None
    """
    The color for their avatar
    """

    permissionOptions: PermissionOptionsDto | None = None
    """
    Specifies the permissions that you can set against the project
    member. This changes based on who is logged in and the role they
    have.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
