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
class TaskDetailsDto:
    """
    A Task is an individual element of work that must be performed to
    complete a Project. A Task can have one or more Resources assigned
    to it. Tasks can be linked to other Tasks to indicate whether they
    have a dependency or a connection.
    """

    id: str | None = None
    project: TaskProjectDto | None = None
    tags: list[TaskTagDto] | None = None
    assignees: list[TaskAssigneeDto] | None = None
    todos: list[TaskTodoDto] | None = None
    shortId: str | None = None
    name: str | None = None
    description: str | None = None
    status: TaskStatusDto | None = None
    priorityId: int | None = None
    plannedStartDate: str | None = None
    plannedFinishDate: str | None = None
    actualStartDate: str | None = None
    actualFinishDate: str | None = None
    modifyDate: str | None = None
    createDate: str | None = None
    percentComplete: int | None = None
    isSummary: bool | None = None
    wbs: str | None = None
    actualCost: float | None = None
    plannedCost: float | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
