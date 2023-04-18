# Generated by Django 3.0.2 on 2023-04-18 05:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendees',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('class_id', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('roll_no', models.CharField(max_length=100)),
                ('subject_states', models.CharField(max_length=50)),
                ('Date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='UnTitled', max_length=200)),
                ('description', models.CharField(default='Author not provied any description', max_length=200)),
                ('content', models.CharField(default='Author not provied any description', max_length=2000)),
                ('blog_profile_img', models.CharField(default='https://www.equalityhumanrights.com/sites/default/files/styles/listing_image/public/default_images/blog-teaser-default-full_5.jpg?itok=YOsTg-7X', max_length=2000)),
                ('blog_type', models.CharField(default='Blog', max_length=2000)),
                ('categories', models.CharField(max_length=200)),
                ('updated_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='class_enrolled',
            fields=[
                ('user_id', models.IntegerField()),
                ('mail_id', models.CharField(max_length=200)),
                ('class_id', models.IntegerField(primary_key=True, serialize=False)),
                ('subject_code', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('question_number', models.PositiveIntegerField()),
                ('total_marks', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='daily_test',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('student_id', models.IntegerField()),
                ('Mark', models.CharField(max_length=50)),
                ('Date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Daily_test_mark',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('class_id', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('roll_no', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
                ('mark', models.IntegerField()),
                ('Date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_id', models.IntegerField()),
                ('image', models.ImageField(default='images/user_image.png', upload_to='photo/%Y/%m/%d')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('designation', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=200)),
                ('coming_from', models.CharField(max_length=200)),
                ('mail_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('event_name', models.CharField(max_length=100)),
                ('event_photo', models.URLField()),
                ('event_description', models.TextField()),
                ('poster_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty_details',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=200, unique=True)),
                ('image', models.ImageField(default='images/Screenshot_3.png', upload_to='photo/%Y/%m/%d')),
                ('id_number', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200, unique=True)),
                ('designation', models.CharField(default='designation', max_length=200)),
                ('date_of_join', models.DateField(default=django.utils.timezone.now)),
                ('department', models.CharField(default='department', max_length=200)),
                ('qualififcation', models.CharField(default='qualififcation', max_length=200)),
                ('assessment_period', models.IntegerField(default=0)),
                ('experience', models.IntegerField(default=0)),
                ('bio', models.CharField(default='No Bio yet.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FooterEditPage',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('InstituteName', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('PhoneNumber', models.CharField(max_length=200)),
                ('EXN', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200)),
                ('last_updated_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('G_id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(default='images/user_image.png', upload_to='Gallery/%Y/%m/%d')),
                ('categories', models.CharField(max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Internal_test_mark',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('class_id', models.CharField(max_length=100)),
                ('roll_no', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
                ('mark', models.IntegerField()),
                ('assesment_no', models.IntegerField()),
                ('Date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='logo',
            fields=[
                ('L_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Reson', models.CharField(max_length=200)),
                ('image', models.ImageField(default='images/user_image.png', upload_to='logo')),
                ('last_updated_date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'get_latest_by': ['image'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=10000000)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('room', models.CharField(max_length=1000000)),
                ('user', models.CharField(max_length=1000000)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cover_image', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('semester', models.CharField(max_length=100)),
                ('notes_title', models.CharField(max_length=100)),
                ('regulation', models.CharField(max_length=100)),
                ('subcode', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='notes/')),
            ],
        ),
        migrations.CreateModel(
            name='NoteCourse',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('course_id', models.CharField(max_length=50)),
                ('semester', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='RoomMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('uid', models.CharField(max_length=1000)),
                ('room_name', models.CharField(max_length=200)),
                ('insession', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sec_Daily_test_mark',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('class_id', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('roll_no', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
                ('mark', models.IntegerField()),
                ('Date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaLinks',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Twitter', models.CharField(max_length=200)),
                ('Facebook', models.CharField(max_length=200)),
                ('Instagram', models.CharField(max_length=200)),
                ('LinkedIn', models.CharField(max_length=200)),
                ('last_updated_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Subject_handled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_id', models.IntegerField()),
                ('subject_name', models.CharField(max_length=200)),
                ('subject_code', models.CharField(max_length=200)),
                ('target_pass', models.CharField(default='10', max_length=200)),
                ('actual_pass', models.CharField(default='10', max_length=200)),
                ('subject_staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBase.Faculty_details')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_image', models.CharField(max_length=200)),
                ('subject_name', models.CharField(max_length=200, unique=True)),
                ('subject_code', models.CharField(max_length=200, unique=True)),
                ('semester', models.IntegerField()),
                ('department', models.CharField(max_length=200)),
                ('discription', models.CharField(default='No Discription yet.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('T_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('image', models.ImageField(default='images/user_image.png', upload_to='Testimonials/%Y/%m/%d')),
                ('description', models.CharField(max_length=200)),
                ('categories', models.CharField(max_length=200)),
                ('last_updated_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=200)),
                ('mail_id', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('role', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='URLForClass',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Class_id', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='ebooks')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBase.NoteCourse')),
            ],
        ),
        migrations.CreateModel(
            name='Test_evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=200)),
                ('target_pass', models.CharField(max_length=200)),
                ('actual_pass', models.CharField(max_length=200)),
                ('subject_detials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBase.Subject_handled')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/Teacher/')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=False)),
                ('department', models.CharField(max_length=40)),
                ('salary', models.PositiveIntegerField(null=True)),
                ('Annauni_num', models.CharField(default='0000000', max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/Student/')),
                ('address', models.CharField(max_length=40)),
                ('mail_id', models.CharField(default='sample@gmail.com', max_length=40)),
                ('mobile', models.CharField(max_length=20)),
                ('joinned_year', models.DateField(default=django.utils.timezone.now)),
                ('role_no', models.IntegerField()),
                ('department', models.CharField(max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBase.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBase.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.PositiveIntegerField()),
                ('question', models.CharField(max_length=600)),
                ('option1', models.CharField(max_length=200)),
                ('option2', models.CharField(max_length=200)),
                ('option3', models.CharField(max_length=200)),
                ('option4', models.CharField(max_length=200)),
                ('answer', models.CharField(choices=[('Option1', 'Option1'), ('Option2', 'Option2'), ('Option3', 'Option3'), ('Option4', 'Option4')], max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBase.Course')),
            ],
        ),
        migrations.AddField(
            model_name='faculty_details',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBase.Users'),
        ),
        migrations.CreateModel(
            name='EbookForClass',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cover_image', models.CharField(max_length=100)),
                ('Class_id', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='ebooks')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBase.NoteCourse')),
            ],
        ),
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='ebooks')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBase.NoteCourse')),
            ],
        ),
        migrations.CreateModel(
            name='ClassRooms',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('class_image', models.CharField(max_length=200)),
                ('class_name', models.CharField(max_length=200)),
                ('subject_code', models.CharField(max_length=200, unique=True)),
                ('semester', models.IntegerField()),
                ('department', models.CharField(max_length=200)),
                ('discription', models.CharField(default='No Discription yet.', max_length=200)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBase.Faculty_details')),
            ],
        ),
    ]