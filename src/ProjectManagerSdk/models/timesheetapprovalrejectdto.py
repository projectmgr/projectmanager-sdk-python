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
class TimeSheetApprovalRejectDto:
    """
    Data for rejecting a timesheet approval
    """

    resourceId: str | None = None
    """
    The id for the resource, if null it indicates the request is for the
    current logged-in user
    """

    date: str | None = None
    """
    The date of the week to which the timesheet applies
    """

    reason: str | None = None
    """
    The reason why the timesheet approval is being rejected
    """


