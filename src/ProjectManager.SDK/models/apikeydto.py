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
class ApiKeyDto:
    """
    Represents api access key entity
    """

    id: object | None = None
    createdBy: object | None = None
    expires: object | None = None
    apiKey: object | None = None
    name: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
