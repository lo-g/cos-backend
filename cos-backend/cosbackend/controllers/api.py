from cosbackend.lib.base import BaseController
from cosbackend.model import DBSession
from cosbackend.model import Player
from tg import Response
from tg import decode_params
from tg import expose, validation_errors_response


class APIController(BaseController):

    @expose('json')
    def get_ranking(self):
        players = DBSession.query(Player).order_by(Player.defeats.desc()).all()
        return dict(result=players)

    @decode_params('json')
    @expose('json')
    def add_player(self, name=None, defeats=0):
        player = DBSession.query(Player).filter_by(name=name).first()
        if not player:
            player = Player()
            player.name = name
            player.defeats = defeats
            DBSession.add(player)
        return dict()

    @decode_params('json')
    @expose('json')
    def update_shame(self, name=None, defeats=1):
        player = DBSession.query(Player).filter_by(name=name).first()
        player.defeats += defeats
        return dict()
