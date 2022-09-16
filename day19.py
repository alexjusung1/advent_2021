from collections import Counter
from itertools import combinations
import numpy as np
from txt_input.filepath import get_text

ROTATIONS = []
neg_matrix = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], np.int8)

rot = np.identity(3, dtype=np.int8)
for _ in range(6):
    for matrix in neg_matrix:
        ROTATIONS.append(matrix.reshape(3, 1) * rot)
    rot[0] = -rot[0]
    if _ % 2:
        rot[[0, 1]] = rot[[1, 0]]
    else:
        rot[[1, 2]] = rot[[2, 1]]

class Scanner(object):
    def __init__(self, report: str):
        id_str, *beacon_rel_pos = report.splitlines()
        self.beacon_rel_pos = np.array([list(map(int, beacon.split(','))) for beacon in beacon_rel_pos], np.int16)
        self.scanner_id = int(id_str.split()[-2])
        self.next_scanners: list['Scanner'] = []
        self.noconnect = set()  # Stores id of not connected scanners
        
        # beacon_rel_pos @ parent_rot + parent_pos -> parent_rel_pos
        # Since rotations are all 90 degrees, order X matter
        self.parent_pos = np.zeros((3,), np.int16)
        self.parent_rot = np.identity(3, dtype=np.int8)
    
    def link_scanner(self, other: 'Scanner'):
        self_eval = self.beacon_rel_pos[:, np.newaxis, ...]
        if other.scanner_id not in self.noconnect:
            for rot in ROTATIONS:
                other_beacons = (other.beacon_rel_pos @ rot)[np.newaxis, ...]
                beacon_diffs = (self_eval - other_beacons).reshape(-1, 3)
                common_pos, freq = Counter(map(tuple, beacon_diffs)).most_common(1)[0]
                if freq >= 12:
                    other.parent_pos = np.array(common_pos)
                    other.parent_rot = rot
                    self.next_scanners.append(other)
                    return True
            self.noconnect.add(other.scanner_id)
        return any(children.link_scanner(other) for children in self.next_scanners)
    
    def get_scanners(self):
        scanner_pos = {tuple(self.parent_pos)}
        for scanner in self.next_scanners:
            for pos in scanner.get_scanners():
                scanner_pos.add(tuple(pos @ self.parent_rot + self.parent_pos))
        return scanner_pos
        
    def get_beacons(self):
        tot = set(map(tuple, self.beacon_rel_pos))
        for scanner in self.next_scanners:
            tot.update(scanner.get_beacons())
        return set(tuple(beacon @ self.parent_rot + self.parent_pos) for beacon in tot)

first, *rest = scanners = [Scanner(report) for report in get_text('day19.txt').split('\n\n')]
while rest:
    unconnected = []
    for scanner in rest:
        if not first.link_scanner(scanner):
            unconnected.append(scanner)
    rest = unconnected

print(len(first.get_beacons()))
max_dist = 0
for scanner1, scanner2 in combinations(first.get_scanners(), 2):
    max_dist = max(max_dist, sum(abs(a - b) for a, b in zip(scanner1, scanner2)))
print(max_dist)
