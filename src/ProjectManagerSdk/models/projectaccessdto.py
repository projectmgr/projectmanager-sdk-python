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
class ProjectAccessDto:
    """
    ProjectAccessDto
    """

    userId: str | None = None
    """
    The unique identifier of the user of this ProjectMember.
    """

    projectId: str | None = None
    """
    The unique identifier of the user of this Project.
    """

    role: str | None = None
    """
    The role of the user in the project
    """

    hasJoined: bool | None = None
    """
    If set to true, the user has joined the project. If set to false,
    the user may still have access due to the access all projects
    permission. In the UI only projects that the user has joined will be
    shown in the navigation on the left
    """


