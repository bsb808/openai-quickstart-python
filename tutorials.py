import os
import openai
from dotenv import load_dotenv
load_dotenv() 

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

#response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )

prompt = generate_prompt('racoon')

response = openai.Completion.create(model="text-davinci-003",
                                    prompt=prompt,
                                    max_tokens = 200,
                                    temperature=0.6)


#response = openai.Completion.create(model="text-davinci-003",temperature=0.6)
