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


from ProjectManagerSdk.models.projectaccessentrydto import ProjectAccessEntryDto
from typing import List
import dataclasses

@dataclasses.dataclass
class ProjectMembersAccessDto:
    """
    DTO to assign roles to a list of project members
    """

    projectAccess: List[ProjectAccessEntryDto] | None = None
    """
    List of project members and their roles
    """


