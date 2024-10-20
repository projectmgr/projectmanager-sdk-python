#
# ProjectManager API for Python
#
# (c) 2023-2024 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  2023-2024 ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#


from typing import List
import dataclasses

@dataclasses.dataclass
class TaskProjectDto:
    """
    A Project is a collection of Tasks that contributes towards a goal.
    Within a Project, Tasks represent individual items of work that team
    members must complete. The sum total of Tasks within a Project
    represents the work to be completed for that Project.
    """

    id: str | None = None
    """
    The unique identifier of this Project.
    """

    shortId: str | None = None
    """
    The ShortId of this Project.
    """

    name: str | None = None
    """
    The common name of this Project.
    """


