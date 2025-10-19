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
class AssigneeDto:
    """
    Task assignee dto
    """

    resourceId: str | None = None
    """
    Assignee resource id
    """

    percentAssignment: float | None = None
    """
    Percent of work assigned to task
    """

    assignedEffort: int | None = None
    """
    Effort assigned to the resource for the task.
    """


