import os
import openai

from dotenv import load_dotenv, find_dotenv
from openai_client import get_completion
from prompt_manager import read_prompts_and_texts, get_item_by_id

try:
    if not load_dotenv(find_dotenv()):
        raise FileNotFoundError("Could not find the .env file")

    openai_api_key = os.getenv('OPENAI_API_KEY')
    if openai_api_key is None:
        raise ValueError("OPENAI_API_KEY not found in .env file")

    openai.api_key = openai_api_key

    prompts, texts = read_prompts_and_texts('prompts.json')
    chosen_prompt = get_item_by_id(prompts, 'prompt_7')  # Change to the desired prompt id
    chosen_text =get_item_by_id(texts, 'text_5')  # Change to the desired text id

    if chosen_prompt:
        if '{text}' in chosen_prompt['prompt']:
            if chosen_text:
                prompt = chosen_prompt['prompt'].format(text=chosen_text['text'])
            else:
                prompt = chosen_prompt['prompt'].format(text='')
        else:
            prompt = chosen_prompt['prompt']

        response = get_completion(prompt)
        if response is not None:
            print(response)
        else:
            print("An error occurred while getting the completion")
    else:
        print("The prompt with the specified id was not found")

except FileNotFoundError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(f"Unexpected error: {e}")
