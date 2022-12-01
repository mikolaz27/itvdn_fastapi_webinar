from api import utils
from api.models import PostDB, PostSchema
from fastapi import APIRouter, HTTPException, Path
from typing import List

router = APIRouter()


@router.post("/", response_model=PostDB, status_code=201)
async def create_post(payload: PostSchema):
    post_id = await utils.post(payload)

    response_object = {
        "id": post_id,
        "title": payload.title,
        "description": payload.description,
        "created_by": payload.created_by,
    }
    return response_object


@router.get("/{id}/", response_model=PostDB)
async def read_post(id: int = Path(..., gt=0), ):
    post = await utils.get(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.get("/", response_model=List[PostDB])
async def read_all_posts():
    return await utils.get_all()


@router.put("/{id}/", response_model=PostDB)
async def update_post(payload: PostSchema, id: int = Path(..., gt=0)):
    post = await utils.get(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post_id = await utils.put(id, payload)
    response_object = {
        "id": post_id,
        "title": payload.title,
        "description": payload.description,
        "created_by": payload.created_by
    }
    return response_object


@router.delete("/{id}/", response_model=PostDB)
async def delete_post(id: int = Path(..., gt=0)):
    post = await utils.get(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    await utils.delete(id)

    return post
