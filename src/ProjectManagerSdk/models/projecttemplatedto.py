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


from ProjectManagerSdk.models.projecttemplatecategorydto import ProjectTemplateCategoryDto
from dataclasses import dataclass

@dataclass
class ProjectTemplateDto:
    """
    A ProjectTemplate is a named document that contains default Project
    details. Project Templates are defined for the system and are shared
    among Projects.
    """

    id: str | None = None
    """
    The unique identifier of this ProjectTemplate.
    """

    name: str | None = None
    """
    The name of this ProjectTemplate. Name can de used as a unique text
    reference for Project Templates.
    """

    title: str | None = None
    """
    The title of this ProjectTemplate. Title can be used as a
    description text for Project Templates.
    """

    description: str | None = None
    """
    The full text description of this ProjectTemplate.
    """

    icon: str | None = None
    """
    The icon path for this ProjectTemplate.
    """

    previewImage: str | None = None
    """
    The preview image path for this ProjectTemplate.
    """

    order: int | None = None
    """
    The overall order of this ProjectTemplate. This order only applies
    to non-Custom ProjectTemplates
    """

    isCustom: bool | None = None
    """
    Is this ProjectTemplate a custom template. Custom templates are
    Templates that have been created from existing Project definitions.
    """

    categories: list[ProjectTemplateCategoryDto] | None = None
    """
    The ProjectTemplateCategories that this Project Template belongs to.
    Custom ProjectTemplates do not belong to any
    ProjectTemplateCategories.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
