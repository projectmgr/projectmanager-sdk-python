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
class ProjectPriorityDto:
    """
    A ProjectPriority is a named priority level used by your business to
    determine how to decide which Tasks are the most important. You can
    name your ProjectPriority levels anything you like and you can
    reorganize the order of the ProjectPriority levels at any time.
    """

    id: str | None = None
    """
    The unique identifier of this ProjectPriority.
    """

    name: str | None = None
    """
    The name of this ProjectPriority.
    """


