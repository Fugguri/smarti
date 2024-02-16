# import os

# from mics import promt_helper

# from llama_index.llms import (ChatMessage, MessageRole, OpenAI)
# from llama_index.prompts import PromptTemplate
# from llama_index.prompts import ChatPromptTemplate
# from llama_index import (LLMPredictor,
#                          GPTVectorStoreIndex,
#                          SimpleDirectoryReader,
#                          ServiceContext,
#                          )
# proxy_url = "http://9gfWr9:g0LSUy@131.108.17.194:9799/"

# dialog_history = dict()


# class GPTService:
#     def __init__(self, api_key, model_name="gpt-4-turbo-preview"):
#         os.environ['OPENAI_API_KEY'] = api_key
#         os.environ['HTTP_PROXY'] = proxy_url
#         os.environ['HTTPS_PROXY'] = proxy_url

#         self.openai = OpenAI(
#             # temperature=0,
#             model_name=model_name,
#             # http_client=http_client,
#             system_prompt=promt_helper.MAIN_PROMT.content

#         )

#         # Text QA Prompt
#         self.chat_text_qa_msgs = [
#             promt_helper.MAIN_PROMT,
#             promt_helper.PROGRAM_PROMT,
#             # promt_helper.PRICE_PROMT,
#             # ChatMessage(
#             #     role=MessageRole.SYSTEM,
#             #     content=(
#             #         ''''
#             # Возрадения на тему финансов и ответы на них:
#             # Нет денег: А какую сумму вы были бы готовы выделять ежемесячно на обучение? Мы понимаем, что не у всех клиентов есть возможность сразу вносить такую сумму, поэтому у нас доступна беспроцентная рассрочка до 24 месяцев, первый платеж у вас будет только через месяц, все проценты мы берем на себя. Ежемесячный платеж равен (0000), согласитесь, что в нынешних реалиях это сходить пару раз в магазин. А для того, чтобы в будущем не возникало ситуации, когда денег на что-то не хватает, необходимо получить высокоплачиваемую и актуальную  профессию, которой мы и обучаем. И вы сможете начать консультировать еще на этапе обучения, а это значит, что уже сможете окупать стоимость своего обученияю.
#             # Дорого: А почему вы так решили? Возможно, сравниваете наше обучение еще с чем-то? Наша цена более чем обоснована. Все наши курсы практикоориентированные, мы готовим квалифицированных специалистов. Согласитесь (000000) рублей не такая большая сумма за получение новой профессии с нуля с выдачей диплома. Если сравнивать с ВУЗами, то там примерно такая стоимость обучения за 1 год, а учиться надо минимум 4 года. У нас очень много практики, полная поддержка на всех этапах обучения, информация, которую вы получаете всегда актуальная, наши преподаватели это практикующие специалисты, именно поэтому наше обучение столько стоит
#             # Мне не нравится банк ".....": А почему вам не нравится этот банк? Был какой-то негативный опыт? У нас большая часть клиентов обучается по рассрочке через этот банк. Проблем никогда не возникало.  Но в любом случае, мы можем попробовать подать и в другие банки
#             #             ''')),
#             # ChatMessage(
#             #     role=MessageRole.SYSTEM,
#             #     content=(
#             #         ''''Возрадения на тему отсутствия времени и нагрузки и ответы на них:
#             # Нет времени: Понимаю, что всегда есть какие-то дела и вопросы, требующие вашего внимания, но самое идеальное время это учиться сейчас. Тем более, что наше обучение построено таким образом, что вы сможете учиться, работать, уделять время семье и близким. Лекции вы смотрите, когда хотите, так как они в записи, работа в тройках проводится с другими учениками, которым было бы удобно обучаться в то же время, что и вам, сессии вопрос-ответ вы всегда сможете посмотреть в записи, как и супервизии. Если у вас есть потребность в получении новых знаний, чтобы решить проблему с...., то не стоит откладывать.
#             # Уже обучаюсь у других: Раз вы оставили заявку, видимо, есть какая-то область, которую вы хотели бы изучить? А какой курс сейчас проходите? Чего не хватает вам в том обучении? Сколько осталось проходить? (смотрим табличку с конкурентами)
#             #                     '''

#             #     ),
#             # ),
#             # ChatMessage(
#             #     role=MessageRole.SYSTEM,
#             #     content=(
#             #         ''''Возрадения на тему внешнеполитической ситуации и ответы на них:
#             # В нынешней ситуации не хочу тратить деньги, они еще мне пригодятся.: Соглашусь, что сейчас остро стоит вопрос финансов в связи с событиями в мире и вместе с тем, как растет курс доллара, все наши деньги обесцениваются, поэтому вкладываться в себя-это сейчас наиболее выгодное решение, тем более мы еще не повышали стоимость наших курсов, но в ближайшее время скорее всего это случится. Поэтому откладывать обучение сейчас точно не стоит.
#             # Сейчас вокруг такая обстановка, что пока отложила для себя получение новой профессии, буду смотреть, что будет дальше: Соглашусь, что нынешняя ситуация внесла коррективы во все сферы нашей жизни. И в то же время любой кризис- это всегда новые возможности, которые нельзя упускать. Вы хотите освоить профессию психолога, сейчас самое время это делать, потому что сейчас профессия психолога актуальна как никогда. У многих людей высокая тревожность, апатия, стресс и не все могут с ними справиться. Поэтому учиться нужно наоборот как можно быстрее
#             # Если речь о дп: Также нужно понимать, что в нашей ментальности дети получают все самое лучшее. И в каких-то момента родитель в чем-то лучше урежет себя  чем ребенка. Особенно, когда идет речь о его здоровье.
#             # Нет эмоционального ресурса, нет моральных сил: Очень вас понимаю, подобные ситуации не могут не сказаться на нашем общем самочувствии, поэтому особенно важно не закрываться в себе. Когда вы находитесь в сообществе единомышленников, вам будет сильно проще переживать все эти события. Во-первых, вы сможете отвлекаться и уходить в учебу, а это действительно помогает. Во-вторых, вы всегда найдете поддержку среди преподавателей, кураторов, других учеников.
#             # Боюсь сокращения или потери работы: Хорошо, что вы задумываетесь над этим. Именно поэтому сейчас особенно важно искать запасные варианты, пока у вас есть такая возможность. Наш продукт сейчас востребован как никогда. А если вы будете заниматься частной практикой, то вы не будете привязаны к своему работодателю и остаться без работы вы не сможете. Плюс вы всегда сможете пройти наше обучение в ускоренном темпе
#             #                     '''

#             #     ),
#             # ),

#         ]
#         self.text_qa_template = ChatPromptTemplate(self.chat_text_qa_msgs)

#         # Refine Prompt
#         chat_refine_msgs = [
#             ChatMessage(
#                 role=MessageRole.SYSTEM,
#                 content=(
#                     '''
# Собираем у пользователя следующие данные:
# Имя
# Телефон
# Почта

# Пример сбора данных у пользователя:

# Напишите в чат как вас зовут? Напишите ваше имя в чат.
# Укажите ваш контактный номер телефона в формате 89996665544 без пробелов, скобок и тире. Важно! Ваши персональные данные защищены политикой конфиденциальности. Также, все наши сотрудники подписали “Соглашение о неразглашении” (NDA). Поэтому мы гарантируем, что ваш номер телефона не попадет в мошеннические руки или какие-либо базы для спам-звонков. Напишите номер прямо в чат.
# Укажите, пожалуйста, ваш e-mail в отчетном сообщении. Напишите его прямо в чат.

# Сообщение после оставленных данных:
# Спасибо! В ближайшее время с вами свяжется специалист и проконсультирует по всем вопросам. Ссылки на наш телеграмм канал Института и на отзывы'''
#                 ),
#             ),
#             ChatMessage(
#                 role=MessageRole.SYSTEM,
#                 content=(
#                     """Клиент ответил.
# Если клиенту нужно подобрать программу, задай данные вопросы и предоставь варианты ответа:

# Выберите цель обучения:
# -Освоить новую профессию с нуля
# -Повысить профессиональные навыки
# -Саморазвитие и личностный рост
# -Помочь родным и близким
# -Повысить уровень дохода
# Какое направление вам наиболее интересно?:
# -Практическая психология
# -Детская психология
# -Семейная психология
# -Сексология
# -Клиническая психология
# -Затрудняюсь ответить
# Какой бюджет вы готовы выделять в месяц на свое обучение?:
# -От 5 000 до 8 000 руб./мес.
# -От 8 000 до 12 000 руб./мес.
# -Пока не готова выделять бюджет
# Когда готовы начать обучение?:
# -Чем скорее, тем лучше
# -В течение месяца
# -В течение 3 месяцев
# -Еще не решила

# Если клиент выбрал цель обучения, направление, готов выделить бюджет и начать обучение в ближайшее время или в течение месяца, то запроси контактные данные (имя, телефон, почту) у клиента.

# Если клиент выбрал цель обучения, направление, готов выделить бюджет, но планирует начать обучение через 3 месяца или еще не решил, то предлагай бесплатную консультацию. Отправляй текст консультации и запрашиваем контактные данные (имя, телефон, почту) у клиента.

# Если клиент выбрал цель обучения, направление, но не готов выделять бюджет на обучение, то предлагай пользователю релевантный контент - записи открытых уроков.
# Ссылки на записи открытых уроков:
# Практический психолог - Запись открытого урока «Практическая психология — стартовая точка для начинающих психологов"[https://smart-inc.ru/open-lesson-pp]
# Детский психолог - Запись эфира "Детский психолог: как помогать детям и реализоваться в профессии"[https://smart-inc.ru/efir-child-psycholog]
# Семейный психолог - Запись открытого урока "Медиация: как разрешать конфликты экологично"[https://smart-inc.ru/open-lesson-mediation]
# Сексология - Запись открытого урока "Как отличить здоровые отношения от зависимых"[https://smart-inc.ru/open-lesson-relationship]

# Если клиент определился с целью обучения, но не определился с направлением, то предлагай ему общие записи открытых уроков.
# Ссылки на записи открытых уроков:
# Запись открытого урока "Как стать востребованным психологом"[https://smart-inc.ru/open-lesson]
# Запись конференции "Профессия психолога: тренды и создание личного бренда"[https://smart-inc.ru/open-lesson-conference-psychology-profession]


# Так же предлагай клиенту бесплатную консультацию от Smart.
# Длительность: 20-30 минут

# Что  ждёт клиента на консультации:
# Определим ваши цели
# Установим ваши уникальные потребности
# Подберем индивидуальный курс, который будет подходить вашему графику и целям обучения
# """
#                 ),
#             ),
#             ChatMessage(
#                 role=MessageRole.USER,
#                 content=(
#                     "We have the opportunity to refine the original answer "
#                     "(only if needed) with some more context below.\n"
#                     "------------\n"
#                     "{context_msg}\n"
#                     "------------\n"
#                     "Given the new context, refine the original answer to better "
#                     "answer the question: {query_str}. "
#                     "If the context isn't useful, output the original answer again.\n"
#                     "Original Answer: {existing_answer}"
#                 ),
#             ),
#         ]

#         self.refine_template = ChatPromptTemplate(chat_refine_msgs)
#         service_context = ServiceContext.from_defaults(
#             # system_prompt=promt,
#             llm=self.openai)

#         self.llm_predictor = LLMPredictor(llm=self.openai)
#         # memory = ConversationBufferMemory(
#         #     memory_key="chat_history"
#         # )

#         self.documents = SimpleDirectoryReader('docs').load_data()
#         self.index = GPTVectorStoreIndex.from_documents(
#             self.documents,
#             service_context=service_context,
#             # show_progress=True
#         )

#         custom_prompt = PromptTemplate(
#             """\
# Учитывая разговор (между Человеком и ассистентом) и последующее сообщение от Человека, \
# перепишите сообщение в виде отдельного вопроса, который отражает весь соответствующий контекст \
# из разговора.

# <История чата>
# {chat_history}

# <Последующее сообщение>
# {вопрос}

# <Отдельный вопрос>
# """
#         )
#         self.query_engine = self.index.as_chat_engine(
#             text_qa_template=self.text_qa_template,
#             chat_mode="condense_question", verbose=True,
#             # refine_template=self.refine_template,
#             # condense_question_prompt=custom_prompt,
#             # debug=True
#         )

#     def dialog_summary(self, chat_id):

#         response = self.query_engine.chat(
#             "Основываясь на диалоге сделай вывод к какой категории клентов можно отнести нашу переписку.",
#             chat_history=self.chat_text_qa_msgs
#         )
#         return response.response

#     def query_index(self, prompt, chat_id):
#         # print(self.query_engine.__dict__)
#         dialog = dialog_history.get(chat_id, None)

#         if not dialog:
#             dialog_history[chat_id] = self.chat_text_qa_msgs
#             dialog = dialog_history[chat_id]

#         dialog.append(ChatMessage(
#             role=MessageRole.USER,
#             content=(prompt)))
#         response = self.query_engine.chat(
#             prompt,
#             chat_history=dialog
#         )
#         # print(self.chat_text_qa_msgs)
#         dialog.append(ChatMessage(
#             role=MessageRole.ASSISTANT,
#             content=(response.response)))

#         return response.response
