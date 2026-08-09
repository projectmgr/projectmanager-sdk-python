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
class ProjectExportFilterDto:
    """
    Filter settings for Projects export
    """

    groupId: str | None = None
    """
    Specify the project group filter for the export
    """

    favoritesOnly: bool | None = None
    """
    Specify whether to include only favorite projects in the export
    """

    status: List[str] | None = None
    """
    Specify the status filter for the export
    """

    manager: List[str] | None = None
    """
    Specify the project manager filter for the export
    """

    customer: List[str] | None = None
    """
    Specify the project customer filter for the export
    """

    chargeCode: List[str] | None = None
    """
    Specify the project charge code filter for the export
    """

    priority: List[str] | None = None
    """
    Specify the priority filter for the export
    """


