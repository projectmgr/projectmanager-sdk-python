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


from ProjectManagerSdk.models.workspacepermissionsdto import WorkSpacePermissionsDto
from typing import List
import dataclasses

@dataclasses.dataclass
class RoleCreateDto:
    """
    Request body for POST /api/data/security/businessroles. Creates a
    custom workspace role; the server assigns the role id and the name
    must be unique in the workspace. Permission flags use the same shape
    as RetrieveMe `permissions` (Astro.Common.Dto.WorkSpaces.WorkSpacePermissionsDto).
    Subscription entitlements are applied server-side; nothing in
    Chargebee is updated by this request.
    """

    name: str | None = None
    """
    Display name of the new custom role; must not duplicate another role
    name in the workspace (case-insensitive).
    """

    description: str | None = None
    """
    Optional description; must not match reserved system role
    description tokens.
    """

    permissions: WorkSpacePermissionsDto | None = None
    """
    Workspace permissions for the new role. Same property names as
    RetrieveMe; `true`/`false` per flag. Omitted or null properties are
    treated as off. `ChangeOwnEmail` is not modeled here and defaults to
    off for new custom roles.
    """


