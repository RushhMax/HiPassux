from app.domain.repositories.friends_repository import FriendRequestRepository, RequestStatus, User

class FriendRequestService:
    
    @staticmethod
    def get_all_friend_requests():
        try:
            requests = FriendRequestRepository.get_all_friend_requests()
            return {
                'success': True,
                'message': "Requests fetched successfully",
                'data': [request.to_dict() for request in requests]
            }
        except Exception as e:
            return {'success': False, 'message': str(e)}
    
    @staticmethod
    def send_friend_request(sender_username, receiver_username):
        if sender_username == receiver_username:
            return {'success': False, 'message': "No puedes enviarte una solicitud a ti mismo."}

        try:
            existing_request = FriendRequestRepository.get_requests_by_sender_username(sender_username)
            if any(request.receiver_id == User.query.filter_by(username=receiver_username).first().user_id for request in existing_request):
                return {'success': False, 'message': "Ya has enviado una solicitud a este usuario."}

            new_request = FriendRequestRepository.create_friend_request(sender_username, receiver_username)
            if new_request:
                return {'success': True, 'message': "Solicitud enviada exitosamente", 'data': new_request.to_dict()}
            return {'success': False, 'message': "No se pudo crear la solicitud."}
        except Exception as e:
            return {'success': False, 'message': str(e)}
    
    @staticmethod
    def respond_to_friend_request(request_id, action):
        if action not in ['accept', 'reject']:
            return {'success': False, 'message': "Acción inválida."}

        try:
            request_obj = FriendRequestRepository.get_friend_request_by_id(request_id)
            if not request_obj:
                return {'success': False, 'message': "Solicitud no encontrada."}

            if action == 'accept':
                request_obj = FriendRequestRepository.update_friend_request(request_id, RequestStatus.ACCEPTED)
            elif action == 'reject':
                request_obj = FriendRequestRepository.update_friend_request(request_id, RequestStatus.REJECTED)

            return {'success': True, 'message': "Solicitud respondida exitosamente", 'data': request_obj.to_dict()}
        except Exception as e:
            return {'success': False, 'message': str(e)}