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


from ProjectManagerSdk.models.projectcreateaccessdto import ProjectCreateAccessDto
from dataclasses import dataclass

@dataclass
class ProjectCreateRequestDto:
    """
    A Project is a collection of Tasks that contributes towards a goal.
    Within a Project, Tasks represent individual items of work that team
    members must complete. The sum total of Tasks within a Project
    represents the work to be completed for that Project.
    """

    name: str | None = None
    """
    The name of the Project.
    """

    description: str | None = None
    """
    An optional description of the Project
    """

    folderId: str | None = None
    """
    The unique identifier of the folder of this project, or null if not
    assigned.
    """

    projectAccess: ProjectCreateAccessDto | None = None
    """
    If you wish to grant access to this Project to a selected list of
    people during creation, provide a list of ProjectMembers here. If
    you do not specify anyone, this Project will be available to only
    yourself.
    """

    customerId: str | None = None
    """
    The unique identifier of the customer for this project, or null if
    not customer specific
    """

    managerId: str | None = None
    """
    The unique identifier of the manager of this project, or null if not
    assigned.
    """

    chargeCodeId: str | None = None
    """
    The unique identifier of the ChargeCode for this Project, if one has
    been selected.
    """

    statusId: str | None = None
    """
    The ProjectStatus chosen for this Project, if one has been selected.
    """

    priorityId: str | None = None
    """
    The ProjectPriority level of this Project, if one has been selected.
    """

    hourlyRate: float | None = None
    """
    The default hourly rate for work on this Project. This rate will be
    used if an assignee working on this Project does not have an hourly
    rate configured in their profile.
    """

    budget: float | None = None
    """
    The proposed budget for this Project.
    """

    statusUpdate: str | None = None
    """
    Contains an optional status update for Projects that can be used to
    summarize the status of multiple Projects at a glance. You can edit
    the StatusUpdate field on the Portfolio page of the application.
    """

    template: bool | None = None
    """
    True if this Project is a template that will be reused as a
    framework for future Projects. You can save a Project as a template
    and reuse it in the future for creating additional Projects. If this
    Project is a template, set this to `true` and this template will be
    available to choose from when creating a new Project within the
    application.
    """

    templateId: str | None = None
    """
    The Template that this project should be created from. Specifying a
    TemplateId will copy default settings for Tasks.

    NOTE: This does not support custom templates - TemplateId has to be
    a reference to a static non-Custom template.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
