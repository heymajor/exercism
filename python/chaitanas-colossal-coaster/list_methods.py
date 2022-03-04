def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue:  list - names in the normal queue.
    :param ticket_type:  int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """
    if ticket_type:
        express_queue.append(person_name)
        return express_queue
    else:
        normal_queue.append(person_name)
        return normal_queue


# print(
#     add_me_to_the_queue(
#         express_queue=["Tony", "Bruce"],
#         normal_queue=["RobotGuy", "WW"],
#         ticket_type=1,
#         person_name="RichieRich",
#     )
# )
# print(
#     add_me_to_the_queue(
#         express_queue=["Tony", "Bruce"],
#         normal_queue=["RobotGuy", "WW"],
#         ticket_type=0,
#         person_name="HawkEye",
#     )
# )


def find_my_friend(queue, friend_name):
    """

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """
    return queue.index(friend_name)


# print(
#     find_my_friend(
#         queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], friend_name="Steve"
#     )
# )


def add_me_with_my_friends(queue, index, person_name):
    """

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """
    queue.insert(index, person_name)
    return queue


# print(
#     add_me_with_my_friends(
#         queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"],
#         index=1,
#         person_name="Bucky",
#     )
# )


def remove_the_mean_person(queue, person_name):
    """

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return:  list - queue update with the mean persons name removed.
    """
    queue.remove(person_name)
    return queue


# print(
#     remove_the_mean_person(
#         queue=["Natasha", "Steve", "Eltran", "Wanda", "Rocket"], person_name="Eltran"
#     )
# )


def how_many_namefellows(queue, person_name):
    """

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return:  int - the number of times the name appears in the queue.
    """
    return queue.count(person_name)


# print(
#     how_many_namefellows(
#         queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"], person_name="Natasha"
#     )
# )


def remove_the_last_person(queue):
    """

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """
    name = queue[len(queue) - 1]
    queue.remove(name)

    return name


# print(remove_the_last_person(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]))


def sorted_names(queue):
    """

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """
    queue.sort()
    return queue


print(sorted_names(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]))
