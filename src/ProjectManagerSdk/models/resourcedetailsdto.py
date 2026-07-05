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


from ProjectManagerSdk.models.idnamedto import IdNameDto
from ProjectManagerSdk.models.resourceapproverdto import ResourceApproverDto
from ProjectManagerSdk.models.resourceskilldto import ResourceSkillDto
from ProjectManagerSdk.models.resourceteamdto import ResourceTeamDto
from ProjectManagerSdk.models.resourceworkingdayshours import ResourceWorkingDaysHours
from typing import List
import dataclasses

@dataclasses.dataclass
class ResourceDetailsDto:
    """
    An extended view of a Resource returned when retrieving a single
    Resource. Includes everything on Astro.Api.Dto.Resources.ResourceDto
    plus additional profile details that are only surfaced for an
    individual Resource, such as the Projects the Resource has access
    to.
    """

    id: str | None = None
    """
    The unique identifier of this Resource.
    """

    initials: str | None = None
    """
    The resource initials.
    """

    name: str | None = None
    """
    The name of the Resource. Usually this is the same as the FirstName
    and LastName
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

    countryName: str | None = None
    """
    Returns the name of the country
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

    teams: List[ResourceTeamDto] | None = None
    """
    The list of ResourceTeams to which this Resource belongs.
    """

    skills: List[ResourceSkillDto] | None = None
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

    roleId: str | None = None
    """
    The unique identifier of the Role associated with this Resource.
    Applies to personnel Resources only.
    """

    isActive: bool | None = None
    """
    True if this Resource is currently active and valid. If this value
    is false, this Resource is considered to be deactivated and not
    available for further use. For personnel Resources, setting this
    value to False will make this user unable to access this Workspace.
    """

    createdDate: str | None = None
    """
    The date this resource was created
    """

    createdBy: str | None = None
    """
    Set to a unique identifier of the user who created this Resource.
    """

    modifiedDate: str | None = None
    """
    The date this resource was last modified
    """

    modifiedBy: str | None = None
    """
    Set to a unique identifier of the user who last modified this
    Resource.
    """

    colorName: str | None = None
    """
    Collaboration Color for this resource. eg. teal, cyan, lightblue,
    blurple, purple, pink, orange, gray
    """

    color: str | None = None
    """
    Read only Hex code of the ColorName
    """

    avatarUrl: str | None = None
    """
    The resources avatar url, if any.
    """

    language: str | None = None
    """
    The language preference for this Resource, used for localization and
    communication.
    """

    resourceTypeId: int | None = None
    """
    The type identifier for this Resource. 1 = Resource (standard
    resource), 2 = Sample (sample resource).
    """

    defaultPlannedHours: float | None = None
    """
    Default planned effort for this resource, in hours (stored as whole
    minutes server-side).
    """

    workingDays: ResourceWorkingDaysHours | None = None
    """
    Hours available per weekday for scheduling (whole hours per day;
    matches workspace/resource calendar rows).
    """

    projectMembership: List[IdNameDto] | None = None
    """
    The list of Projects this Resource has access to, each as an id and
    name. Returns an empty array when the Resource does not have access
    to any Projects.
    """


