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
class ProjectDto:
    """
    A Project is a collection of Tasks that contributes towards a goal.
    Within a Project, Tasks represent individual items of work that team
    members must complete. The sum total of Tasks within a Project
    represents the work to be completed for that Project.
    """

    id: object | None = None
    name: object | None = None
    description: object | None = None
    shortCode: object | None = None
    shortId: object | None = None
    folder: object | None = None
    status: object | None = None
    startDate: object | None = None
    endDate: object | None = None
    targetDate: object | None = None
    priority: object | None = None
    chargeCode: object | None = None
    manager: object | None = None
    customer: object | None = None
    budget: object | None = None
    hourlyRate: object | None = None
    statusUpdate: object | None = None
    modifyDate: object | None = None
    createDate: object | None = None
    isTemplate: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
