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

    name: object | None = None
    description: object | None = None
    percentComplete: object | None = None
    statusId: object | None = None
    priorityId: object | None = None
    plannedStartDate: object | None = None
    plannedFinishDate: object | None = None
    actualStartDate: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
