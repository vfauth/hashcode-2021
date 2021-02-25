#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import math

def main():
    #print(parse_file("inputs/a.txt"))

    duration, nb_intersec, adj, streets, cars = parse_file("inputs/b.txt")
    # print(streets)

    path_duration = []
    light_rotation = 20

    for index, car in enumerate(cars):
        # print(car)
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

    schedule = dict()
    for dest in adj:
        nb_incoming_cars=0
        for origin in adj[dest]:
            nb_incoming_cars += incoming_streets[adj[dest][origin][0]]

        if nb_incoming_cars !=0:
            schedule[dest]=dict()
            for origin in adj[dest]:
                schedule[dest][adj[dest][origin][0]] = math.ceil(incoming_streets[adj[dest][origin][0]]/nb_incoming_cars*light_rotation)

    output(schedule)



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



        return duration, nb_intersec, adj, streets, cars

def output(dict_data):
    f = open('output.txt', 'w')
    nb_keys = len(dict_data.keys())
    out = str(nb_keys) + '\n'
    for iterationID in dict_data.keys():
        out += str(iterationID) + '\n'
        nb_road_for_intersection = len(dict_data[iterationID])
        out += str(nb_road_for_intersection) + '\n'
        for street in dict_data[iterationID]:
            out += street + ' '  # street name
            out += str(dict_data[iterationID][street])   # light duration for street
            out += '\n'
    f.write(out)
    f.close()

    return out

main()
