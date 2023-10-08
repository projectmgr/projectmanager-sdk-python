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
class ProjectCreateRequestDto:
    """
    A Project is a collection of Tasks that contributes towards a goal.
    Within a Project, Tasks represent individual items of work that team
    members must complete. The sum total of Tasks within a Project
    represents the work to be completed for that Project.
    """

    name: str | None = None
    description: str | None = None
    folderId: str | None = None
    projectAccess: ProjectCreateAccessDto | None = None
    customerId: str | None = None
    managerId: str | None = None
    chargeCodeId: str | None = None
    statusId: str | None = None
    priorityId: str | None = None
    hourlyRate: float | None = None
    budget: float | None = None
    statusUpdate: str | None = None
    template: bool | None = None
    templateId: str | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
