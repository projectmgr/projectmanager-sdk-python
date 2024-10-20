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


from ProjectManagerSdk.models.projectversionchangedatadto import ProjectVersionChangeDataDto
from typing import List
import dataclasses

@dataclasses.dataclass
class ProjectVersionDto:
    """
    A ProjectVersion is a snapshot of a Project at a specific moment in
    time. Information on the ProjectVersion record keeps track of the
    unique identity of this version, plus the name and details of the
    user who created this version, and the changes that were made.
    """

    id: str | None = None
    """
    The unique identifier of the project version.
    """

    version: int | None = None
    """
    Version of the Project
    """

    initials: str | None = None
    """
    the initials of the user
    """

    name: str | None = None
    """
    The display name of the user
    """

    avatarUrl: str | None = None
    """
    Avatar URL
    """

    color: str | None = None
    """
    The color for their avatar
    """

    createDate: str | None = None
    """
    Version datetime
    """

    userId: str | None = None
    """
    The unique identifier of user who created backup
    """

    groupId: str | None = None
    """
    The group version belongs to
    """

    changeData: ProjectVersionChangeDataDto | None = None
    """
    Subset of the changes related to this ProjectVersion
    """


