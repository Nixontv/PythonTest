from flask import request
import logging
import json
import urllib

DEFAULT_USERAGENT = 'Mozilla/5.0 (Linux; Android 9; Pixel Build/PQ3A.190801.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.73 Mobile Safari/537.36'


def log_body(path, body):
    logging.warning("TAG_DEBUG:%s:body=%s" % (path, body,))


def parse_body(body):
    return json.loads(urllib.parse.unquote(body.decode('utf-8')))


def get_advertising_id(body):
    try:
        try:
            ads_id = body['advertisingId']
        except Exception:
            pass
        try:
            ads_id = body['applicationId']
        except Exception:
            pass
        return ads_id
    except Exception:
        return 'advertising_id'


def get_apps_flyer_id(body):
    try:
        return body['appsFlyerId']
    except Exception:
        return 'apps_flyer_id'


def generate_subs_str(subs):
    r = ''
    for i in range(len(subs)):
        r += 'sub_id_%s=%s' % (str(i + 1), subs[i],)
        if i != len(subs) - 1:
            r += '&'
    return r


def get_data_qq_tracker(data, af_id=None, tread_id=None):
    try:
        if not af_id or not tread_id:
            raise Exception('')
        body = parse_body(data)
        advertising_id = get_advertising_id(body)
        apps_flyer_id = get_apps_flyer_id(body)

        try:
            # facebook
            conversion_data = json.loads(body['conversionData'])
            campaign = conversion_data['campaign']

            campaign_name, *subs = campaign.split('_')

            if len(subs) < 7:
                while (len(subs) != 7):
                    subs.append('')
        except:
            # google or none traffic
            referrer = urllib.parse.unquote(body['referrer'])
            print(referrer)
            if referrer == 'utm_source=(not set)&utm_medium=(not set)':
                raise Exception('non google traffic')

            campaign_name = ''
            subs = []

            if len(subs) < 7:
                while (len(subs) != 7):
                    subs.append('')

        base_url = 'https://supertracker.xyz/%s?' % (tread_id,) + \
                   generate_subs_str(subs) + \
                   '&appflyer_dev_key=%s&advertising_id=%s&Campaign=%s&apps_flyer_id=%s' % tuple(
            [af_id] + [advertising_id] + [campaign_name] + [apps_flyer_id])
        offer_id = campaign_name
        useragent = DEFAULT_USERAGENT
    except Exception as e:
        # none traffic
        base_url = ''
        offer_id = ''
        useragent = DEFAULT_USERAGENT
    return (base_url, offer_id, useragent,)


# default handler
def get_default_perform_map(apps_flyer_key, thread):
    def default_perform_map():
        (base_url, offer_id, useragent,) = get_data_qq_tracker(request.data, apps_flyer_key, thread)
        return {'url': base_url, 'offer_id': offer_id, 'useragent': useragent}

    return default_perform_map


def get_default_perform_map_testing(url):
    def default_perform_map():
        try:
            print(parse_body(request.data))
        except:
            pass

        return {'url': url, 'offer_id': ''}

    return default_perform_map