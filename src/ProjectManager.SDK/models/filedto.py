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

    id: str | None = None
    projectId: str | None = None
    taskId: str | None = None
    ownerId: str | None = None
    createdDate: str | None = None
    folderId: str | None = None
    fileType: str | None = None
    fileTypeLabel: str | None = None
    size: int | None = None
    downloadPath: str | None = None
    deleted: bool | None = None
    type: str | None = None
    name: str | None = None
    entityOwnerId: str | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
