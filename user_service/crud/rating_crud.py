from user_service.models import Rating

def submit_rating(db, rating_data):
    new_rating = Rating(
        order_id=rating_data.order_id,
        resturant_rating=rating_data.resturant_rating,
        agent_rating=rating_data.agent_rating,
        comments=rating_data.comments
    )
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)
    return new_rating
