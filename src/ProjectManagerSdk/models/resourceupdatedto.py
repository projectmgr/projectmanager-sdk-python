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
class ResourceUpdateDto:
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
    The email address of this Resource. Note that this email cannot be
    changed once it has been assigned.
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

    teamIds: list[str] | None = None
    """
    The list of ResourceTeams to which this Resource belongs.
    """

    skillIds: list[str] | None = None
    """
    The list of ResourceSkills possessed by this Resource.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
