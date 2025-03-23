from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# load the env file for the api_key
load_dotenv()
# create an ChatOpenAI and specify which model you want to use
model = ChatOpenAI(model='gpt-4',temperature=1.5,max_tokens=10)

result = model.invoke("Tell me some contratrion ideas")

print(result.content)

