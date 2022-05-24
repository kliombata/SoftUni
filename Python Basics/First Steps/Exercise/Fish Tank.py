lenght = int(input())
width = int(input())
height = int(input())
percentage = int(input())

volume_cm = lenght * width * height
volume_l = volume_cm / 1000
conversion = percentage / 100
volume = volume_l - (volume_l * conversion)

print (volume)