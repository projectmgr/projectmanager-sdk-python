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
class NptAssigneeDto:
    """
    A NptAssignee is a Resource to whom a Npt is assigned. A single Npt
    can be assigned to multiple NptAssignee.
    """

    id: str | None = None
    """
    The unique identifier of this Resource
    """

    initials: str | None = None
    """
    A shortened set of initials to use when representing this
    NptAssignee visually in small areas. The initials may be used in
    small icons or other overlays.
    """

    name: str | None = None
    """
    The name of this NptAssignee
    """

    description: str | None = None
    """
    A more complete description of the NptAssignee.
    """

    isActive: bool | None = None
    """
    True if this NptAssignee is currently active with the Project.
    """

    colorName: str | None = None
    """
    Collaboration Color for this resource. eg. teal, cyan, lightblue,
    blurple, purple, pink, orange, gray
    """

    firstName: str | None = None
    """
    The first or given name of this NptAssignee. For personnel
    NptAssignees only.
    """

    lastName: str | None = None
    """
    The last or family name of this NptAssignee. For personnel
    NptAssignees only.
    """

    shortName: str | None = None
    """
    A shortened version of the name of this NptAssignee. This is used in
    areas where the Initials are too short but the full name is too
    long.
    """

    avatarUrl: str | None = None
    """
    A link to an Avatar for this NptAssignee. Avatars are small images
    or representations that can be used to visually identify this
    NptAssignee at a glance.
    """

    email: str | None = None
    """
    The email address for the resource. It can be empty if the resource
    does not have a login.
    """


