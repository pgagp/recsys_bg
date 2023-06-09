# RecSys for board games
С результатом вы можете ознакомиться [здесь](https://recsys-board-games.streamlit.app)

Система рекомендаций настольных игр позволяет пользователю получать рекомендации по настольным играм, основываясь на его предпочтениях и прошлом опыте игр.

Для создания этого проекта были использованы данные, полученные через API сайта настольных игр tesera.ru. После получения данных была проведена предобработка, включающая в себя очистку, обработку пропущенных значений, приведение к единому формату и т.д.
Затем был проведен исследовательский анализ данных, в ходе которого были выявлены закономерности и зависимости между различными параметрами настольных игр. 

Для создания системы рекомендаций были обучены модели машинного обучения, основанные на алгоритмах коллаборативной фильтрации и контентной фильтрации. Коллаборативная фильтрация одновременно использует сходство между пользователями и элементами для предоставления рекомендаций. То есть модели совместной фильтрации могут рекомендовать элемент пользователю A на основе интересов аналогичного пользователя B. Контентная фильтрация основывается на описании и характеристиках игр и рекомендует игры, которые наиболее соответствуют интересам пользователя.
