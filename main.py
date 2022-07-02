def fix_marks(schoolkid='Фролов Иван'):
    try:
        child = Schoolkid.objects.get(full_name__contains=schoolkid)
        marks = Mark.objects.filter(schoolkid=child)
        child_bad_marks = marks.filter(points__lte=3)
        child_bad_marks.update(points=5)
    except Schoolkid.MultipleObjectsReturned:
        print("При поиске человека было найдено несколько людей с таким именем.")
    except Schoolkid.DoesNotExist:
        print("Такого человека не было найдено в базе данных")


def remove_chastisements(schoolkid='Фролов Иван'):
    try:
        child = Schoolkid.objects.get(full_name__contains=schoolkid)
        Chastisement.objects.filter(schoolkid=child).delete()
    except Schoolkid.MultipleObjectsReturned:
        print("При поиске человека было найдено несколько людей с таким именем")
    except Schoolkid.DoesNotExist:
        print("Такого человека не было найдено в базе данных")


def create_commendation(schoolkid='Фролов Иван', subject_title='Музыка'):
    try:
        commendation_text=[
            "Молодец!",
            "Отлично!",
            "Хорошо!",
            "Гораздо лучше, чем я ожидал!",
            "Здорово!"
        ]
        child = Schoolkid.objects.get(full_name__contains=schoolkid)
        subject = Subject.objects.filter(title=subject_title, year_of_study=child.year_of_study).first()
        lesson = Lesson.objects.filter(subject=subject, year_of_study=child.year_of_study, group_letter=child.group_letter).order_by('?').first()
        Commendation.objects.create(schoolkid=child, teacher=lesson.teacher, subject=lesson.subject, created=lesson.date, text=random.choice(commendation_text))
    except Schoolkid.MultipleObjectsReturned:
        print("При поиске человека было найдено несколько людей с таким именем")
    except Schoolkid.DoesNotExist:
        print("Такого человека не было найдено в базе данных")
    except AttributeError:
        print("Название урока введено не верно")
