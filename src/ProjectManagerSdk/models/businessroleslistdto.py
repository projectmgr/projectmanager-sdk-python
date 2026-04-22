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


from ProjectManagerSdk.models.roledto import RoleDto
from typing import List
import dataclasses

@dataclasses.dataclass
class BusinessRolesListDto:
    """
    Business roles for the account security UI. Each role includes a
    permissions object whose keys are camelCase action names (for
    example invitePeople) with isGranted and subscription-related fields
    per row.
    """

    roles: List[RoleDto] | None = None
    """
    All business roles in the workspace, including built-in and custom
    roles.
    """


