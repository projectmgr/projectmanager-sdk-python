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


from typing import List
import dataclasses

@dataclasses.dataclass
class ProjectUpdateDto:
    """
    A Project is a collection of Tasks that contributes towards a goal.
    Within a Project, Tasks represent individual items of work that team
    members must complete. The sum total of Tasks within a Project
    represents the work to be completed for that Project. Fields that
    cannot be modified during an UpdateProject call are not visible on
    this data model.
    """

    name: str | None = None
    """
    The name of the Project.
    """

    shortName: str | None = None
    """
    The short name of the Project.
    """

    description: str | None = None
    """
    An optional description of the Project
    """

    targetDate: str | None = None
    """
    The target planned completion date for this Project, or null if one
    has not been selected. This value can be updated in the Project
    Settings page or the Portfolio Project page within the application.
    """

    folderId: str | None = None
    """
    To move this Project into a ProjectFolder, set this to the unique
    identifier of the ProjectFolder.
    """

    customerId: str | None = None
    """
    To assign this Project to a ProjectCustomer, set this to the unique
    identifier of the ProjectCustomer. If set to an empty guid the
    Project will be unassigned from the current ProjectCustomer.
    """

    managerId: str | None = None
    """
    To assign this Project to a ProjectManager, set this to the unique
    identifier of the ProjectManager.
    """

    chargeCodeId: str | None = None
    """
    To set the ChargeCode for this Project, set this to the unique
    identifier of the ChargeCode to use for this Project.
    """

    statusId: str | None = None
    """
    To change the ProjectStatus of this Project, set this to the unique
    identifier of the ProjectStatus.
    """

    priorityId: str | None = None
    """
    To change the ProjectPriority of this Project, set this to the
    unique identifier of the ProjectPriority.
    """

    hourlyRate: float | None = None
    """
    To change the hourly rate of this Project, set this to the new
    amount.
    """

    budget: float | None = None
    """
    To change the budget of this Project, set this to the new amount.
    """

    statusUpdate: str | None = None
    """
    To update the Project's status text, set this to the new status
    text.
    """

    favorite: bool | None = None
    """
    Mark this project as favorite for the logged in user.
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

    updatePlannedWithActual: bool | None = None
    """
    True if allow actual dates to update planned dates
    """

    notes: str | None = None
    """
    To update the project notes
    """


