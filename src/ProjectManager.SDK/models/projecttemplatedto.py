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

    id: object | None = None
    name: object | None = None
    title: object | None = None
    description: object | None = None
    icon: object | None = None
    previewImage: object | None = None
    order: object | None = None
    isCustom: object | None = None
    categories: list[object] | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
