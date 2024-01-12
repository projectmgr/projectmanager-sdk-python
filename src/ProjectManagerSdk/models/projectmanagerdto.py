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


from dataclasses import dataclass

@dataclass
class ProjectManagerDto:
    """
    A ProjectManager is a person who manages a Project.
    """

    id: str | None = None
    """
    The unique identifier of this ProjectManager
    """

    name: str | None = None
    """
    The name of this ProjectManager
    """

    initials: str | None = None
    """
    Manager initials
    """

    avatarUrl: str | None = None
    """
    Avatar's url
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
