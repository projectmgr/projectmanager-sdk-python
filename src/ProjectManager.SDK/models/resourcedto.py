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
    firstName: str | None = None
    lastName: str | None = None
    email: str | None = None
    hourlyRate: float | None = None
    phone: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    notes: str | None = None
    approver: ResourceApproverDto | None = None
    teams: list[ResourceTeamDto] | None = None
    skills: list[ResourceSkillDto] | None = None
    onlineDateTime: str | None = None
    role: str | None = None
    isActive: bool | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
