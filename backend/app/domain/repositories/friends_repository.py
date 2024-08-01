from app.domain.entities.friends import FriendRequest, RequestStatus, db
from app.domain.entities.user import User

class FriendRequestRepository:
    
    @staticmethod
    def get_all_friend_requests():
        return FriendRequest.query.all()
    
    @staticmethod
    def get_friend_request_by_id(request_id):
        return FriendRequest.query.get(request_id)
    
    @staticmethod
    def get_requests_by_sender_username(sender_username):
        sender = User.query.filter_by(username=sender_username).first()
        if sender:
            return FriendRequest.query.filter_by(sender_id=sender.user_id).all()
        return []

    @staticmethod
    def get_requests_by_receiver_username(receiver_username):
        receiver = User.query.filter_by(username=receiver_username).first()
        if receiver:
            return FriendRequest.query.filter_by(receiver_id=receiver.user_id).all()
        return []

    @staticmethod
    def create_friend_request(sender_username, receiver_username):
        sender = User.query.filter_by(username=sender_username).first()
        receiver = User.query.filter_by(username=receiver_username).first()
        
        if sender and receiver:
            new_request = FriendRequest(sender_id=sender.user_id, receiver_id=receiver.user_id)
            db.session.add(new_request)
            db.session.commit()
            return new_request
        return None
    
    @staticmethod
    def update_friend_request(request_id, status):
        request_obj = FriendRequest.query.get(request_id)
        if request_obj:
            request_obj.status = status
            db.session.commit()
        return request_obj
    
    @staticmethod
    def delete_friend_request(request_id):
        request_obj = FriendRequest.query.get(request_id)
        if request_obj:
            db.session.delete(request_obj)
            db.session.commit()
        return request_obj