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


from ProjectManagerSdk.models.pendingtimesheetapprovaldto import PendingTimeSheetApprovalDto
from typing import List
import dataclasses

@dataclasses.dataclass
class TimeSheetApprovalResponseDto:
    """
    Holds the list of pending timesheet approvals
    """

    pendingApprovals: List[PendingTimeSheetApprovalDto] | None = None
    """
    A list of pending timesheet approvals
    """


