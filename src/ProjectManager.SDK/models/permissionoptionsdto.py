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
class PermissionOptionsDto:
    """
    Specifies the permissions a member can be changed to on a project.
    This objects values can change based on the logged in user and the
    role they have.
    """

    none: bool | None = None
    collaborate: bool | None = None
    guest: bool | None = None
    editor: bool | None = None
    manager: bool | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
