from user_service.models import Resturant


def get_available_resturants(db, hour: int):
    return db.query(Resturant).filter(
        Resturant.open_hour <= hour,
        Resturant.close_hour >= hour,
        Resturant.is_open == True
    ).all()
