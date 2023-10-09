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
class ResourceTeamDto:
    """
    A ResourceTeam is a group of Resources that can be referred to as a
    group. You can use a ResourceTeam as a shortcut to quickly assign or
    allocate multiple Resources quickly.
    """

    id: str | None = None
    """
    The unique identifier of this ResourceTeam
    """

    name: str | None = None
    """
    The name of this ResourceTeam
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
