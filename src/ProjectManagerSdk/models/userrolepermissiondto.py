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
class UserRolePermissionDto:
    """
    The basic permission object
    """

    description: str | None = None
    """
    The description of the permission
    """

    value: bool | None = None
    """
    True if the permission is on
    """

    canBeModified: bool | None = None
    """
    If true this permission can be turned on or off for this role. Most
    roles can have all permissions modified, but some roles have all or
    some permissions fixed.
    """


