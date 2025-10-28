#
# ProjectManager API for Python
#
# (c) ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#


from ProjectManagerSdk.models.userrolepermissionsdto import UserRolePermissionsDto
from typing import List
import dataclasses

@dataclasses.dataclass
class UserRoleDto:
    """
    A UserRole is a name for a privilege level granted to a specific
    User. The 'Global Admin' UserRole is granted to the owner of the
    Workspace, and this UserRole cannot be changed. You can choose which
    UserRole applies to a User within your Workspace.
    """

    id: str | None = None
    """
    The unique identifier of this UserRole.
    """

    name: str | None = None
    """
    The friendly name of this UserRole.
    """

    description: str | None = None
    """
    The description of this UserRole.
    """

    isAdmin: bool | None = None
    """
    Set to true if this is the default Admin role
    """

    isCustom: bool | None = None
    """
    Set to true if this is a custom role (Only supported on Enterprise
    Plan)
    """

    isGlobalAdmin: bool | None = None
    """
    Set to true if this is the default Global Admin role
    """

    isGuest: bool | None = None
    """
    Set to true if this is the Guest role
    """

    isDefault: bool | None = None
    """
    This is the role that will be assigned to new users by default.
    """

    permissions: UserRolePermissionsDto | None = None
    """
    Returns the permission setup associated with this UserRole
    """


