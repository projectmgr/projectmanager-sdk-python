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


from ProjectManagerSdk.models.projectcreateaccessmemberdto import ProjectCreateAccessMemberDto
from typing import List
import dataclasses

@dataclasses.dataclass
class ProjectCreateAccessDto:
    """
    Specify who has access to a newly created project
    """

    everyone: bool | None = None
    """
    If set to true every user will get access to this project
    """

    members: List[ProjectCreateAccessMemberDto] | None = None
    """
    If everyone is set to false the list of members will be used to give
    people access
    """


