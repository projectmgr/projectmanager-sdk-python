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
    options are: * csv * excel
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


