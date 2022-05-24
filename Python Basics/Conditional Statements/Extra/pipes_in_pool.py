volume = int(input())
pipe_one_per_hour = int(input())
pipe_two_per_hour = int(input())
hours = float(input())

pipe_one = pipe_one_per_hour * hours
pipe_two = pipe_two_per_hour * hours
both_pipes = pipe_one + pipe_two
overflow = 0

if both_pipes <= volume:
    volume_percentage = (both_pipes / volume) * 100
    pipe_one_percentage = (pipe_one / both_pipes) * 100
    pipe_two_percentage = (pipe_two / both_pipes) * 100
    print(f"The pool is {volume_percentage:.2f}% full. Pipe 1: {pipe_one_percentage:.2f}%. Pipe 2: {pipe_two_percentage:.2f}%.")
else:
    overflow = both_pipes - volume
    print(f"For {hours} hours the pool overflows with {overflow:.2f} liters.")
