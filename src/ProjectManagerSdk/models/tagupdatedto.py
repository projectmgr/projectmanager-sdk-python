#
# ProjectManager API for Python
#
# (c) ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#


from typing import List
import dataclasses

@dataclasses.dataclass
class TagUpdateDto:
    """
    A Tag is a named categorization you can use to distinguish objects
    from each other. Tags each have a unique identifier, a name, and a
    color.
    """

    color: str | None = None
    """
    The color that will be used to represent this Tag visually. This
    color is automatically chosen by the application when a user creates
    a Tag. You can choose specify any color that can be represented
    using HTML RGB syntax such as `#0088FF`, in the format `RRGGBB`. You
    may not use names for colors.
    """


