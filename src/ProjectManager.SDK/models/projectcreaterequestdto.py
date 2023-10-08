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

    name: object | None = None
    description: object | None = None
    folderId: object | None = None
    projectAccess: object | None = None
    customerId: object | None = None
    managerId: object | None = None
    chargeCodeId: object | None = None
    statusId: object | None = None
    priorityId: object | None = None
    hourlyRate: object | None = None
    budget: object | None = None
    statusUpdate: object | None = None
    template: object | None = None
    templateId: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
