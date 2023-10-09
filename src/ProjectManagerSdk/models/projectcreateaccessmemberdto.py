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
class ProjectCreateAccessMemberDto:
    """
    Represents project member that have access to new project
    """

    userId: str | None = None
    """
    Member's id
    """

    permission: str | None = None
    """
    Member's role in the project
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
