pesnia = input().split()
slog = []
for word in pesnia:
    count = 0
    for glasn in word:
        if glasn in "аеёиоуэюяАЕЁИОУЭЮЯ":
            count += 1
    slog.append(count)
if len(set(slog)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")