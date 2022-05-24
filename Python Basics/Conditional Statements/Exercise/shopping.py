budget = float(input())
num_video_cards = int(input())
num_processors = int(input())
num_ram_storage = int(input())

price_video_card = 250
video_cards = price_video_card * num_video_cards
price_processor = 0.35 * video_cards
price_ram_storage = 0.10 * video_cards
processors = num_processors * price_processor
ram_storage = num_ram_storage * price_ram_storage
total = video_cards + processors + ram_storage

if num_video_cards > num_processors:
    total = total - (total * 0.15)

difference = abs(total - budget)

if total <= budget:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
