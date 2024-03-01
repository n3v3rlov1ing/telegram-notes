import aiosqlite

class Database():
    def __init__(self):
        self.path = 'notes'
        
    async def add_note(self, user_id: int, text: str) -> None:
        async with aiosqlite.connect(self.path) as db:
            await db.execute("INSERT INTO notes (user_id, text) VALUES (?, ?) ", (user_id, text))
            await db.commit()
    
    async def get_notes(self, user_id: int, limit: int = 5) -> str:
        async with aiosqlite.connect(self.path) as db:
            response = await db.execute("SELECT text FROM notes WHERE user_id = ? LIMIT ?", (user_id, limit))
            notes = ''
            for i in await response.fetchall():
                notes += f'{i[0]}\n'
            return notes