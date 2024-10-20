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


from __future__ import annotations
from ProjectManagerSdk.models.notificationdatadto import NotificationDataDto
from typing import List
import dataclasses

@dataclasses.dataclass
class NotificationDto:
    """
    A notification represents a message sent to a user to inform them of
    relevant actions or events within their workspace. Notifications are
    ephemeral and may be deleted when they are no longer needed. When a
    user has more than 1,000 pending notifications some old
    notifications will be deleted automatically.
    """

    id: str | None = None
    """
    The unique identifier of this notification
    """

    senderId: str | None = None
    """
    The unique identifier of the sender of this notification
    """

    children: List[NotificationDto] | None = None
    """
    If you received multiple notifications from the same user in a short
    period of time, they will be grouped together. For example, if you
    receive multiple notifications about users joining the same project,
    they will be grouped together in the Children element.
    """

    notificationType: str | None = None
    """
    A friendly category or type for this notification
    """

    createDate: str | None = None
    """
    Timestamp when the notification was sent
    """

    subject: str | None = None
    """
    User readable subject line for the notification
    """

    message: str | None = None
    """
    User readable message content for the notification
    """

    readDate: str | None = None
    """
    Timestamp when the notification was acknowledged as read
    """

    data: NotificationDataDto | None = None
    """
    A string containing JSON-encoded extra data for the notification
    """


