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
class ProjectAccessEntryDto:
    """
    Represents the access permissions assigned to a single user within a
    project.
    """

    userId: str | None = None
    """
    The unique identifier of the user to whom the access permissions
    apply.
    """

    canEdit: bool | None = None
    """
    Indicates whether the user has permission to edit the project.
    """

    canManage: bool | None = None
    """
    Indicates whether the user has permission to manage the project
    (e.g., assign roles, change settings).
    """


