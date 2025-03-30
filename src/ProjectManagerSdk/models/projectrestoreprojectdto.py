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
class ProjectRestoreProjectDto:
    """
    This is the projectId being restored to
    """

    id: str | None = None
    """
    The unique identifier of the Project. This value is set by the
    system and cannot be set with a CreateProject or changed with an
    UpdateProject call.
    """


