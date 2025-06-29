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
class TaskOwnerDto:
    """
    A Resource represents a person, material, or tool that is used
    within your Projects. When you attach a Resources to more than one
    Task, the software will schedule the usage of your Resource so that
    it is not allocated to more than one Task at the same time. The
    users in your Workspace are also considered Resources. To invite a
    new User to your Workspace, create a new Resource for that user.
    """

    id: str | None = None
    """
    The unique identifier of this Resource.
    """

    initials: str | None = None
    """
    The resource initials.
    """

    firstName: str | None = None
    """
    The first name of the person Resource. Applies to personnel
    Resources only.
    """

    lastName: str | None = None
    """
    The last name of the person Resource. Applies to personnel Resources
    only.
    """

    email: str | None = None
    """
    If this Resource is a person who can log on to ProjectManager.com,
    this value should be the email address of the person. If this
    Resource is not a person, but you wish to receive email alerts for
    usage of this Resource, you can also add an email address here and
    notifications will be sent when this Resource is used. Otherwise
    this value should be `null`.
    """

    isActive: bool | None = None
    """
    True if this Resource is currently active and valid. If this value
    is false, this Resource is considered to be deactivated and not
    available for further use. For personnel Resources, setting this
    value to False will make this user unable to access this Workspace.
    """

    color: str | None = None
    """
    Read only Hex code of the ColorName
    """

    avatarUrl: str | None = None
    """
    The resources avatar url, if any.
    """


