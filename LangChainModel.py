# import os
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain_community.chat_models import ChatOpenAI
# from langchain.vectorstores.chroma import Chroma
# from langchain.document_loaders.directory import DirectoryLoader
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.chains import ConversationalRetrievalChain
# from langchain_core.prompts import ChatPromptTemplate
# from langchain.chains import StuffDocumentsChain, LLMChain
# from langchain_core.prompts import PromptTemplate
# from langchain_community.llms import OpenAI


# proxy_url = "http://9gfWr9:g0LSUy@131.108.17.194:9799/"
# api_key = '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'


# class LanChainModel:
#     def __init__(self, model_name="gpt-3.5-turbo", docs_folder='docs'):
#         os.environ['OPENAI_API_KEY'] = api_key
#         os.environ['HTTP_PROXY'] = proxy_url
#         os.environ['HTTPS_PROXY'] = proxy_url

#         template = """
#         Диалог всегда начинается с "Здравствуйте. Я цифровой помощник онлайн-института Smart. Меня зовут - Смартик.

# Вы можете общаться со мной, как с живым человеком. Я отлично понимаю человеческую речь и смогу ответить на любой вопрос.

# Хотите подобрать обучающую программу или у вас есть конкретный вопрос?
# "
#              Критерии для бота:
# 	1. Общается только на русском языке
# 	2. Пишет по одному вопросу, не отправляет вопросы списком
# 	3. Если переписка затягивается, то бот должен подводить к этапу квалификации и взятии контактных данных
# 	4. Не давать сразу готовый ответ, например, по стоимости, а вовлекать в диалог, называть сумму от или диапазон, чтобы после вывести на сбор контактов
# 	5. Не просто ответил на вопрос и бросил, а ответил и далее вовлекает диалог и после выводит на квалификацию
# 	6. Общение на TOV
# 	7. Основная цель - квалифицировать и взять контактные данные пользователя
# 	8. Интеграция с salebot, чтобы после сделка передавалась в ОП (можно сделать в гугл-таблицу и после передавать их в salebot / передача через API)
# 	9. Имеет ряд обязательных вопросов, по которым должен пройтись с пользователем
# Ты бот - специалист поддержки компании Smart

# {context}
# Отвечай исходя из контекста.

# Вопрос:{question}
# Ответ:
#  """

#         loader = DirectoryLoader(docs_folder)
#         documents = []
#         documents.extend(loader.load())
#         text_splitter = CharacterTextSplitter()
#         documents = text_splitter.split_documents(documents)

#         embedding = ChatOpenAI(
#             api_key=api_key,
#             temperature=0,
#             model_name=model_name,

#         )

#         prompt = PromptTemplate(
#             template=template, input_variables=["context", "question"])
#         embedding = OpenAIEmbeddings()
#         vectorstore = Chroma.from_documents(documents, embedding)
#         llm_chain = LLMChain(llm=llm, prompt=prompt)
#         self.chain = StuffDocumentsChain(
#             llm_chain=llm_chain,
#             # document_prompt=document_prompt,
#             # document_variable_name=document_variable_name
#         )
#         system_message = {
#             "role": "system", "content": """Критерии для бота: ... (your system message) """}

#     def save_index(self, file_path='index.json'):
#         self.index.save_to_disk(file_path)

#     def load_index(self, file_path='index.json'):
#         # self.index = GPTVectorStoreIndex.load_from_disk(file_path)
#         ...

#     def query_index(self, prompt):
#         # query_engine = self.index.as_query_engine()
#         response = self.chain.invoke({"input": prompt})

#         return response.content


# if __name__ == "__main__":

#     gpt_service = LanChainModel()

#     while True:
#         user_prompt = input("Type prompt... (or 'exit' to quit)")
#         if user_prompt.lower() == 'exit':
#             break
#         response = gpt_service.query_index(user_prompt)
#         print(response)
