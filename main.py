import random
import flask
# from endpoints import api
import helpers

def create_app():
    return flask.Flask(__name__)

app = create_app()

generate_random_str = lambda s: s + str(random.getrandbits(128))

@app.route('/')
def hallo():
    """Return a friendly HTTP greeting."""
    return 'Hallo from Belarus - 14.02.2025 - 09:58 pm'

@app.route('/api/test')
def hallo_api_test():
    """Return a friendly HTTP greeting."""
    return 'test: Hallo from Belarus - 14.02.2025 - 09:58 pm'

enpoints_data = [
    # [path, [methods], handler, idle]

    # ['/api/data/test',              ['POST'], api.test],

    # java android apps
    # ['/api/get-data',               ['POST'], api.get_data], # removed
    # ['/api/all-features',           ['POST'], api.all_features],
    # ['/api/data/magic-star',        ['POST'], api.magic_star],
    # ['/api/data/slots-history',     ['POST'], api.slots_history],

    # unity apps
    # ['/api/data/machines-history',  ['POST'], helpers.get_default_perform_map('xhHMouC5Vf6msvAqwwiLCQ', 'VKLHFT')],
    # ['/api/data/magic-start',       ['POST'], helpers.get_default_perform_map('PyhS7sUR9wHDy2b2GVm75Z', 'kfv3RdFh')],
    # ['/api/data/cards-history',     ['POST'], helpers.get_default_perform_map('X6A6pckJh3hhBSGTt9K4ff', '7BP11NkN')],
    # ['/api/data/golden-history',    ['POST'], helpers.get_default_perform_map('AJATijrtNYfWSHMmBWj6MS', 'jkcJ8gmG')],
    # ['/api/data/rockets-history',   ['POST'], helpers.get_default_perform_map('AGP8Vivr6vjjraeAHeyD24', 'HZk5F1qJ')],
    # ['/api/data/magic-history',     ['POST'], helpers.get_default_perform_map('mrHeHQ7QNNrVeCF2dwtQBL', 'F5Y8jT')],
    # ['/api/data/cherry-history',    ['POST'], helpers.get_default_perform_map('NJ2XeouVjGLKSPKGmxw3M8', 'bcfHzPYZ')],


    # ['/api/data/boom-history',  ['POST'], helpers.get_default_perform_map_testing('http://html5test.com/')],
    # ['/api/data/boom-history',      ['POST'], helpers.get_default_perform_map('ogQGNXS7DZVF2mncVn8xjZ', 'g5tvqX')],
    # ['/api/data/diamonds-history',  ['POST'], helpers.get_default_perform_map('uFfGGhB6x2enpgWvah55p9', '4b9pkv')],
    # ['/api/data/fortune-history',   ['POST'], helpers.get_default_perform_map('kpFcETfH3erC8ryM6bZFrC', 'fYqGMskp')],
    # ['/api/data/joker-space',       ['POST'], helpers.get_default_perform_map('', ''), True],
    # ['/api/data/magic-space',       ['POST'], helpers.get_default_perform_map('', ''), True],
    # ['/api/data/cherry-space',      ['POST'], helpers.get_default_perform_map('', ''), True],
    # ['/api/data/seven-space',       ['POST'], helpers.get_default_perform_map('', ''), True],
    # ['/api/data/casino-space',      ['POST'], helpers.get_default_perform_map('mpnrsdhAQ928P2CApJ2uVN', 'QXsBBmhs')],
    # ['/api/data/slots-space',       ['POST'], helpers.get_default_perform_map('', ''), True],
    ['/api/data/machines-space',    ['POST'], helpers.get_default_perform_map('euFuNJVKsMMfAuB264zvz4', '48Mh9bGJ')],
    ['/api/data/cards-space',       ['POST'], helpers.get_default_perform_map('fWjA7KeA4PEVoBxqMB7QGQ', 'gLwQDCQ5')],
    ['/api/data/golden-space',       ['POST'], helpers.get_default_perform_map('BrCKiRKFFNDnyTwTgC6iaf', 'bMWVyYbC')],

    # ['/api/data/rockets-space',     ['POST'], helpers.get_default_perform_map('', ''), True],
    # ['/api/data/boom-space',        ['POST'], helpers.get_default_perform_map('', ''), True],
    # ['/api/data/diamonds-space',    ['POST'], helpers.get_default_perform_map('', ''), True],
    # ['/api/data/fortune-space',     ['POST'], helpers.get_default_perform_map('', ''), True],
    # ['/api/data/joker-like',        ['POST'], helpers.get_default_perform_map('', ''), True],
    ['/api/data/magic-like',        ['POST'], helpers.get_default_perform_map('', ''), True],
    ['/api/data/cherry-like',       ['POST'], helpers.get_default_perform_map('', ''), True],
    ['/api/data/seven-like',        ['POST'], helpers.get_default_perform_map('', ''), True],
    ['/api/data/casino-like',       ['POST'], helpers.get_default_perform_map('', ''), True],
    ['/api/data/slots-like',        ['POST'], helpers.get_default_perform_map('', ''), True],
    ['/api/data/machines-like',     ['POST'], helpers.get_default_perform_map('', ''), True],
]

@app.before_request
def before_request_func():
    # log body of every request
    try:
        body = helpers.parse_body(flask.request.data)
        body['remote_addr'] = flask.request.remote_addr
        helpers.log_body(
            path=flask.request.path,
            body=body)
    except:
        helpers.log_body(
            path=flask.request.path,
            body={'message': 'logging data parse error'})
        pass

# initialize endpoints
for endpoint in enpoints_data:
    try:
        f = endpoint[2].perform_map
        f.__name__ = generate_random_str('f')
    except:
        f = endpoint[2]
        f.__name__ = generate_random_str('f')
    app.route(endpoint[0], methods=endpoint[1])(f)

# yellow_affiliate_apps_info_bot
# @app.route("/bot/status", methods=["GET"])
# def bot_status_handler():
#     bot.helpers.send_message(476373419, "bot status checking performed")
#     return {'status': 'good' if bot.commands.StaticValues.bot_status_good else 'bad'}
#
# @app.route("/bot/handler", methods=["POST"])
# def bot_message_handler():
#     try:
#         chat_id = flask.request.json["message"]["chat"]["id"]
#         text = flask.request.json["message"]["text"]
#
#         if bot.base_handlers.handle_commands_response(chat_id, text):
#             return bot.commands.StaticValues.ok_response
#     except KeyError:
#         # message editing
#         chat_id = flask.request.json["edited_message"]["chat"]["id"]
#         bot.helpers.send_message(chat_id, "bot doesnt supports messages editing")
#         return bot.commands.StaticValues.ok_response
#
#     # all other messages
#     bot.helpers.send_message(chat_id, "please, dont spam")
#     return bot.commands.StaticValues.ok_response
#
# @app.route("/bot/check-apps", methods=["GET"])
# def bot_check_apps_handler():
#     [removed_apps] = bot.commands.Commands.check_and_remove_apps()
#     for chat_id in list(removed_apps):
#         message = bot.helpers.get_apps_message(
#             [{'application_id': application_id} for application_id in removed_apps[chat_id]],
#             'removed_apps',)
#         if len(message) == 0:
#             continue
#         bot.helpers.send_message(chat_id, message)
#     return bot.commands.StaticValues.ok_response

if __name__ == '__main__':
    # def fail_callback():
    #     bot.commands.StaticValues.bot_status_good = False
    # bot.helpers.perform_web_hook_call(fail_callback=fail_callback)
    app.run(host='127.0.0.1', port=8080, debug=True)

