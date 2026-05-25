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
class TaskStatusUpdateObsoleteDto:

    name: str | None = None
    """
    The name of this TaskStatus.
    """

    order: int | None = None
    """
    A numerical value that can be used to sort TaskStatus values
    according to the needs of your business.
    """

    id: str | None = None
    """
    The unique identifier of this TaskStatus.
    """


