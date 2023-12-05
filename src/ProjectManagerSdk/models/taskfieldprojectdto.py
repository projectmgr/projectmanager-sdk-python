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
class TaskFieldProjectDto:
    """
    The TaskFieldProject is a summary of the Project that this TaskField
    relates to.
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


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
