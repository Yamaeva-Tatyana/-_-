def find_common_participants(participants_group1, participants_group2, divider = ","):
    common_participants = list(set(participants_group1.split(divider)).intersection(participants_group2.split(divider)))
    common_participants.sort()

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group, participants_second_group, "|")