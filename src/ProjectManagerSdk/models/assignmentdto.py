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
class AssignmentDto:
    """
    User assigned to task or risk
    """

    taskId: str | None = None
    """
    Task or risk the user is assigned to
    """

    projectId: str | None = None
    """
    The task or risk project Id
    """

    resourceId: str | None = None
    """
    Resource identifier
    """


