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

from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.notificationresponsedto import NotificationResponseDto
from ProjectManagerSdk.models.notificationtimestampdto import NotificationTimestampDto
from ProjectManagerSdk.models.notificationtotalcountdto import NotificationTotalCountDto
from ProjectManagerSdk.models.notificationunreadcountdto import NotificationUnreadCountDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class NotificationClient:
    """
    API methods related to Notification
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_notifications(self, lastId: str, senderId: str, notificationTypes: List[str], asFlatList: bool) -> AstroResult[NotificationResponseDto]:
        """
        Retrieve the most recent notifications for the current user,
        along with the amount of notifications. A notification
        represents a message sent to a user to inform them of relevant
        actions or events within their workspace. Notifications are
        ephemeral and may be deleted when they are no longer needed.
        When a user has more than 1,000 pending notifications some old
        notifications will be deleted automatically. This API retrieves
        500 notifications at a time. To fetch more than 500
        notifications, repeat this API call using the parameter `lastId`
        of the oldest notification from each batch to fetch the next 500
        notifications.

        Parameters
        ----------
        lastId : str
            To continue loading more notifications in a series of
            requests, provide the ID of the oldest notification from the
            currently loaded batch as the `lastId` parameter
        senderId : str
            Filter the notifications to only those sent by the user with
            the specified ID
        notificationTypes : List[str]
            Specifies the types of notifications to return. If not
            provided, all notifications will be returned.
        asFlatList : bool
            If set to true all notifications will be returned as a flat
            list, otherwise they will be grouped by parent in the same
            manner as displayed in the UI.
        """
        path = "/api/data/notifications"
        queryParams = {}
        if lastId:
            queryParams['lastId'] = lastId
        if senderId:
            queryParams['senderId'] = senderId
        if notificationTypes:
            queryParams['notificationTypes'] = notificationTypes
        if asFlatList:
            queryParams['asFlatList'] = asFlatList
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=NotificationResponseDto, data=json.loads(result.content)['data'])
            return AstroResult[NotificationResponseDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[NotificationResponseDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def notification_count(self) -> AstroResult[NotificationTotalCountDto]:
        """
        Retrieve the total count of pending notifications for the
        current user. A notification represents a message sent to a user
        to inform them of relevant actions or events within their
        workspace. Notifications are ephemeral and may be deleted when
        they are no longer needed. When a user has more than 1,000
        pending notifications some old notifications will be deleted
        automatically.

        Parameters
        ----------
        """
        path = "/api/data/notifications/count"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=NotificationTotalCountDto, data=json.loads(result.content)['data'])
            return AstroResult[NotificationTotalCountDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[NotificationTotalCountDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def unread_notification_count(self) -> AstroResult[NotificationUnreadCountDto]:
        """
        Retrieve the count of unread notifications for the current user.
        A notification represents a message sent to a user to inform
        them of relevant actions or events within their workspace.
        Notifications are ephemeral and may be deleted when they are no
        longer needed. When a user has more than 1,000 pending
        notifications some old notifications will be deleted
        automatically.

        Parameters
        ----------
        """
        path = "/api/data/notifications/unreadcount"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=NotificationUnreadCountDto, data=json.loads(result.content)['data'])
            return AstroResult[NotificationUnreadCountDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[NotificationUnreadCountDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_all_notifications(self) -> AstroResult[object]:
        """
        Delete all pending notifications for the current user. A
        notification represents a message sent to a user to inform them
        of relevant actions or events within their workspace.
        Notifications are ephemeral and may be deleted when they are no
        longer needed. When a user has more than 1,000 pending
        notifications some old notifications will be deleted
        automatically.

        Parameters
        ----------
        """
        path = "/api/data/notifications/deleteall"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def mark_notification_read(self, id: str) -> AstroResult[NotificationTimestampDto]:
        """
        Marks a pending notification as read. A notification represents
        a message sent to a user to inform them of relevant actions or
        events within their workspace. Notifications are ephemeral and
        may be deleted when they are no longer needed. When a user has
        more than 1,000 pending notifications some old notifications
        will be deleted automatically.

        Parameters
        ----------
        id : str
            The unique identifier of the notification to mark read
        """
        path = f"/api/data/notifications/{id}/markread"
        queryParams = {}
        result = self.client.send_request("POST", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=NotificationTimestampDto, data=json.loads(result.content)['data'])
            return AstroResult[NotificationTimestampDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[NotificationTimestampDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def read_all_notifications(self) -> AstroResult[NotificationTimestampDto]:
        """
        Marks all pending notification for the current user as read. A
        notification represents a message sent to a user to inform them
        of relevant actions or events within their workspace.
        Notifications are ephemeral and may be deleted when they are no
        longer needed. When a user has more than 1,000 pending
        notifications some old notifications will be deleted
        automatically.

        Parameters
        ----------
        """
        path = "/api/data/notifications/markallread"
        queryParams = {}
        result = self.client.send_request("POST", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=NotificationTimestampDto, data=json.loads(result.content)['data'])
            return AstroResult[NotificationTimestampDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[NotificationTimestampDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_notification(self, id: str) -> AstroResult[object]:
        """
        Deletes a pending notification that is no longer wanted. A
        notification represents a message sent to a user to inform them
        of relevant actions or events within their workspace.
        Notifications are ephemeral and may be deleted when they are no
        longer needed. When a user has more than 1,000 pending
        notifications some old notifications will be deleted
        automatically.

        Parameters
        ----------
        id : str
            The unique identifier of the notification to mark read
        """
        path = f"/api/data/notifications/delete/{id}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def mark_notification_unread(self, id: str) -> AstroResult[object]:
        """
        Marks a pending notification as unread. A notification
        represents a message sent to a user to inform them of relevant
        actions or events within their workspace. Notifications are
        ephemeral and may be deleted when they are no longer needed.
        When a user has more than 1,000 pending notifications some old
        notifications will be deleted automatically.

        Parameters
        ----------
        id : str
            The unique identifier of the notification to mark read
        """
        path = f"/api/data/notifications/{id}/markunread"
        queryParams = {}
        result = self.client.send_request("POST", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
