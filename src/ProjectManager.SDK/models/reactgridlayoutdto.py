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
class ReactGridLayoutDto:
    """
    A setting for react grid layout sizes
    """

    lg: list[object] | None = None
    md: list[object] | None = None
    sm: list[object] | None = None
    xs: list[object] | None = None
    xxs: list[object] | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
