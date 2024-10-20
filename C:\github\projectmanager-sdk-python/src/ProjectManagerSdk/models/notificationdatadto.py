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
class NotificationDataDto:
    """
    Contains the optional data associated with the notifcation.
    """

    taskId: str | None = None
    """
    Set if the notification is related to a task
    """

    projectId: str | None = None
    """
    Set if the notification is related to a project
    """

    taskShortId: str | None = None
    """
    set if the notification is related to a task
    """

    projectShortId: str | None = None
    """
    set if the notification is related to a project
    """

    projectName: str | None = None
    """
    Name of the project the notification is related to
    """

    taskName: str | None = None
    """
    Name of the task this notification is related to
    """

    senderFirstName: str | None = None
    """
    Firstname of the person initiating the notification
    """

    assigneeId: str | None = None
    """
    Assignee for the notification
    """

    view: str | None = None
    """
    View
    """

    shareId: str | None = None
    """
    Id for the shared item
    """

    fileName: str | None = None
    """
    Name of the file
    """


