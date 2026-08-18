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


from ProjectManagerSdk.models.projectexportfilterdto import ProjectExportFilterDto
from typing import List
import dataclasses

@dataclasses.dataclass
class ProjectExportSettingsDto:
    """
    Export settings for Projects export
    """

    type: str | None = None
    """
    Format to export to, currently csv and excel are supported
    """

    includeClosed: bool | None = None
    """
    Include closed projects to export
    """

    columns: object | None = None
    """
    The list of column names to export
    """

    filters: ProjectExportFilterDto | None = None
    """
    Export filters
    """

    order: List[str] | None = None
    """
    Order of columns to export
    """


