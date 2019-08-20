# Generated by Django 2.2.4 on 2019-08-20 18:09

from django.contrib.contenttypes.models import ContentType
from django.db import migrations

from issue.models import IssueAction, Issue


def normalize_generic_issues(apps, schema_editor):
    """
    Normalize related issues as generic reference
    """
    for issue_action in IssueAction.objects.all():
        issue_action.action_issue_type = ContentType.objects.get_for_model(Issue)
        issue_action.action_issue_id = issue_action.issue_id
        issue_action.save(update_fields=['action_issue_type', 'action_issue_id'])


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0006_auto_20190820_1806'),
    ]

    operations = [
        migrations.RunPython(normalize_generic_issues)
    ]
