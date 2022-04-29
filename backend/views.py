from django.forms import EmailInput
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from .permissions import IsCEO, IsCommunityManager, IsITSupport, IsAccountant
from .serializers import LoginSerializer, SubscriptionListSerializer, UserListSerializer, AdminUserSerializer, TicketSerializer, UserSerializer, SessionsSerializer, SubscriptionSerializer, NewsLetterSerializer
from .models import User, Sessions, Ticket, Subscription, NewsLetter
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .utils import Util
from .models import Sessions, Ticket, User, Subscription, NewsLetter
from rest_framework.authtoken.models import Token 


class CeoRegisterUser(generics.GenericAPIView):
    permission_classes = [IsCEO]
    serializer_class = AdminUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            first_name = serializer.validated_data['first_name'].capitalize()
            last_name = serializer.validated_data['last_name'].capitalize()
            username = serializer.validated_data['username'].capitalize()
            mobile_number = serializer.validated_data['mobile_number']
            email = serializer.validated_data['email']
            duties = serializer.validated_data['duties']
            password = serializer.validated_data['password']
            try:
                user = User.objects.create(first_name=first_name, last_name=last_name, username=username, mobile_number=mobile_number, email=email, duties=duties)
                user.set_password(password)
                user.save()
                return Response({"success":f"{username} created successfully"}, status=status.HTTP_201_CREATED)
            except Exception as err:
                return Response({"error":err}, status = status.HTTP_400_BAD_REQUEST)

        return Response({"error":serializer.errors}, status = status.HTTP_400_BAD_REQUEST)


class CeoUpdateUser(generics.GenericAPIView):
    permission_classes = [IsCEO]
    serializer_class = AdminUserSerializer

    def get(self, request, pk):
        user =User.objects.filter(pk-pk).first()
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        user =User.objects.filter(pk-pk).first()
        serializer = self.serializer_class(user, data =request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user =User.objects.filter(pk-pk).first()
        username = user.username
        user.delete()
        return Response({"success":f"{username} deleted successfully"}, status=status.HTTP_201_CREATED)


class RegisterUsers(generics.GenericAPIView):
    permissions_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    """Endpoint to register other users who are not staffs"""
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            first_name =serializer.validated_data['first_name']
            last_name = serializer.validated_data['last_name']
            email = serializer.validated_data['email']
            mobile_number = serializer.validated_data['mobile_number']
            password = serializer.validated_data['password']
            try:    
                user = User.objects.create_user(
                    username=username, 
                    first_name=first_name,
                    last_name=last_name, 
                    email=email, 
                    mobile_number=mobile_number,
                    password=password
                    )
                user.set_password(password)
                user.save()
                return Response({"success":"successfully created"}, status=status.HTTP_201_CREATED)
            except Exception as error:
                return Response({"error":str(error)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateUserByCommunityManager(generics.GenericAPIView):
    permissions_classes = [IsCommunityManager]
    serializer_class = UserSerializer
    queryset = ''
    """Endpoint to check if a user exists only accessible by Community Manager"""
    def get_user(self, pk):
        try:
            user =User.objects.get(pk=pk)   
            return user
        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
    """Endpoint to get a user only accessible by Community Manager"""
    def get(self, request, pk):
        user = self.get_user(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    """Endpoint to update a user only accessible by Community Manager"""

    def patch(self, request, pk):
        user = self.get_user(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        try:
            if serializer.is_valid():
                if user.duties == "CEO":
                    return Response({"error": "You are not allowed to update this user"}, status=status.HTTP_400_BAD_REQUEST)
                if user.duties == "Admin":
                    return Response({"error": "You are not allowed to update this user"}, status=status.HTTP_400_BAD_REQUEST)
                if user.duties == "IT Support":
                    return Response({"error": "You are not allowed to update this user"}, status=status.HTTP_400_BAD_REQUEST)
                if user.duties == "Accountant":
                    return Response({"error": "You are not allowed to update this user"}, status=status.HTTP_400_BAD_REQUEST)
                if user.duties == "Community manager" and user.id != request.user.id:
                    return Response({"error": "You are not allowed to update this user"}, status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                return Response({"success": f"{user.username} successfully updated"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({"error":str(error)}, status=status.HTTP_400_BAD_REQUEST)

class Login(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        try:
            if email is None or password is None:
                return Response({'invalid_credentials': 'please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)
            user = authenticate(username=email, password=password)
            if not user:
                return Response({'invalid_credentials': 'Ensure both email and password are correct and you have verified your account'}, status=status.HTTP_400_BAD_REQUEST)
            token,_ = Token.objects.get_or_create(user=user)
            return Response({"data":token.key, "username":user.username}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({"success": False}, status=status.HTTP_400_BAD_REQUEST)


class ViewAllUsers(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = [IsCEO | IsCommunityManager]
    serializer_class = UserListSerializer

class SendNewsLetter(generics.GenericAPIView):
    permissions_classes = [IsCommunityManager]
    serializer_class = NewsLetterSerializer
    """Endpoint to send a newsletter to all users only accessible by Community Manager"""
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        get_all_users_emails = User.objects.all().values_list('email', flat=True)
        if serializer.is_valid():
            title = serializer.validated_data['title']
            topic = serializer.validated_data['topic']
            newsletter = NewsLetter.objects.create(
                title = title,
                topic = topic
            )
            newsletter.save()
            try:
                for email in get_all_users_emails:
                    email_topic = f"{title} \n\n {topic}"
                    data = data = {'email_topic': email_topic, 'to_email': email, 'email_subject': title}
                    Util.send_mail(data)
                return Response({"success": f"{title} successfully sent"}, status=status.HTTP_201_CREATED)
            except Exception as error:
                return Response({"error":str(error)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateSubscription(generics.GenericAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = SubscriptionSerializer
    """Endpoint for users to create a subscription"""
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        user = request.user
        print(user)
        if serializer.is_valid():
            plans = serializer.validated_data['plans']
            try:
                Subscription.objects.create(plans=plans, user=user)
                return Response({"success": f"{user} successfully subscribed"}, status=status.HTTP_201_CREATED)
            except Exception as error:
                return Response({"error":str(error)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateSubscription(generics.GenericAPIView):
    permissions_classes = [IsAccountant]
    serializer_class = SubscriptionListSerializer
    queryset = ''
    """Endpoint to check if a user exists only accessible by Accountant"""
    def get_user(self, pk):
        try:
            user =User.objects.get(pk=pk)   
            return user
        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
    """Endpoint to get a user if he is a subscriber only accessible by Accountant"""
    def get(self, request, pk):
        user = self.get_user(pk)
        get_subscription = Subscription.objects.filter(user=user).first()
        serializer = SubscriptionListSerializer(get_subscription)
        return Response(serializer.data, status=status.HTTP_200_OK)
    """Endpoint to update a user subscription only accessible by Accountant"""
    def patch(self, request, pk): 
        user = self.get_user(pk)
        get_subscription = Subscription.objects.filter(user=user).first()
        serializer = SubscriptionListSerializer(get_subscription, data=request.data, partial=True)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response({"success": f"{get_subscription} successfully updated"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({"error":str(error)}, status=status.HTTP_400_BAD_REQUEST)

class CreateSession(generics.GenericAPIView):
    permissions_classes = [IsITSupport]
    serializer_class = SessionsSerializer
    """Endpoint to create a session"""
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            users = serializer.validated_data['users']
            title = serializer.validated_data['title']
            description = serializer.validated_data['description']
            date = serializer.validated_data['date']
            is_booked = serializer.validated_data['is_booked']
            try:
                Sessions.objects.create(title=title, date=date, description=description, user=users[0], is_booked=is_booked)
                return Response({"success": f"A session has been created for {users}"}, status=status.HTTP_201_CREATED)
            except Exception as error:
                return Response({"error":str(error)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateSession(generics.GenericAPIView):
    permissions_classes = [IsITSupport]
    serializer_class = SessionsSerializer
    queryset = ''
    """Endpoint to get all sessions"""
    def get(self, request):
        get_sessions = Sessions.objects.all()
        serializer = SessionsSerializer(get_sessions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    """Endpoint to update session progress"""
    def patch(self, request, pk):
        get_session = Sessions.objects.get(pk=pk)
        serializer = SessionsSerializer(get_session, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": f"{get_session} successfully updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateTickets(generics.GenericAPIView):
    permissions_classes = [IsITSupport]
    serializer_class = TicketSerializer
    """Endpoint to create a ticket"""
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            users = serializer.validated_data['users']
            ticket_title = serializer.validated_data['ticket_title']
            ticket_description = serializer.validated_data['ticket_description']
            is_resolved = serializer.validated_data['is_resolved']
            try:
                Ticket.objects.create(ticket_title=ticket_title, ticket_description=ticket_description, is_resolved=is_resolved, user=users[0])
                return Response({"success": f"A ticket has been created for {users}"}, status=status.HTTP_201_CREATED)
            except Exception as error:
                return Response({"error":str(error)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateTickets(generics.GenericAPIView):
    permissions_classes = [IsITSupport]
    serializer_class = TicketSerializer
    queryset = ''
    """Endpoint to get all tickets"""
    def get(self, request):
        get_tickets = Ticket.objects.all()
        serializer = TicketSerializer(get_tickets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    """Endpoint to update ticket progress"""
    def patch(self, request, pk):
        get_ticket = Ticket.objects.get(pk=pk)
        serializer = TicketSerializer(get_ticket, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": f"{get_ticket} successfully resolved"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD)
