from sqlalchemy import select
from sqlalchemy.orm import Session
from app.user.domain.repository import UserRepository
from app.user.domain.entities import User, UserCreateDTO, UserUpdateDTO
from app.user.infrastructure.models.model import UserModel

class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    async def create_user(self, user_data: UserCreateDTO) -> User:
        user_orm = UserModel(
            username=user_data.username,
            email=user_data.email, 
            hashed_password=""  # Temporalmente vacío
        )
        # Encriptar la contraseña antes de guardarla
        user_orm.set_password(user_data.password)
        
        self.session.add(user_orm)
        await self.session.commit()
        await self.session.refresh(user_orm)

        return User.model_validate(user_orm)
    
    async def update_user(self, user_data: UserUpdateDTO) -> User:
        # Buscar el usuario existente por ID
        stmt = select(UserModel).where(UserModel.user_id == user_data.user_id)
        result = await self.session.execute(stmt)
        user_orm = result.scalars().first()
        
        if not user_orm:
            raise ValueError(f"Usuario con ID {user_data.user_id} no encontrado.")

        # Actualizar los campos
        user_orm.username = user_data.username
        user_orm.email = user_data.email

        # Actualizar la contraseña, si se proporciona
        if user_data.password:
            user_orm.set_password(user_data.password)
        
        # Guardar los cambios
        await self.session.commit()
        await self.session.refresh(user_orm)
        
        return User.model_validate(user_orm)

    
    async def delete_user(self, user_id: int) -> bool:
        # Buscar el usuario por su ID
        stmt = select(UserModel).where(UserModel.user_id == user_id)
        result = await self.session.execute(stmt)
        user_orm = result.scalars().first()

        if not user_orm:
            raise ValueError(f"User with ID {user_id} not found.")

        # Eliminar el usuario
        await self.session.delete(user_orm)
        await self.session.commit()
        return True

    
    async def get_user_by_id(self, user_id: int) -> User:
        stmt = select(UserModel).where(UserModel.user_id == user_id)
        result = await self.session.execute(stmt)
        user_orm = result.scalars().first()

        if not user_orm:
            raise ValueError(f"Product with ID {user_id} not found.")

        return User.model_validate(user_orm)

    async def get_all_user(self) -> list[User]:
        stmt = select(UserModel)
        result = await self.session.execute(stmt)
        user_orm = result.scalars().all()

        #return [Product.from_orm(p) for p in product_orms]
        return [User.model_validate(p) for p in user_orm]
