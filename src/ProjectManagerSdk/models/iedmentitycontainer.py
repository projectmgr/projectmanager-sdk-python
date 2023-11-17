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


from ProjectManagerSdk.models.iedmentitycontainerelement import IEdmEntityContainerElement
from dataclasses import dataclass

@dataclass
class IEdmEntityContainer:

    elements: list[IEdmEntityContainerElement] | None = None
    schemaElementKind: str | None = None
    namespace: str | None = None
    name: str | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
