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


from typing import List
import dataclasses

@dataclasses.dataclass
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

    defaultView: str | None = None
    """
    The web default view of the template.
    """


