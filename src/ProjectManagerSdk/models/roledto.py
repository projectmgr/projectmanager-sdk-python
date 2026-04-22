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


from typing import List
import dataclasses

@dataclasses.dataclass
class RoleDto:
    """
    Workspace business role returned by the data API security endpoints
    (list/update responses and create response).
    """

    id: str | None = None
    """
    Unique identifier of the business user role (`BusinessUserRoleId`).
    """

    name: str | None = None
    """
    Display name of the role (e.g. Member, Manager, or a custom role
    name).
    """

    description: str | None = None
    """
    Optional description; for system roles may match a well-known
    description token used server-side.
    """

    isGlobalAdmin: bool | None = None
    """
    True when this row is the non-editable global administrator role for
    the workspace.
    """

    isAdmin: bool | None = None
    """
    True when this role has account administrator privileges (non-guest
    elevated role).
    """

    isCustom: bool | None = None
    """
    True for user-defined roles; false for built-in system roles.
    """

    isDefault: bool | None = None
    """
    True when this role represents the default team member role for the
    workspace.
    """

    isGuest: bool | None = None
    """
    True when this role is the guest (client) role with restricted
    permissions.
    """

    permissions: object | None = None
    """
    Workspace security matrix. Keys are camelCase action names (for
    example invitePeople). Each entry includes isGranted and, when the
    action is subscription-gated, optional featureId and featureName.
    """


