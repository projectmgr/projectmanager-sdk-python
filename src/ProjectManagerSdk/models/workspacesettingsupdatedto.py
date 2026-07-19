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


from ProjectManagerSdk.models.workspaceworkingdaysdto import WorkspaceWorkingDaysDto
from typing import List
import dataclasses

@dataclasses.dataclass
class WorkspaceSettingsUpdateDto:
    """
    Request body for updating workspace-level scheduling defaults. Omit
    properties to leave existing values unchanged.
    """

    defaultPlannedHours: float | None = None
    """
    Default planned hours per day for new resources (0–24).
    """

    workingDays: WorkspaceWorkingDaysDto | None = None
    """
    Default working hours per weekday for the workspace calendar.
    """


