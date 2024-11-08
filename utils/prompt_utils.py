def recommendation_prompt(watched_vids_link, links):
    RECOMMENDATION_PROMPT = f""" The user has not watched the following YouTube video links: {links} The user has already watched the following videos: {watched_vids_link} From the list of unwatched videos, recommend exactly 3 links that would be interesting to the user. Please respond with only the links, in the format: https://www.youtube.com/watch?v=XXXXXX """
    return RECOMMENDATION_PROMPT

def learning_path_prompt(watched_vids_link, links):
    LEARNING_PATH_PROMPT = f"""
    The user has watched the following YouTube videos:
    {watched_vids_link}

    Given the user's progress and interests demonstrated by the watched videos, create a structured learning path using the unwatched videos from this list:
    {links}

    The learning path should:
    1. Reinforce foundational knowledge if needed.
    2. Introduce intermediate concepts based on the user's current understanding.
    3. Progressively lead to advanced topics, making sure each recommended video logically builds on the previous one.

    Provide a list of exactly 3 video links that guide the user through a logical progression of learning. If possible, explain briefly how each step contributes to building the user's knowledge.

    remember only provide the link in this format [link1,link2,link3] and only provide the array i dont want any extra texts from you
    """
    return LEARNING_PATH_PROMPT

def explanation_prompt(link):
    EXPLANATION_PROMPT = f""" The user has watched the following video: {link} you have to answer any questions regarding this video so please summaries and try to understand the video and if the user asks any question answer that."""
    return EXPLANATION_PROMPT

def qna_prompt(name, question, summary):
    QNA_PROMPT = f"""You have to answer question according The Name of the video and the summary of it so i here is the name of the video {name} and here is the summary of it {summary}. Now answer this Question: {question}.Please just answer the question dont provide any extra texts like 'based on the summary...' or 'Based on the title...' only the answer """
    return QNA_PROMPT
