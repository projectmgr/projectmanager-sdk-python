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
class ResourceWorkloadTaskAssignmentDto:
    """
    Details about the TaskAssignment a workload allocation belongs to.
    Only populated when the request specifies `include=taskAssignment`.
    """

    id: str | None = None
    """
    The unique identifier of the TaskAssignment.
    """

    totalAssignedMinutes: int | None = None
    """
    The total number of minutes assigned to this Resource across all of
    this TaskAssignment's allocations.
    """


