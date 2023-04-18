from django.urls import path
from EduZone import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView, LoginView

from AppBase.Routes.blog import *
from AppBase.Routes.tool import *
from AppBase.Routes.notes import *
from AppBase.Routes.blog import *
from AppBase.Routes.common import *
from AppBase.Routes.CommonNotes import *
from AppBase.Routes.admin_page import *

from django.contrib import admin
from django.urls import path
# Initilizes........................

urlpatterns = [
    path('admin/', admin.site.urls),
]


def Make_Join(Componets):
    OutComponets = []
    for i in Componets:
        for j in i:
            OutComponets.append(j)
    return OutComponets

# Urls............................


tools = [
    path('home', home, name='home'),
    path('student_dashboard', student_dashboard, name='student_dashboard'),
    path('AI', AI, name='AI'),
    path('About', About, name='About'),
    path('connect_metamask', connect_metamask, name='connect_metamask'),
    path('contact', contact, name='contact'),
    path('library', library, name='library'),
    path('books', books, name='books'),
    path('', home, name='home'),
    path('toolHome', toolHome, name='toolHome'),
    path('trans', translate_, name='trans'),
    path('convert_text', convert_text, name='convert_text'),
    path('wikipedia_summary', wikipedia_summary, name='wikipedia_summary'),
    path('convert_docx_to_pdf', convert_docx_to_pdf),
    path('convert_pdf_to_docx', convert_pdf_to_docx, name='convert_pdf_to_docx'),
    path('convert_pdf_to_excel', convert_pdf_to_excel,
         name='convert_pdf_to_excel'),
    path('convert_excel_to_pdf', convert_excel_to_pdf),
    path('convert_jpg_to_pdf', convert_jpg_to_pdf),
    path('convert_jpg_to_word', convert_jpg_to_word),
    path('calculator', calculator),
    path('cgpa_calculator', cgpa_calculator),
    path('handwriting_converter', handwriting_converter,
         name='handwriting_converter'),
    path('keyword_to_image', keyword_to_image, name='keyword_to_image'),
    path('video_meeting/<str:room_id>', meeting, name='video_meeting'),
    path('staff_meeting/<str:room_id>', staff_meeting, name='staff_meeting'),
    path('admin_meeting/<str:room_id>', admin_meeting, name='admin_meeting'),
    path('join_meeting', join_meeting, name='join_meeting'),
    path('staff_join_meeting', staff_join_meeting, name='staff_join_meeting'),
    path('admin_join_meeting', admin_join_meeting, name='admin_join_meeting'),

    path('gpa_calculator', gpa_calculator, name='gpa_calculator'),
    path('get_subject', get_subject),
    path('Code_scriping', Code_scriping, name='Code_scriping'),
]
alternative_url = [path('student/video_meeting', meeting),
                   path('student/chat_lobby', lobby),
                   path('student/list_blog', student_list_blog),
                   path('student/chat_home/', chat_home, name='chat_home'),
                   path('student/toolHome', toolHome, name='toolHome'),
                   path('student/logout', LogoutView.as_view)

                   ]

videochat = [
    path('chat_lobby', lobby),
    path('room/', video_chat_room),
    path('get_token/', getToken),

    path('create_member/', createMember),
    path('get_member/', getMember),
    path('delete_member/', deleteMember),
]

common = [
    path('student_home', student_home, name='student_home'),
    path('staff_home', staff_home, name='staff_home'),
]

chatroom = [
    path('chat_home/', chat_home, name='chat_home'),
    path('staff_chat_home/', staff_chat_home, name='staff_chat_home'),
    path('admin_chat_home/', admin_chat_home, name='admin_chat_home'),
    # problem...................
    path('chat/<str:room>/', chat_room, name="chat_room"),
    path('staffchat/<str:room>/', staff_chat_room, name="staff_chat_room"),
    path('adminchat/<str:room>/', admin_chat_room, name="staff_chat_room"),
    path('chat_home/checkview', checkview, name="checkview"),
    path('chat_home/staff_checkview', staff_checkview, name="staff_checkview"),
    path('chat_home/admin_checkview', admin_checkview, name="admin_checkview"),
    path('chat_home/Ncheckview', Ncheckview, name="Ncheckview"),
    path('send', send, name="send"),
    path('getMessages/<str:room>/', getMessages, name="getMessages"),
]


blog_url = [
    path('student_list_blog_course',
         student_list_blog_course, name='student_list_blog_course'),
    path('staff_list_blog_course',
         staff_list_blog_course, name='staff_list_blog_course'),

    path('admin_list_blog_course',
         admin_list_blog_course, name='admin_list_blog_course'),
    path('admin_create_blog', admin_create_blog, name='admin_create_blog'),
    path('staff_list_blog', admin_list_blog, name='admin_list_blog'),

    path('list_blog', student_list_blog, name='student_list_blog'),
    path('staff_list_blog', staff_list_blog, name='staff_list_blog'),
    path('list_blog', teacher_list_blog, name='teacher_list_blog'),
    path('list_edit_blog', list_edit_blog, name='list_edit_blog'),
    path('admin_list_edit_blog', admin_list_edit_blog,
         name='admin_list_edit_blog'),
    path('view_blog/<str:pk>', view_blog, name='view_blog'),
    path('edit_blog/<str:pk>', edit_blog),
    path('create_blog', blog_edit, name='create_blog'),
    path('staff_create_blog', staff_create_blog, name='staff_create_blog'),
    path('save_blog', save_blog),
    path('delete_blog', delete_blog),
    path('edit_blog/save_edit_blog/<int:pk>', save_edit_blog),
]

gallery_ = [

    path("gallery", gallery),
    path('image_upload_page_gallery', image_upload_page_gallery,
         name='image_upload_page_gallery'),
    path('upload_image', upload_image),
    path('delete_image', delete_image),

]


note = [
    path('course_list', course_list, name='course_list'),
    path('course/course_edit/<int:pk>', course_detail, name='course_detail'),
    path('course/<int:pk>/', course_detail, name='course_detail'),
    path('course/add/', course_add, name='course_add'),

    path('ebook/book_list/', book_list, name='book_list'),
    path('ebook/add/', ebook_add, name='ebook_add'),
    path('ebook/<int:pk>/edit/', ebook_edit, name='ebook_edit'),
    path('ebook/<int:pk>/delete/', ebook_delete, name='ebook_delete'),

    path('note/notes_list', notes_list, name='notes_list'),
    path('note/common_notes_list', common_notes_list, name='common_notes_list'),
    path('note/listout_notes', listout_notes, name='listout_notes'),
    path('note/<int:note_id>/', note_detail, name='note_detail'),
    path('note/create/', create_note, name='create_note'),
    path('note/<int:note_id>/update/', update_note, name='update_note'),
    path('note/<int:note_id>/delete/', delete_note, name='delete_note'),
]

AternativeUrls = [
    path('class_listout/<str:class_id>',
         get_class_peoples, name='class_listout'),
]


urlpatterns.extend(Make_Join([tools, note, gallery_, blog_url,
                   chatroom,  videochat, alternative_url]))
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
