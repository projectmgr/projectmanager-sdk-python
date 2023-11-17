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


from ProjectManagerSdk.models.iedmexpression import IEdmExpression
from ProjectManagerSdk.models.iedmterm import IEdmTerm
from ProjectManagerSdk.models.iedmvocabularyannotatable import IEdmVocabularyAnnotatable
from dataclasses import dataclass

@dataclass
class IEdmVocabularyAnnotation:

    qualifier: str | None = None
    term: IEdmTerm | None = None
    target: IEdmVocabularyAnnotatable | None = None
    value: IEdmExpression | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
