from aiogram.fsm.state import State, StatesGroup

class Notes(StatesGroup):
    text = State()
    
class Limit(StatesGroup):
    limit = State()