import hashlib
import json
from collections import defaultdict
from datetime import datetime
from bisect import insort_left

# Basic encryption for sensitive data
def encrypt_data(data, key):
    return hashlib.sha256(f"{data}{key}".encode()).hexdigest()

class Node:
    def __init__(self, patient_id, patient_name, next=None):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.left = None
        self.right = None

class PatientTree:
    def __init__(self):
        self.root = None

    def insert(self, patient_id, patient_name):
        if self.root is None:
            self.root = Node(patient_id, patient_name)
        else:
            self._insert(self.root, patient_id, patient_name)

    def _insert(self, node, patient_id, patient_name):
        if patient_id < node.patient_id:
            if node.left is None:
                node.left = Node(patient_id, patient_name)
            else:
                self._insert(node.left, patient_id, patient_name)
        else:
            if node.right is None:
                node.right = Node(patient_id, patient_name)
            else:
                self._insert(node.right, patient_id, patient_name)

    def search(self, patient_id):
        return self._search(self.root, patient_id)

    def _search(self, node, patient_id):
        if node is None:
            return None
        if patient_id == node.patient_id:
            return node.patient_name
        elif patient_id < node.patient_id:
            return self._search(node.left, patient_id)
        else:
            return self._search(node.right, patient_id)

class Schedule:
    def __init__(self):
        self.appointments = defaultdict(list)

    def add_appointment(self, doctor_id, time_slot):
        self.appointments[doctor_id].append(time_slot)
        self.appointments[doctor_id].sort()

    def get_schedule(self, doctor_id):
        return self.appointments.get(doctor_id, [])

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] -= quantity
            if self.items[item_name] <= 0:
                del self.items[item_name]
        else:
            print(f"Item {item_name} not found in inventory.")

    def check_stock(self, item_name):
        return self.items.get(item_name, 0)

    def low_stock_alert(self, threshold=5):
        return {item: qty for item, qty in self.items.items() if qty < threshold}

# Example Usage
def main():
    # Setup
    key = 'secret_key'  # Encryption key
    patient_tree = PatientTree()
    schedule = Schedule()
    inventory = Inventory()

    # Insert patient records
    patient_tree.insert(1, encrypt_data('John Doe', key))
    patient_tree.insert(2, encrypt_data('Jane Smith', key))

    # Schedule appointments
    schedule.add_appointment('Dr. Adams', '2024-08-01 09:00')
    schedule.add_appointment('Dr. Adams', '2024-08-01 10:00')

    # Manage inventory
    inventory.add_item('Aspirin', 10)
    inventory.add_item('Bandages', 20)
    inventory.remove_item('Aspirin', 5)
    
    # Outputs
    print("Patient Record for ID 1:", patient_tree.search(1))
    print("Doctor Adams Schedule:", schedule.get_schedule('Dr. Adams'))
    print("Aspirin Stock Level:", inventory.check_stock('Aspirin'))
    print("Low Stock Alerts:", inventory.low_stock_alert())

if __name__ == '__main__':
    main()
import hashlib
import json
from collections import defaultdict
from datetime import datetime
from bisect import insort_left

# Basic encryption for sensitive data
def encrypt_data(data, key):
    return hashlib.sha256(f"{data}{key}".encode()).hexdigest()

class Node:
    def __init__(self, patient_id, patient_name, next=None):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.left = None
        self.right = None

class PatientTree:
    def __init__(self):
        self.root = None

    def insert(self, patient_id, patient_name):
        if self.root is None:
            self.root = Node(patient_id, patient_name)
        else:
            self._insert(self.root, patient_id, patient_name)

    def _insert(self, node, patient_id, patient_name):
        if patient_id < node.patient_id:
            if node.left is None:
                node.left = Node(patient_id, patient_name)
            else:
                self._insert(node.left, patient_id, patient_name)
        else:
            if node.right is None:
                node.right = Node(patient_id, patient_name)
            else:
                self._insert(node.right, patient_id, patient_name)

    def search(self, patient_id):
        return self._search(self.root, patient_id)

    def _search(self, node, patient_id):
        if node is None:
            return None
        if patient_id == node.patient_id:
            return node.patient_name
        elif patient_id < node.patient_id:
            return self._search(node.left, patient_id)
        else:
            return self._search(node.right, patient_id)

class Schedule:
    def __init__(self):
        self.appointments = defaultdict(list)

    def add_appointment(self, doctor_id, time_slot):
        self.appointments[doctor_id].append(time_slot)
        self.appointments[doctor_id].sort()

    def get_schedule(self, doctor_id):
        return self.appointments.get(doctor_id, [])

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] -= quantity
            if self.items[item_name] <= 0:
                del self.items[item_name]
        else:
            print(f"Item {item_name} not found in inventory.")

    def check_stock(self, item_name):
        return self.items.get(item_name, 0)

    def low_stock_alert(self, threshold=5):
        return {item: qty for item, qty in self.items.items() if qty < threshold}

# Example Usage
def main():
    # Setup
    key = 'secret_key'  # Encryption key
    patient_tree = PatientTree()
    schedule = Schedule()
    inventory = Inventory()

    # Insert patient records
    patient_tree.insert(1, encrypt_data('John Doe', key))
    patient_tree.insert(2, encrypt_data('Jane Smith', key))

    # Schedule appointments
    schedule.add_appointment('Dr. Adams', '2024-08-01 09:00')
    schedule.add_appointment('Dr. Adams', '2024-08-01 10:00')

    # Manage inventory
    inventory.add_item('Aspirin', 10)
    inventory.add_item('Bandages', 20)
    inventory.remove_item('Aspirin', 5)
    
    # Outputs
    print("Patient Record for ID 1:", patient_tree.search(1))
    print("Doctor Adams Schedule:", schedule.get_schedule('Dr. Adams'))
    print("Aspirin Stock Level:", inventory.check_stock('Aspirin'))
    print("Low Stock Alerts:", inventory.low_stock_alert())

if __name__ == '__main__':
    main()
