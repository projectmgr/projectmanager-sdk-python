#
# ProjectManager API for Python
#
# (c) 2023-2023 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  2023-2023 ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#


from dataclasses import dataclass

@dataclass
class TaskAssigneeDto:
    """
    A TaskAssignee is the person to whom a Task is assigned. A single
    Task can be assigned to multiple TaskAssignees.
    """

    id: str | None = None
    """
    The unique identifier of this TaskAssignee
    """

    initials: str | None = None
    """
    A shortened set of initials to use when representing this
    TaskAssignee visually in small areas. The initials may be used in
    small icons or other overlays.
    """

    name: str | None = None
    """
    The name of this TaskAssignee
    """

    description: str | None = None
    """
    A more complete description of the TaskAssignee.
    """

    isActive: bool | None = None
    """
    True if this TaskAssignee is currently active with the Project.
    """

    color: str | None = None
    """
    The color that will be used to represent this TaskAssignee visually.
    You can choose specify any color that can be represented using HTML
    RGB syntax such as `#0088FF`, in the format `RRGGBB`. You may not
    use names for colors.
    """

    firstName: str | None = None
    """
    The first or given name of this TaskAssignee. For personnel
    TaskAssignees only.
    """

    lastName: str | None = None
    """
    The last or family name of this TaskAssignee. For personnel
    TaskAssignees only.
    """

    shortName: str | None = None
    """
    A shortened version of the name of this TaskAssignee. This is used
    in areas where the Initials are too short but the full name is too
    long.
    """

    avatarUrl: str | None = None
    """
    A link to an Avatar for this TaskAssignee. Avatars are small images
    or representations that can be used to visually identify this
    TaskAssignee at a glance.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
