from typing import List
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.pagination import paginate
from hymns.schemas import HymnSchema
from hymns.models import Hymn

router = Router(
    tags=["Hymns"]
)


@router.get("/", response=List[HymnSchema])
@paginate
def hymns_list(request: HttpRequest):
    """Returns a list of all Hymns"""
    return Hymn.objects.all()


@router.get("/search/", response=List[HymnSchema])
def search_by_title(request: HttpRequest, hymn_title: str):
    """Search Hymn by title"""
    hymns = Hymn.objects.filter(title__icontains=hymn_title)
    serialized_hymns = [HymnSchema.from_orm(hymn) for hymn in hymns]
    return serialized_hymns


@router.get("/{hymn_id}/", response=HymnSchema)
def get_hymn_by_id(request: HttpRequest, hymn_id:int):
    """Returns a single by ID"""
    hymn = get_object_or_404(Hymn, pk=hymn_id)
    return hymn
    