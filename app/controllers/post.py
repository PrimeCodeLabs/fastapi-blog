from typing import List
from cachetools import TTLCache
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db, validate_payload_size
from app.models.post import Post as PostModel
from app.models.user import User as UserModel
from app.schemas.post import Post as PostSchema, PostCreate
from app.services.auth_service import get_current_user

router = APIRouter()
cache = TTLCache(maxsize=100, ttl=300)


@router.post("/", response_model=PostSchema, dependencies=[Depends(validate_payload_size)])
def create_post(post: PostCreate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_post = PostModel(**post.model_dump(), owner_id=current_user.id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.get("/", response_model=List[PostSchema])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    if current_user.email in cache:
        return cache[current_user.email]
    posts = db.query(PostModel).filter(PostModel.owner_id == current_user.id).offset(skip).limit(limit).all()
    cache[current_user.email] = posts
    return posts

@router.delete("/{post_id}", response_model=PostSchema)
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: PostModel = Depends(get_current_user)):
    post = db.query(PostModel).filter(PostModel.id == post_id, PostModel.owner_id == current_user.id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    return post
