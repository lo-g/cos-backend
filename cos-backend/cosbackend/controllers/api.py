from cosbackend.lib.base import BaseController
from cosbackend.model import DBSession
from cosbackend.model import Player
from tg import Response
from tg import decode_params
from tg import expose, validation_errors_response


class APIController(BaseController):

    @expose('json')
    def get_ranking(self, **kwargs):
        print "get_ranking"
        players = DBSession.query(Player).all()
        print players

        return dict(result=players)

        # return {
        #     'result': [
        #         {
        #             'name': 'Andonio',
        #             'defeats': 111
        #         },
        #         {
        #             'name': 'Nicola',
        #             'defeats': 11111
        #         },
        #         {
        #             'name': 'lorenzo',
        #             'defeats': 11
        #         },
        #         {
        #             'name': 'davide',
        #             'defeats': 11
        #         },
        #         {
        #             'name': 'marco',
        #             'defeats': 111
        #         },
        #     ]
        # }

    @decode_params('json')
    @expose('json')
    def add_player(self, name=None, defeats=0):

        print "name", name
        print "defeats", defeats

        player = DBSession.query(Player).filter_by(name=name).first()
        if not player:
            player = Player()
            player.name = name
            player.defeats = defeats
            DBSession.add(player)

        return dict()
