import uuid

from fastapi import APIRouter, HTTPException, status

from app.models import MemberCreate, MemberUpdate, MemberResponse
from app import database as db

router = APIRouter(prefix="/members", tags=["members"])


@router.get("/", response_model=list[MemberResponse])
def list_members():
    return db.get_all()


@router.get("/{member_id}", response_model=MemberResponse)
def get_member(member_id: str):
    member = db.get_by_id(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member


@router.post("/", response_model=MemberResponse, status_code=status.HTTP_201_CREATED)
def create_member(payload: MemberCreate):
    member = payload.model_dump(mode="json")
    member["id"] = str(uuid.uuid4())
    return db.create(member)


@router.put("/{member_id}", response_model=MemberResponse)
def update_member(member_id: str, payload: MemberUpdate):
    updates = payload.model_dump(mode="json", exclude_unset=True)
    if not updates:
        raise HTTPException(status_code=400, detail="No fields to update")
    member = db.update(member_id, updates)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member


@router.delete("/{member_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_member(member_id: str):
    if not db.delete(member_id):
        raise HTTPException(status_code=404, detail="Member not found")
