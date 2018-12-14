# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-13 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0115_roundpage_mentor_intern_selection_deadline'),
    ]

    operations = [
        migrations.CreateModel(
            name='InitialMentorFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_edits', models.BooleanField(editable=False)),
                ('in_contact', models.BooleanField(help_text='Has your intern been in contact to discuss how to approach their first tasks?')),
                ('asking_questions', models.BooleanField(help_text='Has your intern been asking questions about their first tasks?')),
                ('active_in_public', models.BooleanField(help_text="Has your intern been active on public project channels, such as the community's chat, forums, issue tracker, mailing list, etc?")),
                ('provided_onboarding', models.BooleanField(help_text='Have you provided documentation or other resources to help onboard your intern?')),
                ('checkin_frequency', models.CharField(choices=[('', 'Not scheduled yet'), ('D', 'Once per day'), ('M', 'Multiple times per week'), ('W', 'Once per week'), ('B', 'Every other week')], default='', help_text="How often do you have a real-time chat, video conference, or phone conversation to check in with your intern's progress on tasks?", max_length=1)),
                ('last_contact', models.DateField(help_text='What was the last date you were in contact with your intern?')),
                ('intern_response_time', models.CharField(choices=[('1H', '1 hour'), ('3H', '3 hours'), ('6H', '6 hours'), ('12H', '12 hours'), ('1D', '1 day'), ('2D', '2-3 days'), ('4D', '4-5 days'), ('6D', '6-7 days'), ('>7D', '> 7 days')], help_text='On average, how long does it take for your intern to respond to your questions or feedback?', max_length=3)),
                ('mentor_response_time', models.CharField(choices=[('1H', '1 hour'), ('3H', '3 hours'), ('6H', '6 hours'), ('12H', '12 hours'), ('1D', '1 day'), ('2D', '2-3 days'), ('4D', '4-5 days'), ('6D', '6-7 days'), ('>7D', '> 7 days')], help_text="On average, how long does it take for you to respond to your intern's questions or requests for feedback?", max_length=3)),
                ('progress_report', models.TextField(help_text="Please provide a paragraph describing your intern's progress on establishing communication with you, and ramping up on their first tasks.")),
                ('full_time_effort', models.BooleanField(help_text='Do you believe your Outreachy intern is putting in a full-time, 40 hours a week effort into the internship?')),
                ('payment_approved', models.BooleanField(help_text='Should your Outreachy intern be paid the initial $1,000 payment? Please base your answer on whether your intern has established communication with their mentors and has start learning how to tackle their first tasks.')),
                ('request_extension', models.BooleanField(help_text='Sometimes interns do not put in a full-time effort. In this case, one of the options is to delay payment of their stipend and extend their internship a specific number of weeks. You will be asked to re-evaluate your intern after the extension is done.')),
                ('extension_date', models.DateField(help_text="If you want to extend the internship, please pick a date when you will be asked to update your intern's initial feedback and authorize payment. Internships can be extended for up to five weeks. We don't recommend extending an internship for more than 1 week at initial feedback.")),
                ('intern_selection', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.InternSelection')),
            ],
        ),
    ]