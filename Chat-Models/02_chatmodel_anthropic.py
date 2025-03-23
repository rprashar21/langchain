from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv


load_dotenv()

model = ChatAnthropic(model='claude')
result = model.invoke('what is capital of india')

print(result)