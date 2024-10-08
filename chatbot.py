from langchain_openai import ChatOpenAI

# ----------------------------------
# :: Chat GPT Bot API Class
# ----------------------------------

"""  
The ChatGPTBotAPI class manages prompts and interactions with the ChatOpenAI language model, 
allowing users to create, retrieve, and update prompts while handling API responses.
"""


class ChatGPTBotAPI:

    # -----------------------------
    # :: init Constructor Function
    # -----------------------------

    """
    The __init__ method initializes an instance of the class by setting up the ChatOpenAI language model with a provided API key
    and creating an empty list to store prompts.
    """

    def __init__(self, api_key):
        self.llm = ChatOpenAI(openai_api_key=api_key)
        self.prompts = []

    # ---------------------------
    # :: Create Prompt Function
    # ---------------------------

    """  
    The create_prompt method adds a new prompt to the list of stored prompts and returns its index in the list.
    """

    def create_prompt(self, prompt):
        self.prompts.append(prompt)
        return len(self.prompts) - 1

    # ---------------------------
    # :: Get Response Function
    # ---------------------------

    """ 
    The get_response method fetches a response from the language model based on a specified prompt index, 
    validating the index and handling potential errors.
    """

    def get_response(self, prompt_index):
        if not self._is_valid_index(prompt_index):
            raise IndexError("Prompt index out of range.")
        prompt = self.prompts[prompt_index]
        try:
            response = self.llm.invoke(prompt)
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            return f"An error occurred: {str(e)}"

    # ---------------------------
    # :: Update Prompt Function
    # ---------------------------

    """ 
    The update_prompt method modifies an existing prompt at a specified index with a new prompt, 
    ensuring the index is valid before making the update.
    """

    def update_prompt(self, prompt_index, new_prompt):
        if not self._is_valid_index(prompt_index):
            raise IndexError("Prompt index out of range.")
        self.prompts[prompt_index] = new_prompt

    # ---------------------------
    # :: Create Prompt Class
    # ---------------------------

    """ 
    The _is_valid_index method checks whether a given index is valid by verifying that it falls within the range of stored prompts.
    """

    def _is_valid_index(self, index):
        return 0 <= index < len(self.prompts)
