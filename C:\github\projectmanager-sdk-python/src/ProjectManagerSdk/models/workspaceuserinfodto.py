#
# ProjectManager API for Python
#
# (c) 2023-2024 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  2023-2024 ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#


from ProjectManagerSdk.models.workspacelinksdto import WorkSpaceLinksDto
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


