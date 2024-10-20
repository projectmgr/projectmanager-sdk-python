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


from ProjectManagerSdk.models.exportduedatefilterdto import ExportDueDateFilterDto
from ProjectManagerSdk.models.exportpriorityfilterdto import ExportPriorityFilterDto
from ProjectManagerSdk.models.riskexportprogressfilterdto import RiskExportProgressFilterDto
from typing import List
import dataclasses

@dataclasses.dataclass
class RiskExportSettingsDto:
    """
    Export Settings for Risk Export
    """

    name: str | None = None
    """
    the name used by the export
    """

    format: str | None = None
    """
    Format to export to, currently csv and excel are supported Valid
    options are: * Csv * excel
    """

    columns: List[str] | None = None
    """
    The list of column names to export
    """

    orderBy: str | None = None
    """
    Which column should be used to order the data Valid options are: *
    name * createDate * assignees * dueDate * impact * level *
    likelihood * openClosed * priority * response * tags * description *
    resolution
    """

    orderDirection: str | None = None
    """
    Specifies the direction of the order. Valid values are "asc" and
    "desc" Valid options are: * asc * desc
    """

    timeZoneOffset: int | None = None
    """
    Timezone offset in minutes
    """

    dueDateFilter: ExportDueDateFilterDto | None = None
    """
    Specify the due date filter for the export. If left null, no due
    date filter will be applied
    """

    priorityFilter: ExportPriorityFilterDto | None = None
    """
    Specify the priority filter for the export. If left null, no
    priority filter will be applied
    """

    progressFilter: RiskExportProgressFilterDto | None = None
    """
    Specify the progress filter for the export. If left null, no
    progress filter will be applied
    """

    assignees: List[str] | None = None
    """
    A list of resourceIds to filter the risks by assignees. If left null
    or empty this will be ignored
    """

    tags: List[str] | None = None
    """
    A list of tagIds to filter the risks by tags. If left null or empty
    this will be ignored
    """


