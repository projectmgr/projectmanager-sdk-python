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
class ProjectMemberDto:
    """
    A ProjectMember is a user who can collaborate on a Project. You can
    control permissions for what each ProjectMember can do and how they
    can interact with the Project using this model.
    """

    id: str | None = None
    initials: str | None = None
    name: str | None = None
    avatarUrl: str | None = None
    role: str | None = None
    permission: str | None = None
    color: str | None = None
    permissionOptions: PermissionOptionsDto | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
