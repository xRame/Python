import websocket
import re

my_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZHIuaGFvb29vb29zNkB5YW5kZXgucnUiLCJpYXQiOjE2MDY1ODMzMTQsImV4cCI6MTYwNjU4NjkxNCwiaXNzIjoiaHR0cHM6Ly93ZWItcHJvZ3JhbW1pbmctMjAyMC53ZWIuYXBwIn0.4Or4UWA8BTB4u7tCcNJ3BzyDui7jYvNEgWR4sLTRBbg"
websocket_resource_url = "wss://validator-2020.awesomestuff.in/dispatcher"


def on_message(ws, message):
    print(message)
    if re.match(package_to_robot, message):
        current_package = re.findall(r'[A-Z]', message)[0]
        current_robot = int(re.findall(r'[0-9]+', message)[0]) - 1
        robots_packages[current_robot].append(current_package)
    if re.match(robot_to_robot, message):
        current_robots = re.findall(r'[0-9]+', message)
        robots_instruction[int(current_robots[0]) - 1].append(int(current_robots[1]) - 1)
    if re.match(robot_to_delivery, message):
        current_robots = re.findall(r'[0-9]+', message)
        robots_instruction[int(current_robots[0]) - 1].append(-1)

    for i in range(len(robots_packages)):
        if len(robots_packages[i]) > 0 and len(robots_instruction[i]) > 0:
            package = robots_packages[i].pop(0)
            instruction = robots_instruction[i].pop(0)
            if instruction == -1:
                delivery_sequence.append(package)
            else:
                robots_packages[instruction].append(package)
    print(robots_packages)
    print(robots_instruction)
    delivery = ''.join(delivery_sequence)
    print(delivery)
    if len(delivery) == 20:
        print(delivery)
        exit(0)


def on_open(ws):
    ws.send('init {}'.format(my_token))


if __name__ == "__main__":
    websocket.enableTrace(True)
    wss = websocket.WebSocketApp(websocket_resource_url, on_message=on_message)
    package_to_robot = r'package [A-Z] goes to robot [0-9]+'
    robot_to_delivery = r'robot [0-9]+ gives package to delivery'
    robot_to_robot = r'robot [0-9]+ gives package to robot [0-9]+'
    robots_packages = [[] for i in range(20)]
    robots_instruction = [[] for i in range(20)]
    delivery_sequence = []
    wss.on_open = on_open
    wss.run_forever()
