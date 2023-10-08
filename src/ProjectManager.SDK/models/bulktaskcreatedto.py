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
class BulkTaskCreateDto:
    """
    You can create a large number of Tasks rapidly using the
    BulkTaskCreate API. With this API you can submit multiple Tasks for
    creation at the same time. This API provides access to a subset of
    Task information; for full control over Task creation please use the
    normal Create Task API.
    """

    name: str | None = None
    description: str | None = None
    percentComplete: int | None = None
    statusId: str | None = None
    priorityId: int | None = None
    plannedStartDate: str | None = None
    plannedFinishDate: str | None = None
    actualStartDate: str | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
