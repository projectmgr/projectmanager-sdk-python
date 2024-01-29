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


import dataclasses

@dataclasses.dataclass
class TaskMetadataUpdateDto:
    """
    Task Metadata DTO
    """

    data: object | None = None
    """
    Customer or system metadata
    """


