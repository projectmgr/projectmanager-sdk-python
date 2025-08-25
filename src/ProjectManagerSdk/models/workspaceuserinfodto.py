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


from ProjectManagerSdk.models.workspacelinksdto import WorkSpaceLinksDto
from ProjectManagerSdk.models.workspacepermissionsdto import WorkSpacePermissionsDto
from typing import List
import dataclasses

@dataclasses.dataclass
class WorkSpaceUserInfoDto:
    """
    Information about a currently logged in user. You can call the
    RetrieveMe API to gather information about the current user.
    """

    links: WorkSpaceLinksDto | None = None
    """
    A collection of shortcut links for the currently logged in
    Workspace.
    """

    emailAddress: str | None = None
    """
    The email address of the currently logged in user.
    """

    id: str | None = None
    """
    The unique identity of the currently logged in user.
    """

    fullName: str | None = None
    """
    The full name of the currently logged in user.
    """

    workSpaceId: str | None = None
    """
    The id of the workspace the user is currently logged into.
    """

    workSpaceName: str | None = None
    """
    The name of the Workspace that the current user has logged onto. For
    most companies, the workspace name will be the name of the business.
    """

    roleName: str | None = None
    """
    The user's role within the current Workspace.
    """

    isGlobalAdmin: bool | None = None
    """
    True if this user is considered a global administrator of the
    current Workspace.
    """

    isAccountAdministrator: bool | None = None
    """
    True if this user is considered an account administrator of the
    current Workspace.
    """

    permissions: WorkSpacePermissionsDto | None = None
    """
    Workspace Permissions that the user has within the current
    Workspace.
    """

    workSpaceStatus: str | None = None
    """
    The current account status of this WorkSpace. This can be one of
    four statuses: - Trial - Active - Cancelled - Expired
    """

    workSpaceIsActive: bool | None = None
    """
    This is true if the WorkSpace is in the Active or Trial state.
    """

    workSpaceCountry: str | None = None
    """
    The name of the country that the current Workspace is located in.
    """

    workSpaceCountryCode: str | None = None
    """
    Returns the iso country code for the current workspace.
    """

    location: str | None = None
    """
    The location of the user, which is a combination of city, state (US
    Only), and country.
    """


