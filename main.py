#!/bin/python3
import numpy as np

def main():
    #print(parse_file("inputs/a.txt"))

    duration, nb_intersec, adj, streets, cars = parse_file("inputs/b.txt")
    print(streets)

    path_duration = []

    for index, car in enumerate(cars):
        print(car)
        sum_street = 0
        for street in car[1:]:
            sum_street += streets[street][2]

        path_duration.append(sum_street)

    print(max(path_duration))
    print(np.mean([len(i) for i in cars]))



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
            if origin not in adj:
                adj[origin] = dict()
            adj[origin][dest] = (street[2], int(street[3]))

            streets[street[2]] = (origin, dest, int(street[3]))

        # Cars
        cars = []
        for i in range(nb_cars):
            car = f.readline().replace('\n', '').split(" ")
            cars.append(car[1:])



        return duration, nb_intersec, adj, streets, cars



main()
