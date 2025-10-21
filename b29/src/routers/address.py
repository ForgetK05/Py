from fastapi import APIRouter
from src.db import AddressSchema, Address, get_session, select
from typing import List


