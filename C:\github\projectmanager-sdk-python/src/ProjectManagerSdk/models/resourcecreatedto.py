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
class ResourceCreateDto:
    """
    A Resource represents a person, material, or tool that is used
    within your Projects. When you attach a Resources to more than one
    Task, the software will schedule the usage of your Resource so that
    it is not allocated to more than one Task at the same time. The
    users in your Workspace are also considered Resources. To invite a
    new User to your Workspace, create a new Resource for that user.
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

    countryCode: str | None = None
    """
    A text field indicating the country in which this Resource is
    located. This value must be one of the following: US, NZ, AU.
    """

    notes: str | None = None
    """
    Free-form text notes about this Resource. You may use this field to
    store extra information about the Resource.
    """

    roleId: str | None = None
    """
    The Role Id associated with this Resource. Applies to personnel
    Resources only.
    """

    teamIds: List[str] | None = None
    """
    The list of ResourceTeams to which this Resource belongs.
    """

    skillIds: List[str] | None = None
    """
    The list of ResourceSkills possessed by this Resource.
    """

    colorName: str | None = None
    """
    Collaboration Color for this resource. eg. teal, cyan, lightblue,
    blurple, purple, pink, orange, gray
    """

    country: str | None = None
    """
    Deprecated - this property is no longer being used. Please pass in
    Country data on the CountryCode property. A text field indicating
    the country in which this Resource is located. This value is not
    constrained to the list of known ISO 3166 country names or codes.
    """

    role: str | None = None
    """
    Deprecated - this property is no longer being used. Please pass in
    Role data on the RoleId property The Role privileges associated with
    this Resource. Applies to personnel Resources only.
    """

    teams: List[str] | None = None
    """
    Deprecated - this property is no longer being used. Please pass in
    Team data on the TeamIds property The list of ResourceTeams to which
    this Resource belongs.
    """

    skills: List[str] | None = None
    """
    Deprecated - this property is no longer being used. Please pass in
    Skill data on the SkillIds property The list of ResourceSkills
    possessed by this Resource.
    """


