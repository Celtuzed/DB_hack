def fix_marks(schoolkid='Фролов Иван'):
    child = Schoolkid.objects.get(full_name__contains=schoolkid)
    marks = Mark.objects.filter(schoolkid=child)
    child_bad_marks = marks.filter(points__lte=3)
    for mark in range(child_bad_marks.count()):
        child_bad_mark = child_bad_marks.first()
        child_bad_mark.points = 5
        child_bad_mark.save()


def remove_chastisements(schoolkid='Фролов Иван'):
    child = Schoolkid.objects.get(full_name__contains=schoolkid)
    chastisements = Chastisement.objects.filter(schoolkid=child)
    for chastisement in chastisements:
        chastisement.delete()


def create_commendation(schoolkid='Фролов Иван', subject_title='Музыка'):
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

