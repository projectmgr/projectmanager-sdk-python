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


from ProjectManagerSdk.models.resourceworkingdayshours import ResourceWorkingDaysHours
from typing import List
import dataclasses

@dataclasses.dataclass
class ResourceBulkUpdateDto:
    """
    Represents the values to apply to a single Resource as part of a
    bulk Resource update API call. This is a deliberately reduced
    version of Astro.Api.Dto.Resources.ResourceUpdateDto. Only fields
    that are sensible to update across many Resources at once are
    included. The following fields are intentionally omitted because
    they represent per-person identity or carry per-Resource side
    effects that should not be applied in bulk: - Email: cannot be
    changed once assigned and is unique per person. - RoleId: triggers
    invite-permission, account-owner and last-global-admin logic. -
    IsActive: triggers last-global-admin and license-count logic. -
    HourlyRate: triggers workspace-wide hourly rate recalculations. -
    ClearAvatar: removes the stored avatar image and deletes the asset
    from S3.
    """

    resourceId: str | None = None
    """
    The unique identifier of the Resource to update.
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

    teamIds: List[str] | None = None
    """
    The list of ResourceTeams to which this Resource belongs.
    """

    skillIds: List[str] | None = None
    """
    The list of ResourceSkills possessed by this Resource.
    """

    approverId: str | None = None
    """
    The Approver Id associated with this Resource. Applies to personnel
    Resources only.
    """

    colorName: str | None = None
    """
    Collaboration Color for this resource. eg. teal, cyan, lightblue,
    blurple, purple, pink, orange, gray
    """

    language: str | None = None
    """
    Translation Language for this resource. e.g. en-US, en-GB, fr-FR,
    es-ES
    """

    publicAvatarId: int | None = None
    """
    Public avatar image index (1-42). The avatar URL is generated as
    /assets/images/avatars/{index:000}.png. Only numeric public avatars
    are accepted; custom URLs are not supported.
    """

    defaultPlannedHours: float | None = None
    """
    Default planned effort in hours. When set, updates the resource;
    when omitted, existing value is unchanged.
    """

    workingDays: ResourceWorkingDaysHours | None = None
    """
    Per-day working hours. When non-null, updates or creates the
    resource calendar; set only days to change—they merge over workspace
    defaults.
    """


