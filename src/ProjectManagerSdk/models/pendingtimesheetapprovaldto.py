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
class PendingTimeSheetApprovalDto:
    """
    Information about a pending timesheet approval
    """

    resourceId: str | None = None
    """
    The resource whose timesheet is being approved
    """

    date: str | None = None
    """
    The date of the week to which the timesheet applies
    """

    resourceName: str | None = None
    """
    The name of the resource
    """


