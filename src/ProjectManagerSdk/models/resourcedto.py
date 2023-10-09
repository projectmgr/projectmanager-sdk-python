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


from ProjectManagerSdk.models.resourceapproverdto import ResourceApproverDto
from ProjectManagerSdk.models.resourceskilldto import ResourceSkillDto
from ProjectManagerSdk.models.resourceteamdto import ResourceTeamDto
from dataclasses import dataclass

@dataclass
class ResourceDto:
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
    The email address of this Resource.
    """

    hourlyRate: float | None = None
    """
    The basic hourly rate for this Resource.
    """

    phone: str | None = None
    """
    The phone number associated with this Resource.
    """

    city: str | None = None
    """
    The city where this Resource is located.
    """

    state: str | None = None
    """
    The state or region where this Resource is located. This value is
    not constrained to a list of known states or regions.
    """

    country: str | None = None
    """
    A text field indicating the country in which this Resource is
    located. This value is not constrained to the list of known ISO 3166
    country names or codes.
    """

    notes: str | None = None
    """
    Free-form text notes about this Resource. You may use this field to
    store extra information about the Resource.
    """

    approver: ResourceApproverDto | None = None
    """
    When managing users, you can choose who will approve a person's
    Timesheets. This is a ResourceApprover. You can specify this person
    within the Resource object.
    """

    teams: list[ResourceTeamDto] | None = None
    """
    The list of ResourceTeams to which this Resource belongs.
    """

    skills: list[ResourceSkillDto] | None = None
    """
    The list of ResourceSkills possessed by this Resource.
    """

    onlineDateTime: str | None = None
    """
    The last time when this Resource was online. Applies to personnel
    Resources only.
    """

    role: str | None = None
    """
    The Role privileges associated with this Resource. Applies to
    personnel Resources only.
    """

    isActive: bool | None = None
    """
    True if this Resource is currently active and valid. If this value
    is false, this Resource is considered to be deactivated and not
    available for further use. For personnel Resources, setting this
    value to False will make this user unable to access this Workspace.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
