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
class ProjectMemberRoleDto:
    """
    Dto To Describe a ProjectMember Role
    """

    role: str | None = None
    """
    Role to apply. Optional — when omitted, a default role is applied
    based on the target user's workspace access: users who can edit all
    projects become a Manager, guest users become a Guest, and everyone
    else becomes an Editor. When updating an existing member, omitting
    the role leaves their current role unchanged.
    """


