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
class NotificationTotalCountDto:
    """
    Information about notifications for the current user. A notification
    represents a message sent to a user to inform them of relevant
    actions or events within their workspace. Notifications are
    ephemeral and may be deleted when they are no longer needed. When a
    user has more than 1,000 pending notifications some old
    notifications will be deleted automatically.
    """

    totalCount: int | None = None
    """
    The total number of notifications pending for the current user.
    """


