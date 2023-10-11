import json

def read_prompts_and_texts(file_path):
    with open(file_path, 'r') as file:
        content = json.load(file)
    return content['prompts'], content['texts']

def get_item_by_id(items, item_id):
    for item in items:
        if item['id'] == item_id:
            return item
    return None
