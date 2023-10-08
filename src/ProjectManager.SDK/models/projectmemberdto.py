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

    id: object | None = None
    initials: object | None = None
    name: object | None = None
    avatarUrl: object | None = None
    role: object | None = None
    permission: object | None = None
    color: object | None = None
    permissionOptions: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
