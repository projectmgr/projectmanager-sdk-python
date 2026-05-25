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
class MoveTaskToProjectDto:
    """
    Move task to project data transfer object. Contains information
    about target project to move, necessary options and users to add
    access for if needed.
    """

    projectId: str | None = None
    """
    Target project id to move
    """

    keepTimeEntries: bool | None = None
    """
    Move time entries associated with the task. If false, time entries
    will be copied to the new project but remain in the original project
    as well. If true, time entries will be moved to the new project and
    removed from the original project.
    """

    addAccessUserIds: List[str] | None = None
    """
    List of user IDs to add access for in the new project.
    """


