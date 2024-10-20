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
class ProjectVersionChangeDataDto:
    """
    A ProjectVersionChangeData is information about a change made to a
    Project that took it from one Version to another. The information in
    this object can help track the details of changes made by the user.
    """

    type: str | None = None
    """
    The type of change made
    """

    method: str | None = None
    """
    The method used to make the change
    """

    property: str | None = None
    """
    The property that was changed, if any
    """

    value: str | None = None
    """
    The new value of the property, or null if the property was cleared
    """

    restoreVersion: int | None = None
    """
    The prior version number to restore to
    """


