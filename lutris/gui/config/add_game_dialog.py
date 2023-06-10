from gettext import gettext as _

from lutris.config import LutrisConfig
from lutris.gui.config.common import GameDialogCommon
from lutris.util.log import logger


class AddGameDialog(GameDialogCommon):
    """Add game dialog class."""

    def __init__(self, parent, game=None, runner=None):
        logger.debug("AddGameDialog.__init__ A")
        super().__init__(_("Add a new game"), parent=parent)
        logger.debug("AddGameDialog.__init__ B")
        self.game = game
        self.saved = False
        if game:
            self.runner_name = game.runner_name
            self.slug = game.slug
        else:
            self.runner_name = runner
            self.slug = None
        logger.debug("AddGameDialog.__init__ C")
        self.lutris_config = LutrisConfig(
            runner_slug=self.runner_name,
            level="game",
        )
        logger.debug("AddGameDialog.__init__ D")
        self.build_notebook()
        logger.debug("AddGameDialog.__init__ E")
        self.build_tabs("game")
        logger.debug("AddGameDialog.__init__ F")
        self.name_entry.grab_focus()
        logger.debug("AddGameDialog.__init__ G")
        self.show_all()
        logger.debug("AddGameDialog.__init__ H")
