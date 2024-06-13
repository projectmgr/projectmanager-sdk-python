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


from ProjectManagerSdk.models.projectchargecodedto import ProjectChargeCodeDto
from ProjectManagerSdk.models.projectcustomerdto import ProjectCustomerDto
from ProjectManagerSdk.models.projectfieldvaluedto import ProjectFieldValueDto
from ProjectManagerSdk.models.projectfiledto import ProjectFileDto
from ProjectManagerSdk.models.projectfolderdto import ProjectFolderDto
from ProjectManagerSdk.models.projectmanagerdto import ProjectManagerDto
from ProjectManagerSdk.models.projectmemberdto import ProjectMemberDto
from ProjectManagerSdk.models.projectprioritydto import ProjectPriorityDto
from ProjectManagerSdk.models.projectstatusdto import ProjectStatusDto
from typing import List
import dataclasses

@dataclasses.dataclass
class ProjectDto:
    """
    A Project is a collection of Tasks that contributes towards a goal.
    Within a Project, Tasks represent individual items of work that team
    members must complete. The sum total of Tasks within a Project
    represents the work to be completed for that Project.
    """

    id: str | None = None
    """
    The unique identifier of the Project. This value is set by the
    system and cannot be set with a CreateProject or changed with an
    UpdateProject call.
    """

    name: str | None = None
    """
    The name of the Project.
    """

    description: str | None = None
    """
    An optional description of the Project
    """

    shortCode: str | None = None
    """
    A shortened name that will be used when reporting on Projects. This
    short name can be edited in the Project Settings page within the
    application and can be any text you wish.
    """

    shortId: str | None = None
    """
    A short identifier that uniquely identifies this Project within your
    Workspace using a single letter followed by a number. This code can
    be used for APIs that accept Project unique identifiers. You can
    observe the short ID within the application by observing the URL of
    the page you visit when you click on this project. The page's URL
    will appear in the form `https://pm.app.projectmanager.com/project/board/D16`
    - in this example, the `ShortId` is `D16`. This code is
    automatically assigned for you and cannot be changed.
    """

    folder: ProjectFolderDto | None = None
    """
    If this Project is grouped within a ProjectFolder, this contains the
    ProjectFolder information.
    """

    status: ProjectStatusDto | None = None
    """
    The ProjectStatus chosen for this Project.
    """

    startDate: str | None = None
    """
    The earliest planned or actual start date of tasks on the project.
    This field is calculated automatically and cannot be changed.
    """

    endDate: str | None = None
    """
    The latest planned or actual finish date of tasks on the project.
    This field is calculated automatically and cannot be changed.
    """

    targetDate: str | None = None
    """
    The target planned completion date for this Project, or null if one
    has not been selected. This value can be updated in the Project
    Settings page or the Portfolio Project page within the application.
    """

    plannedStartDate: str | None = None
    """
    A calculated field of the estimated date on which this Project is
    expected to start. This date is calculated based on the earliest
    estimated start date for a Task within this Project. This value is
    null if no Tasks have an estimated start date within this Project.
    """

    plannedFinishDate: str | None = None
    """
    A calculated field of the estimated date on which this Project is
    expected to finish. This date is calculated based on the latest
    planned finish date for a Task within this Project. This value is
    null if no Tasks have an estimated finish date within this Project.
    """

    actualStartDate: str | None = None
    """
    A calculated field of the actual date on which this Project started.
    This date is calculated based on the earliest actual start date for
    a Task within this Project. This value is null if no Tasks have an
    actual start date within this Project.
    """

    actualFinishDate: str | None = None
    """
    A calculated field of the actual date on which this Project
    finished.

    This date is calculated based on the latest actual finish date for a
    Task within this Project. This value is null if no Tasks have an
    actual finish date within this Project.
    """

    priority: ProjectPriorityDto | None = None
    """
    The ProjectPriority level of this Project, if defined.
    """

    chargeCode: ProjectChargeCodeDto | None = None
    """
    The ChargeCode of this Project, if defined.
    """

    manager: ProjectManagerDto | None = None
    """
    Information about the manager of this project, if one has been
    assigned.
    """

    customer: ProjectCustomerDto | None = None
    """
    Information about the manager of this project, if one has been
    specified.
    """

    budget: float | None = None
    """
    The proposed budget for this Project.
    """

    hourlyRate: float | None = None
    """
    The default hourly rate for work on this Project. This rate will be
    used if an assignee working on this Project does not have an hourly
    rate configured in their profile.
    """

    statusUpdate: str | None = None
    """
    Contains an optional status update for Projects that can be used to
    summarize the status of multiple Projects at a glance. You can edit
    the StatusUpdate field on the Portfolio page of the application.
    """

    modifyDate: str | None = None
    """
    The timestamp in UTC when the Project was most recently modified.
    This field is automatically determined by the system when this
    Project is modified and cannot be directly changed by the user.
    """

    createDate: str | None = None
    """
    The timestamp in UTC when the Project was created. This field is
    automatically determined by the system when this Project is created
    and cannot be changed by the user.
    """

    isTemplate: bool | None = None
    """
    True if this Project is a template that will be reused as a
    framework for future Projects.
    """

    favorite: bool | None = None
    """
    True if this Project is marked as favorite for current user
    """

    creationTemplateId: str | None = None
    """
    The TemplateId that this project was created from. Will be null if
    no template was selected at project creation.
    """

    members: List[ProjectMemberDto] | None = None
    """
    The members of the project
    """

    fields: object | None = None
    """
    Obsolete - use FieldValues instead
    """

    fieldValues: List[ProjectFieldValueDto] | None = None
    """
    Project fields array with values
    """

    files: List[ProjectFileDto] | None = None
    """
    The list of files associated with this Project, if any. This field
    will be present when you fetch a single object. When you query for
    multiple objects, this field is not included in results by default.
    To expand this field, specify the name of this field in the
    `$expand` parameter.
    """

    percentComplete: int | None = None
    """
    The percentage of the project tasks completed
    """


