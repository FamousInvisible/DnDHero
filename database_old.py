import sqlalchemy as db #импорт sqlalchemy

engine = db.create_engine('sqlite:///dnd.db') #создание движка для СУБД

conn = engine.connect() #подключение к БД
metadata = db.MetaData() #создание метаданных

spells = db.Table( #создание таблицы
    'spells', metadata,
    db.Column('spell_id', db.Integer, primary_key=True),
    db.Column('spell_name', db.Text),
    db.Column('spell_lvl', db.Integer),
    db.Column('spell_desc', db.Text),
    db.Column('spell_school', db.Text)
)
metadata.create_all(engine) #добавляем изменения в БД

#ДОБАВЛЕНИЕ ДАННЫХ В ТАБЛИЦУ

'''insert_data = spells.insert().values([{
    'spell_name': 'Огненный Шар',
    'spell_lvl': 3,
    'spell_desc': 'Разрушительный огненный шар наносящий огненный урон',
    'spell_school': 'Колдовство'
}])'''
'''conn.execute(insert_data)'''


skills =  db.Table(
    'skills', metadata,
    db.Column('skills_id', db.Integer, primary_key=True),
    db.Column('skills_name', db.Text),
    db.Column('skills_desc', db.Text)
)
metadata.create_all(engine)

'''insert_data = skills.insert().values([{
    'skills_name': 'Нож',
    'skills_desc': 'Навык обращения с ножами в бою',
}])
conn.execute(insert_data)
'''

def get_spells():
    selection_query = db.select(spells)
    selection_result = conn.execute(selection_query)
    return selection_result.fetchall()

def get_skills():
    selection_query = db.select(spells)
    selection_result = conn.execute(selection_query)
    return selection_result.fetchall()

#Сырой sql запрос в sql alchemy
'''with engine.connect() as connection: 
    result = connection.execute(db.text('ALTER TABLE skills DROP COLUMN errorColumn2'))'''