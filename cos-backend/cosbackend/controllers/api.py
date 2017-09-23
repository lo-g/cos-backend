from cosbackend.lib.base import BaseController
from tg import expose


class APIController(BaseController):

    @expose('json')
    def get_ranking(self, **kwargs):
        print "get_ranking"
        return {
            'result': [
                {
                    'name': 'Andonio',
                    'defeats': 111
                },
                {
                    'name': 'Nicola',
                    'defeats': 11111
                },
                {
                    'name': 'lorenzo',
                    'defeats': 11
                },
                {
                    'name': 'davide',
                    'defeats': 11
                },
                {
                    'name': 'marco',
                    'defeats': 111
                },
            ]
        }
