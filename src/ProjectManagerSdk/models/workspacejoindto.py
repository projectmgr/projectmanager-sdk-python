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
class WorkSpaceJoinDto:
    """
    A Workspace represents a single business subscription to the
    ProjectManager.com service. You can be a member of multiple
    Workspaces. Each Workspace is completely separate from all other
    Workspaces and a user cannot log in to multiple Workspaces at the
    same time.
    """

    businessUserId: str | None = None
    """
    The unique identifier of the BusinessUser to invite to this
    Workspace.
    """


