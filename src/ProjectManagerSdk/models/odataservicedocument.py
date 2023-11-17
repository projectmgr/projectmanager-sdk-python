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


from ProjectManagerSdk.models.odataentitysetinfo import ODataEntitySetInfo
from ProjectManagerSdk.models.odatafunctionimportinfo import ODataFunctionImportInfo
from ProjectManagerSdk.models.odatasingletoninfo import ODataSingletonInfo
from ProjectManagerSdk.models.odatatypeannotation import ODataTypeAnnotation
from dataclasses import dataclass

@dataclass
class ODataServiceDocument:

    typeAnnotation: ODataTypeAnnotation | None = None
    entitySets: list[ODataEntitySetInfo] | None = None
    singletons: list[ODataSingletonInfo] | None = None
    functionImports: list[ODataFunctionImportInfo] | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
