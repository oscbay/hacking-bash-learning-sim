import random


def questions():
    question_list = {
        'What is the name for the test that happens before the OS is booted?': 'post',
        'What is the name for the hardware settings?': 'bios',
        'What is the name of the system that assigns IP addresses to devices on a network?': 'dhcp',
        'What is the open version of high definition multimedia interface called?': 'display port',
        'What is the name of the system that translates domain names into IP addresses?': 'dns',
        'What protocol is used with NVMe to communicate with the CPU?': 'pcie',
        'What is the name for the storage built into the CPU that temporarily stores data?': 'cache'
    }

    correct = 0
    for question, expected_answer in random.sample(list(question_list.items()), 3):
        answer = input(f'{question} ')
        if answer.strip().lower() == expected_answer:
            correct += 1
    return correct