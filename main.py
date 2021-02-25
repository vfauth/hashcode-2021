#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import math

def main():
    # for dataset in ("a", "b", "c", "d", "e", "f"):
    for dataset in ("e"):
        duration, nb_intersec, bonus_score, adj, streets, cars = parse_file(f"inputs/{dataset}.txt")

        path_duration = []
        light_rotation = min(5, duration)

        for index, car in enumerate(cars):
            sum_street = 0
            for street in car[1:]:
                sum_street += streets[street][2]

            path_duration.append(sum_street)

        # print(max(path_duration))
        # print(np.mean([len(i) for i in cars]))
        # plt.hist(path_duration, bins=50)
        # plt.show()
        incoming_streets = {i:0 for i in streets}

        for car in cars:
            for street in car:
                incoming_streets[street]+=1

        # plt.hist([incoming_streets[name] for name,street in streets.items() if street[1]==499])
        # plt.show()

        starting_cars = {}
        for dest in adj:
            starting_cars[dest] = {}
            for origin in adj[dest]:
                starting_cars[dest][origin] = 0
        for car in cars:
            starting_cars[streets[car[0]][1]][streets[car[0]][0]] += 1

        schedule = dict()
        for dest in adj:
            total_intersec_incoming_cars = 0 # Total number of cars
            for origin in adj[dest]:
                total_intersec_incoming_cars += incoming_streets[adj[dest][origin][0]]

            if total_intersec_incoming_cars !=0:
                schedule[dest] = []
                for origin in adj[dest]:
                    incoming_cars = incoming_streets[adj[dest][origin][0]]
                    schedule[dest].append((adj[dest][origin][0], min(max(starting_cars[dest][origin], 1), duration)))

        for dest in schedule:
            schedule[dest].sort(key=lambda x: x[1], reverse=True)
        write_output(f"outputs/{dataset}.txt", schedule)



def parse_file(path):
    with open(path, "r") as f:
        # First line
        counts = f.readline().split(" ")
        duration = int(counts[0])
        nb_intersec = int(counts[1])
        nb_streets = int(counts[2])
        nb_cars = int(counts[3])
        bonus_score = int(counts[4])

        # Streets
        streets = dict()

        adj = dict()
        for i in range(nb_streets):
            street = f.readline().split(" ")
            origin = int(street[0])
            dest = int(street[1])
            if dest not in adj:
                adj[dest] = dict()
            adj[dest][origin] = (street[2], int(street[3]))

            streets[street[2]] = (origin, dest, int(street[3]))

        # Cars
        cars = []
        for i in range(nb_cars):
            car = f.readline().replace('\n', '').split(" ")
            cars.append(car[1:])



        return duration, nb_intersec, bonus_score, adj, streets, cars

def write_output(path, dict_data):
    # Input: {intersec_id: [(street_name, duration)]}
    with open(path, 'w') as f:
        nb_keys = len(dict_data.keys())
        out = str(nb_keys) + '\n'
        for intersec_id in dict_data.keys():
            out += str(intersec_id) + '\n'
            out += str(len(dict_data[intersec_id])) + '\n'
            for street in dict_data[intersec_id]:
                out += street[0] + ' '  # street name
                out += str(street[1])   # light duration for street
                out += '\n'
        f.write(out)

main()
