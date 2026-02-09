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
class PartialResourceDto:
    """
    PartialResourceDto
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


