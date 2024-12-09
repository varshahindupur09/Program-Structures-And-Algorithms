class Vehicle(Enum):
  CAR = 1
  TRUCK = 2
  TWO_WHEELERS = 3
  (# 'small', 'medium', 'large')

class Vehicle:
  # license plate
  pass

class ParkingSpot:
  # floors, per floot parking spot = 10, spot_id, size(# 'small', 'medium', 'large'), reservations (handicap), occupied, vehicle
  def can_fit_vehicle(self, vehicle):
    occupied or not -> false
    size_hirerachy = {'small':1, 'medium':2, 'large':3}
  return size_hirerachy[self.size] >= size_hirerachy[vehicle.size]

  def park_vehicle(self):
    if self.can_fit_vehicle(vehicle):
      self.is_occupied = True
      self.vehicle = vehicle
      return True
    return False

  def remove_vehicle(self):
    # not occupied return None
    self.is_occupied = False
    self.vehicle = None
    return vehicle


class ParkingLot:
    def __init__(self, num_small, num_medium, num_large):
        self.spots = []
        for i in range(num_small):
            self.spots.append(ParkingSpot(f"S{i+1}", 'small'))
        for i in range(num_medium):
            self.spots.append(ParkingSpot(f"M{i+1}", 'medium'))
        for i in range(num_large):
            self.spots.append(ParkingSpot(f"L{i+1}", 'large'))

    def find_available_spot(self, vehicle):
        for spot in self.spots:
            if spot.can_fit_vehicle(vehicle):
                return spot
        return None

    def park_vehicle(self, vehicle):
        spot = self.find_available_spot(vehicle)
        if spot:
            spot.park_vehicle(vehicle)
            print(f"Vehicle {vehicle.license_plate} parked in spot {spot.spot_id}.")
            return True
        print(f"No available spot for vehicle {vehicle.license_plate}.")
        return False

    def remove_vehicle(self, license_plate):
        for spot in self.spots:
            if spot.is_occupied and spot.vehicle.license_plate == license_plate:
                removed_vehicle = spot.remove_vehicle()
                print(f"Vehicle {license_plate} removed from spot {spot.spot_id}.")
                return removed_vehicle
        print(f"Vehicle {license_plate} not found.")
        return None

    def display_parking_lot(self):
        for spot in self.spots:
            status = f"Occupied by {spot.vehicle.license_plate}" if spot.is_occupied else "Available"
            print(f"Spot {spot.spot_id} ({spot.size}): {status}")
