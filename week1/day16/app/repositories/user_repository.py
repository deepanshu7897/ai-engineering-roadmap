from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User


class UserRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_username(
        self,
        username: str,
    ):
        result = await self.db.execute(
            select(User).where(
                User.username == username
            )
        )
        return result.scalar_one_or_none()

    async def get_by_id(
        self,
        user_id: int,
    ):
        result = await self.db.execute(
            select(User).where(
                User.id == user_id
            )
        )
        return result.scalar_one_or_none()

    async def create_user(
        self,
        username: str,
        hashed_password: str,
    ):
        user = User(
            username=username,
            hashed_password=hashed_password,
        )

        self.db.add(user)

        await self.db.commit()

        await self.db.refresh(user)

        return user

    async def get_all_users(self):
        result = await self.db.execute(
            select(User)
        )

        return result.scalars().all()