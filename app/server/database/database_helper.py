def user_helper(user) -> dict:
    return {   
        'id': str(user['_id']),     
        'customer_id': user['customer_id'],
        'api_key': user['api_key'],
        'secret': user['secret'],
        'custom_domains': user['custom_domains'] if 'custom_domains' in user else []
    }


def shorten_helper(shorten) -> dict:
    return {
        'id': str(shorten['_id']),
        'customer_id': shorten['customer_id'],
        'domain_name': shorten['domain_name'],
        'long_url': shorten['long_url'],
        'short_url': 'https://' + shorten['domain_name'] + '/' + shorten['input_desired_keyword'] if shorten['domain_name'] and shorten['input_desired_keyword'] else None  ,
        'input_desired_keyword': shorten['input_desired_keyword'],
        'time_limit': None, #shorten['time_limit'],
        'click_limit': None, #shorten['click_limit'],
        'got_rougue':  None, #shorten['got_rougue'],
        'not_child': None, #shorten['not_child'],
        'not_work': None, #shorten['not_work'],
        'contains_politics': None, #shorten['contains_politics'],
        'contains_promotions': None, #shorten['contains_promotions'],
        'contains_violence': None, #shorten['contains_violence'],
        'created_at':  shorten['created_at']
    }    
