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
class ProjectTemplateDto:
    """
    A ProjectTemplate is a named document that contains default Project
    details. Project Templates are defined for the system and are shared
    among Projects.
    """

    id: str | None = None
    name: str | None = None
    title: str | None = None
    description: str | None = None
    icon: str | None = None
    previewImage: str | None = None
    order: int | None = None
    isCustom: bool | None = None
    categories: list[ProjectTemplateCategoryDto] | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
