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
class TaskCreateDto:
    """
    A Task is an individual element of work that must be performed to
    complete a Project. A Task can have one or more Resources assigned
    to it. Tasks can be linked to other Tasks to indicate whether they
    have a dependency or a connection.
    """

    id: str | None = None
    name: str | None = None
    description: str | None = None
    parentTaskId: str | None = None
    percentComplete: int | None = None
    statusId: str | None = None
    priorityId: int | None = None
    assignees: list[str] | None = None
    plannedStartDate: str | None = None
    plannedFinishDate: str | None = None
    plannedDuration: int | None = None
    plannedEffort: int | None = None
    plannedCost: float | None = None
    actualStartDate: str | None = None
    actualCost: float | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
