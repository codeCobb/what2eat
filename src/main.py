# src/main.py
from fastapi import FastAPI, Response, Depends

from src.core.config import settings
from src.core.config import get_settings, Settings
from src.lifespan import lifespan

from src.core.exception import register_exception_handlers
from src.dishes.router import router as dish_router

# from dotenv import load_dotenv
# from pathlib import Path
# load_dotenv(Path(__file__).parent.parent / ".env")


app = FastAPI(
    app_name=settings.app_name,
    version="0.1.0",
    description="FastAPI 练习项目实战",
    lifespan=lifespan
)


register_exception_handlers(app)

app.include_router(dish_router)

# 路由引入
# @app.get("/")
# def read_root(
#     # 使用 FastAPI 的依赖注入系统来获取配置实例
#     # FastAPI 会自动调用 get_settings()，由于缓存的存在，这几乎没有开销
#     settings: Settings = Depends(get_settings),
# ):
#     """
#     一个示例端点，演示如何访问配置。
#     """
#     return {
#         "message": f"Hello from the {settings.app_name}!",
#         # 演示如何使用在模型中动态计算的属性
#         "database_url": settings.database_url,
#         "jwt_secret": settings.jwt_secret,
#     }


@app.get("/health")
async def health_check(response: Response):
    response.status_code = 200
    return {"status": "ok 👍 "}
