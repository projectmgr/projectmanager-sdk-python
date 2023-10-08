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
class FileDto:
    """
    Represents a file in project manager
    """

    id: object | None = None
    projectId: object | None = None
    taskId: object | None = None
    ownerId: object | None = None
    createdDate: object | None = None
    folderId: object | None = None
    fileType: object | None = None
    fileTypeLabel: object | None = None
    size: object | None = None
    downloadPath: object | None = None
    deleted: object | None = None
    type: object | None = None
    name: object | None = None
    entityOwnerId: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
