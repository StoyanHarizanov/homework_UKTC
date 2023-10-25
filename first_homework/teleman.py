name_of_serial = input()
count_of_seasons = int(input())
count_of_episodes = int(input())
time_per_episode = int(input())

episode_with_adds = time_per_episode - (time_per_episode * 0.25)
count_without_the_specials = count_of_seasons * (count_of_episodes - 1)
time_without_specials = count_without_the_specials * episode_with_adds
special_with_adds = time_per_episode + 12 - ((time_per_episode + 12) * 0.25)
count_specials = count_of_seasons * special_with_adds
total_time = time_without_specials + count_specials
print(total_time)
