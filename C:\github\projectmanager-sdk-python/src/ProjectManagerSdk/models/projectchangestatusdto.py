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


from typing import List
import dataclasses

@dataclasses.dataclass
class ProjectChangeStatusDto:
    """
    A ProjectChange is an individual edit that has been made to a
    project. Since multiple users can edit a project at the same time,
    individual ProjectChanges are applied in a sequential fashion. If a
    ProjectChange causes a conflict or cannot be applied, it will be
    rejected. You can examine a ProjectChange to determine its conflict
    resolution status.
    """

    id: str | None = None
    """
    The unique identifier of this ProjectChange.
    """

    success: bool | None = None
    """
    True if this ProjectChange was successfully applied. If the
    ProjectChange has not been applied, this value is null.
    """

    state: str | None = None
    """
    A status flag that indicates the progress of the ProjectChange
    through resolution.
    """


