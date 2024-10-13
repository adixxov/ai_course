import os
OPENAI_API_KEY = "OPENAI_API_KEY"   # insert your own OPENAI_API_KEY
# I'm omitting all other keys
def set_environment():
    variable_dict = globals().items()
    for key, value in variable_dict:
        if "API" in key or "ID" in key:
            os.environ[key] = value