from django.contrib import admin # type: ignore
from todolist_app.models import TaskList

admin.site.register(TaskList)