# app/container.py

from dependency_injector import containers, providers
from app.services.timeline_service import TimelineService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["app.views.main"])  # Указываем модуль, где используется внедрение зависимостей

    config = providers.Configuration()

    my_service = providers.Factory(
        TimelineService,
    )
