def lift_function(waiting_people, current_state_of_the_lift):
    for i in range(len(current_state_of_the_lift)):
        if waiting_people > 3:
            current_number_of_people = abs(4 - int(current_state_of_the_lift[i]))
            waiting_people -= current_number_of_people
            current_state_of_the_lift[i] += current_number_of_people
        else:
            current_state_of_the_lift[i] += waiting_people
            waiting_people = 0

    if waiting_people > 0:
        print(f"There isn't enough space! {waiting_people} people in a queue!")
    elif sum(current_state_of_the_lift) != len(current_state_of_the_lift) * 4:
        print("The lift has empty spots!")

    return " ".join([str(num) for num in current_state_of_the_lift])


people = int(input())
lift = [int(num) for num in input().split()]

print(lift_function(people, lift))
