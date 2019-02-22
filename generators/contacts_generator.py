from model.contacts import Contact
from utils.utils import random_string
import os, jsonpickle


def generate_contacts_data(num_of_elms):
    testdata = [
        Contact(random_string("name", 20), random_string("header", 20), random_string("footer", 20), None)
        for i in range(num_of_elms)
    ]
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/contacts.json")
    with open(file, "w") as f:
        f.write(jsonpickle.encode(testdata))


def get_contacts():
    generate_contacts_data(3)
    jsonpickle.set_encoder_options("json")
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/contacts.json")) as file:
        return jsonpickle.decode(file.read())
