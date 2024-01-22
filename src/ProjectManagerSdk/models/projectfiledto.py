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


from ProjectManagerSdk.models.projectfiletaskdto import ProjectFileTaskDto
from dataclasses import dataclass

@dataclass
class ProjectFileDto:

    id: str | None = None
    """
    The identifier for this file
    """

    name: str | None = None
    """
    The name of the file
    """

    url: str | None = None
    """
    The url of the file which can be used for downloading
    """

    task: ProjectFileTaskDto | None = None
    """
    The project task that this file relates to. This field will be
    present when you fetch a single object. When you query for multiple
    objects, this field is not included in results by default. To expand
    this field, specify the name of this field in the `$expand`
    parameter.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
