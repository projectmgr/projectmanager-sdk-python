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
class ProjectCreateResponseDto:
    """
    A Project is a collection of Tasks that contributes towards a goal.
    Within a Project, Tasks represent individual items of work that team
    members must complete. The sum total of Tasks within a Project
    represents the work to be completed for that Project.
    """

    id: str | None = None
    """
    The unique identifier of the project of this project, or null if not
    assigned.
    """

    shortId: str | None = None
    """
    The unique identifier of the shortid of this project, or null if not
    assigned.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
