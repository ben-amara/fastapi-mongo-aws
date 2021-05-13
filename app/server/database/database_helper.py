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
        'mini_link': 'https://' + shorten['mini_link'],
        'input_desired_keyword': shorten['input_desired_keyword'],
        'time_limit': shorten['time_limit'] if shorten['time_limit'] else None,
        'click_limit': shorten['click_limit'] if shorten['click_limit'] else None,
        'go_rougue':  shorten['go_rougue'] if shorten['go_rougue'] else None,
        'not_child': shorten['not_child'] if shorten['not_child'] else None,
        'not_work': shorten['not_work'] if shorten['not_work'] else None,
        'contains_politics': shorten['contains_politics'] if shorten['contains_politics'] else None,
        'contains_promotions': shorten['contains_promotions'] if shorten['contains_promotions'] else None,
        'contains_violence': shorten['contains_violence']  if shorten['contains_violence'] else None,
        'created_at':  shorten['created_at']
    }    
