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


from __future__ import annotations
from ProjectManagerSdk.models.iedmdirectvalueannotationsmanager import IEdmDirectValueAnnotationsManager
from ProjectManagerSdk.models.iedmentitycontainer import IEdmEntityContainer
from ProjectManagerSdk.models.iedmmodel import IEdmModel
from ProjectManagerSdk.models.iedmschemaelement import IEdmSchemaElement
from ProjectManagerSdk.models.iedmvocabularyannotation import IEdmVocabularyAnnotation
from dataclasses import dataclass

@dataclass
class IEdmModel:

    schemaElements: list[IEdmSchemaElement] | None = None
    vocabularyAnnotations: list[IEdmVocabularyAnnotation] | None = None
    referencedModels: list[IEdmModel] | None = None
    declaredNamespaces: list[str] | None = None
    directValueAnnotationsManager: IEdmDirectValueAnnotationsManager | None = None
    entityContainer: IEdmEntityContainer | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
