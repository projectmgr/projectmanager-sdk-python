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


from ProjectManagerSdk.models.projectcreateaccessdto import ProjectCreateAccessDto
from ProjectManagerSdk.models.projectworkingdaysdto import ProjectWorkingDaysDto
from ProjectManagerSdk.models.taskstatuscreatedto import TaskStatusCreateDto
from typing import List
import dataclasses

@dataclasses.dataclass
class ProjectCreateDto:
    """
    A Project is a collection of Tasks that contributes towards a goal.
    Within a Project, Tasks represent individual items of work that team
    members must complete. The sum total of Tasks within a Project
    represents the work to be completed for that Project. Fields that
    cannot be selected during a CreateProject API call are not visible
    on this data model.
    """

    name: str | None = None
    """
    The name of the Project.
    """

    description: str | None = None
    """
    An optional description of the Project
    """

    shortId: str | None = None
    """
    Specify the shortId for this project. If left blank a shortId will
    be generated. A short identifier that uniquely identifies this
    Project within your Workspace using a single letter followed by a
    number. This code can be used for APIs that accept Project unique
    identifiers. You can observe the short ID within the application by
    observing the URL of the page you visit when you click on this
    project. The page's URL will appear in the form
    `https://pm.app.projectmanager.com/project/board/D16` - in this
    example, the `ShortId` is `D16`. This id can only be set on
    creation, and can not be updated.
    """

    shortName: str | None = None
    """
    An optional project short name. Up to 7 symbols
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

    templateId: str | None = None
    """
    When creating a Project, you can optionally specify a Template to
    use to construct the Project using a collection of pre-designed
    Tasks. Specifying a value in the TemplateId field will copy default
    settings for Tasks from your template Project into the newly created
    Project. This field does not support custom templates. You must
    choose from a list of ProjectManager-supplied templates.
    """

    targetDate: str | None = None
    """
    The target planned completion date for this Project, or null if one
    has not been selected. This value can be updated in the Project
    Settings page or the Portfolio Project page within the application.
    """

    favorite: bool | None = None
    """
    True if this Project is marked as favorite for current user
    """

    updatePlannedWithActual: bool | None = None
    """
    True if allow actual dates to update planned dates
    """

    taskStatusCreate: List[TaskStatusCreateDto] | None = None
    """
    Create default task status upfront
    """

    workingDays: ProjectWorkingDaysDto | None = None
    """
    Working days for the project. If not specified, the workspace
    working days will be used. This value can be set when the project is
    created but may not be updated afterwards.
    """


