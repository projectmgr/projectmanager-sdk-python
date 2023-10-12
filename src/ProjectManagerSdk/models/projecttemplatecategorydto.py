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


from ProjectManagerSdk.models.projecttemplatedto import ProjectTemplateDto
from dataclasses import dataclass

@dataclass
class ProjectTemplateCategoryDto:
    """
    Information about a Category of ProjectTemplates.
    """

    id: str | None = None
    """
    The unique identifier of this ProjectTemplate Category.
    """

    name: str | None = None
    """
    A friendly name for this ProjectTemplate Category.
    """

    order: int | None = None
    """
    The overall order of this ProjectTemplate Category
    """

    templates: list[ProjectTemplateDto] | None = None
    """
    A list of templates in this category
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
