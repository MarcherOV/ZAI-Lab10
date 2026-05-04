import os, json, time, glob, re
from django.conf import settings
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from offer.models import Course, Registration, MessageTemplate
from issues.models import Issue
from .serializers import CourseSerializer, RegistrationSerializer, IssueSerializer


class FormTemplateView(APIView):
    def get(self, request):
        # *Plik JSON z definicją formularza
        file_path = os.path.join(settings.BASE_DIR, 'src', 'media', 'form_1767566536.json')
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return Response(data)
        except FileNotFoundError:
            return Response({'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)


class MessageTemplateView(APIView):
    def get(self, request):
        # *Tabela BD z treścią szablonu -> HTML
        templates = MessageTemplate.objects.all()
        html_content = "".join([f"<div>{t.content_html}</div>" for t in templates])
        return HttpResponse(html_content, content_type="text/html")


class CategoryListView(APIView):
    def get(self, request):
        # **Kategorie zapisane na stałe
        hardcoded_categories = [
            {'id': 1, 'name': 'IT'},
            {'id': 2, 'name': 'Zarządzanie'},
            {'id': 3, 'name': 'Marketing'}
        ]
        return Response(hardcoded_categories)


class CourseListView(APIView):
    def get(self, request):
        # **Tabela BD, serializowane dane
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class RegistrationListView(APIView):
    def get(self, request):
        # **Tabela BD, serializowane dane (lista osób)
        regs = Registration.objects.all()
        serializer = RegistrationSerializer(regs, many=True)
        return Response(serializer.data)


class RegistrationCreateView(APIView):
    def post(self, request):
        # Zapis do Tabeli BD
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Zapisano', 'id': serializer.instance.id}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class RegistrationDetailView(APIView):
    def get(self, request, id):
        # **Tabela BD, serializowane dane (jedna osoba)
        try:
            reg = Registration.objects.get(id=id)
            serializer = RegistrationSerializer(reg)
            return Response(serializer.data)
        except Registration.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)


class ProblemReportCreateView(APIView):
    def post(self, request):
        # zapis -> Tabela BD
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Zgłoszono problem', 'id': serializer.instance.id}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ProblemListView(APIView):
    def get(self, request):
        # Tabela BD, serializowane dane (lista)
        issues = Issue.objects.all()
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)


# --- Класи для Генератора Форм ---

class FieldListView(APIView):
    def get(self, request):
        fields = ['Imie', 'Nazwisko', 'Email', 'Telefon']
        return Response({'status': 'success', 'data': fields})


class DocumentSaveView(APIView):
    def post(self, request):
        data = request.data
        save_mode = data.get('saveMode', 'file')
        doc_type = data.get('type', 'form')
        
        try:
            if save_mode == 'db':
                doc = MessageTemplate.objects.create(
                    name=f"Doc_{doc_type}",
                    content_html=json.dumps(data)
                )
                return Response({'status': 'success', 'message': f'Server: Zapisano w DB (ID: {doc.id})'})
            else:
                media_dir = os.path.join(settings.BASE_DIR, 'media')
                os.makedirs(media_dir, exist_ok=True)
                filename = f"{doc_type}_{int(time.time())}.json"
                file_path = os.path.join(media_dir, filename)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4)
                return Response({'status': 'success', 'message': 'Server: Zapisano w pliku JSON'})
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DocumentListView(APIView):
    def get(self, request):
        mode = request.GET.get('mode', 'file')
        result = []
        
        if mode == 'db':
            docs = MessageTemplate.objects.all().order_by('-id')
            for doc in docs:
                result.append(f"DB: #{doc.id} ({doc.name})")
        else:
            media_dir = os.path.join(settings.BASE_DIR, 'media')
            if os.path.exists(media_dir):
                files = glob.glob(os.path.join(media_dir, '*.json'))
                for file in files:
                    result.append(os.path.basename(file))
                    
        return Response({'status': 'success', 'data': result})


class DocumentLoadView(APIView):
    def get(self, request):
        target = request.GET.get('target', '')
        try:
            if target.startswith('DB: #'):
                match = re.search(r'#(\d+)', target)
                if match:
                    doc_id = int(match.group(1))
                    doc = MessageTemplate.objects.get(id=doc_id)
                    return Response(json.loads(doc.content_html))
            else:
                file_path = os.path.join(settings.BASE_DIR, 'media', target)
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    return Response(data)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({'status': 'error', 'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)