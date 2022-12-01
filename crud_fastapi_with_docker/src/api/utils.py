from api.models import PostSchema
from database_handler import posts, database


async def post(payload: PostSchema):
    query = posts.insert().values(title=payload.title, description=payload.description, created_by=payload.created_by)
    return await database.execute(query=query)


async def get(id: int):
    query = posts.select().where(id == posts.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = posts.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload=PostSchema):
    query = (
        posts.update().where(id == posts.c.id).values(title=payload.title, description=payload.description)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = posts.delete().where(id == posts.c.id)
    return await database.execute(query=query)
