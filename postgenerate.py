from llm import llm
from fewshot import FewShot

few_shot = FewShot()


def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"


def generate_post(length, tag):
    prompt = get_prompt(length, tag)
    response = llm.invoke(prompt)
    return response.content


def get_prompt(length, tag):
    length_str = get_length_str(length)

    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {tag}
    2) Length: {length_str}
    The script for the generated post should always be English.
    '''

    examples = few_shot.get_filtered_posts(length,tag)

    if len(examples) > 0:
        prompt += "4) Use the writing style as per the following examples."

    for i, post in enumerate(examples):
        post_text = post['text']
        prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        if i == 1: 
            break

    return prompt


if __name__ == "__main__":
    print(generate_post("Medium", "Artificial Intelligence"))