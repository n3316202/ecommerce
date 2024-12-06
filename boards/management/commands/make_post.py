import sys
from typing import Any
from django.core.management import BaseCommand

from boards.models import Post



class Command(BaseCommand):
    def handle(self, *args, **options):
        print("make post start :)")

        for i in range(1, 101):
            # Todo.objects.create(name=f"테스트 todo {i}", complete=choice([True, False]))
            # todo = Todo.objects.create(name=f"테스트 todo {i}")
            post, created = Post.objects.get_or_create(title=f"테스트 post {i}",content=f"테스트 post {i}")
            if created:
                print(f"{i}번째 todo 생성 완료")
            else:
                print(f"{i}번째 todo 이미 존재")
        
        sys.stdout.write(self.style.SUCCESS("make post end :)"))
        print(post)

        